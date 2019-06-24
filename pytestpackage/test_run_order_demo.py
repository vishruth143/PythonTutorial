# https://pytest-ordering.readthedocs.io/en/develop/
import pytest

# B, A, C, E, D, F

# @pytest.mark.run(before=' test_run_order_methodB')
# @pytest.mark.run('second')
# @pytest.mark.second
# @pytest.mark.order2
@pytest.mark.run(order=2)
def test_run_order_methodA(oneTimeSetUp, setUp):
    print("Running method A")

# @pytest.mark.run('first')
# @pytest.mark.first
@pytest.mark.run(order=1)
def test_run_order_methodB(oneTimeSetUp, setUp):
    print("Running method B")

# @pytest.mark.run(after='test_run_order_methodB')
@pytest.mark.run(order=3)
def test_run_order_methodC(oneTimeSetUp, setUp):
    print("Running method C")

@pytest.mark.run(order=5)
def test_run_order_methodD(oneTimeSetUp, setUp):
    print("Running method D")

# @pytest.mark.run('second_to_last')
# @pytest.mark.second_to_last
@pytest.mark.run(order=4)
def test_run_order_methodE(oneTimeSetUp, setUp):
    print("Running method E")

# @pytest.mark.run('last')
# @pytest.mark.last
@pytest.mark.run(order=6)
def test_run_order_methodF(oneTimeSetUp, setUp):
    print("Running method F")