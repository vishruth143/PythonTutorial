import pytest

@pytest.mark.run(order=1)
def test_demo2_methodA(oneTimeSetUp, setUp):
    print("Running conftest demo2 method A")

@pytest.mark.run(order=4)
def test_demo2_methodB(oneTimeSetUp, setUp):
    print("Running conftest demo2 method B")
