"""
conftest.py – shared fixtures across the pytest_scopes package.

Fixture Scopes
--------------
function  : (default) created & torn down for every test function
class     : created once per test class, shared by all methods in it
module    : created once per .py module, shared by all tests in the file
package   : created once per package (directory with __init__.py)
session   : created once for the entire test run
"""

import pytest


# ── SESSION scope ────────────────────────────────────────────────────────────
@pytest.fixture(scope="session")
def session_db():
    """Simulate a heavy DB connection opened once for the whole test run."""
    print("\n[session] Opening DB connection")
    db = {"connection": "open", "queries": 0}
    yield db
    print("\n[session] Closing DB connection")
    db["connection"] = "closed"


# ── PACKAGE scope ─────────────────────────────────────────────────────────────
@pytest.fixture(scope="package")
def package_config():
    """Simulate loading a config file once per package."""
    print("\n[package] Loading config")
    config = {"env": "test", "retries": 3}
    yield config
    print("\n[package] Unloading config")


# ── MODULE scope ──────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def module_client(session_db):
    """Simulate an API client created once per module."""
    print("\n[module] Creating API client")
    client = {"base_url": "https://api.example.com", "db": session_db}
    yield client
    print("\n[module] Destroying API client")


# ── CLASS scope ───────────────────────────────────────────────────────────────
@pytest.fixture(scope="class")
def class_user():
    """Simulate a user object shared across all methods in a test class."""
    print("\n[class] Creating user")
    user = {"id": 1, "name": "Alice", "role": "admin"}
    yield user
    print("\n[class] Deleting user")


# ── FUNCTION scope (default) ──────────────────────────────────────────────────
@pytest.fixture(scope="function")
def function_token():
    """Generate a fresh auth token for every single test."""
    print("\n[function] Generating token")
    token = "token-abc123"
    yield token
    print("\n[function] Invalidating token")

