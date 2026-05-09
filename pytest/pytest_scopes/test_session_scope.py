"""
test_session_scope.py – demonstrates SESSION scope.

`session_db` is created ONCE at the very start of the test run and
torn down after ALL tests across ALL files finish.
Every test that requests it receives the exact same object.
"""


def test_db_connection_is_open(session_db):
    """DB should be open at the start of the session."""
    assert session_db["connection"] == "open"


def test_db_initial_query_count(session_db):
    """
    The query count starts at 0, but other test files that run BEFORE this
    one may have already incremented it (session scope = one shared object).
    We therefore only assert it is non-negative, which is always true.

    TIP: to guarantee ordering, use pytest-ordering or restructure your tests.
    """
    assert session_db["queries"] >= 0


def test_db_increment_queries(session_db):
    """Simulate running a query."""
    session_db["queries"] += 1
    assert session_db["queries"] >= 1


def test_db_query_count_accumulates(session_db):
    """
    Because session scope shares ONE instance, the counter incremented
    in any previous test is visible here.
    """
    assert session_db["queries"] >= 1


def test_db_add_metadata(session_db):
    """Additional metadata attached to the DB persists for the session."""
    session_db["version"] = "PostgreSQL 16"
    assert session_db["version"] == "PostgreSQL 16"


def test_db_metadata_still_present(session_db):
    """Metadata set in the previous test is still there."""
    assert session_db.get("version") == "PostgreSQL 16"

