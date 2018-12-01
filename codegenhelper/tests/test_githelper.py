from ..githelper import get_tag
from nose import with_setup
from ..env import init_test_folder, test_root, remove_test_folder
from assertpy import assert_that
import logging
import os

logging.basicConfig(level = logging.DEBUG)

def setup_folder():
    init_test_folder()

@with_setup(setup_folder, remove_test_folder)
def test_get_tag():
    get_tag("git@github.com:cao5zy/testrepo.git", "v0.0.1", test_root())
    assert_that(os.path.join(test_root(),"testrepo", "README.md")).exists()
        
