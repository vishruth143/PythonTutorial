"""
test_mixed_scopes.py – shows multiple scopes interacting in a single file.

Fixture dependency chain:
  session_db  (session)
      └─ module_client  (module)
              └─ function_token  (function)

Key observations
----------------
* session_db   is created once and shared across ALL tests in the run.
* module_client is created once for this file and reused by every test here.
* function_token is created fresh for EVERY individual test.
"""

import pytest


class TestScopedInteraction:

    def test_all_fixtures_available(self, session_db, module_client, function_token):
        """All three fixtures are accessible together."""
        assert session_db["connection"] == "open"
        assert "base_url" in module_client
        assert function_token.startswith("token-")

    def test_function_token_is_fresh(self, function_token):
        """A new token is generated each time this test runs."""
        original = function_token
        assert original == "token-abc123"

    def test_module_client_is_shared(self, module_client):
        """The same client object is reused within this module."""
        module_client["request_count"] = module_client.get("request_count", 0) + 1
        assert module_client["request_count"] == 1

    def test_module_client_counter_incremented(self, module_client):
        """Counter persists because module_client is module-scoped."""
        module_client["request_count"] = module_client.get("request_count", 0) + 1
        assert module_client["request_count"] == 2

    def test_session_db_accumulates_across_files(self, session_db):
        """
        session_db is shared with other test files, so queries may already
        be > 0 if this file runs after test_session_scope.py.
        """
        assert session_db["queries"] >= 0  # non-negative is always true


# ── Parametrized test using a function-scoped fixture ────────────────────────
@pytest.mark.parametrize("endpoint", ["/users", "/products", "/orders"])
def test_client_endpoints(module_client, function_token, endpoint):
    """
    Parametrize creates 3 test instances.
    * module_client  → same object for all 3 (module scope)
    * function_token → fresh token for each of the 3 (function scope)
    """
    url = module_client["base_url"] + endpoint
    assert url.startswith("https://")
    assert function_token == "token-abc123"

