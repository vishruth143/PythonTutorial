"""
test_module_scope.py – demonstrates MODULE scope.

`module_client` is created ONCE when the first test in this file runs
and torn down after the last test in this file finishes.
All tests here share the exact same client object.
"""


def test_client_has_base_url(module_client):
    assert module_client["base_url"] == "https://api.example.com"


def test_client_linked_to_db(module_client):
    """The client holds a reference to the session-scoped DB."""
    assert module_client["db"]["connection"] == "open"


def test_client_add_header(module_client):
    """
    Mutating the shared client is visible to every subsequent test
    in this module (module scope means one shared instance).
    """
    module_client["headers"] = {"Accept": "application/json"}
    assert "headers" in module_client


def test_client_header_still_present(module_client):
    """Header added in the previous test is still there – same instance."""
    assert module_client.get("headers") == {"Accept": "application/json"}


def test_db_query_counter(module_client):
    """Increment a counter on the session-scoped DB via the module client."""
    module_client["db"]["queries"] += 1
    assert module_client["db"]["queries"] >= 1

