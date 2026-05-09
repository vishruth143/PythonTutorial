"""
test_class_scope.py – demonstrates CLASS scope.

`class_user` is created once before the first method of each class runs
and torn down after the last method finishes.
Two different classes → two separate fixture instances.
"""

import pytest


@pytest.mark.usefixtures("class_user")
class TestAdminUser:
    """All methods share ONE `class_user` instance."""

    def test_user_has_id(self, class_user):
        assert class_user["id"] == 1

    def test_user_name(self, class_user):
        assert class_user["name"] == "Alice"

    def test_user_is_admin(self, class_user):
        assert class_user["role"] == "admin"

    def test_mutate_shared_user(self, class_user):
        """
        Mutations to the dict ARE visible to later methods in the SAME class
        because they all share the same object.
        """
        class_user["extra"] = "shared-data"
        assert "extra" in class_user

    def test_mutation_visible_in_next_method(self, class_user):
        """Confirms the mutation from the previous method persists."""
        assert class_user.get("extra") == "shared-data"


class TestGuestUser:
    """A second class gets a FRESH `class_user` instance (no 'extra' key)."""

    def test_fresh_user_has_no_extra_key(self, class_user):
        """'extra' key must NOT exist – this is a new fixture instance."""
        assert "extra" not in class_user

    def test_guest_can_modify_locally(self, class_user):
        class_user["role"] = "guest"
        assert class_user["role"] == "guest"

