"""
test_package_scope.py – demonstrates PACKAGE scope.

`package_config` is shared by every test inside the same *package*
(directory).  A new instance would only be created for a different package.

NOTE: package scope requires the directory to be a Python package
      (i.e. it must contain an __init__.py file).
"""


def test_config_env(package_config):
    assert package_config["env"] == "test"


def test_config_retries(package_config):
    assert package_config["retries"] == 3


def test_config_add_key(package_config):
    """
    Adding a key is visible to all tests in the package
    because they share the same config object.
    """
    package_config["timeout"] = 30
    assert package_config["timeout"] == 30


def test_config_key_persists(package_config):
    """Key added above is still present – same package-scoped instance."""
    assert package_config.get("timeout") == 30

