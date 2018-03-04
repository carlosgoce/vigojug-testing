import os.path


def test_assert_file_exists():
    # PHP~Java
    # $this->assertFileExists('test.txt');
    assert os.path.isfile('manage.py')
