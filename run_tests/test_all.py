import pytest
import subprocess
import sys


@pytest.mark.a
def test_a():
    assert subprocess.run('run_tests/a_test.sh', shell=True,
                          stdout=sys.stdout, stderr=sys.stderr).returncode == 0
    # assert os.waitstatus_to_exitcode(os.system('nddc_test.sh')) == 0  # python 3.10


@pytest.mark.b
def test_b():
    assert subprocess.run('run_tests/b_test.sh', shell=True,
                          stdout=sys.stdout, stderr=sys.stderr).returncode == 0
    # assert os.waitstatus_to_exitcode(os.system('nvs_test.sh')) == 0   # python 3.10
