import pytest

@pytest.mark.run(order=2)
def test_demo1_methodA(oneTimeSetUp, setUp):
    print("Running conftest demo1 method A")

@pytest.mark.run(order=3)
def test_demo1_methodB(oneTimeSetUp, setUp):
    print("Running conftest demo1 method B")
