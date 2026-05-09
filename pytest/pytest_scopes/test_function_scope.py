"""
test_function_scope.py – demonstrates FUNCTION scope (default).

The fixture `function_token` is created and torn down for EVERY test,
so each test gets a brand-new instance even when they run back-to-back.
"""

import pytest


def test_token_is_string(function_token):
    """Each test receives its own token."""
    assert isinstance(function_token, str)
    assert len(function_token) > 0


def test_token_value(function_token):
    """Verify the token's expected value (fresh copy each time)."""
    assert function_token == "token-abc123"


def test_token_starts_with_prefix(function_token):
    """Check prefix – still a fresh token."""
    assert function_token.startswith("token-")


def test_two_tokens_are_independent(function_token):
    """
    Modifying the token in one test must NOT affect the next test
    because each test gets its own fixture instance.
    """
    function_token = "tampered"          # local rebind only
    assert function_token == "tampered"  # change is visible here …


def test_token_unchanged_after_previous_tamper(function_token):
    """… but this test still gets the original value."""
    assert function_token == "token-abc123"

