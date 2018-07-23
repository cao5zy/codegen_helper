from nose import with_setup
from codegenhelper import put_folder, remove, put_file, compose_dir, remove_file_if_exists
from assertpy import assert_that
import os

root = "./.test_files"

def setup_collect_files_with_ext():
    put_file("cf.ce", put_folder("folder1", put_folder(root)), "")


def clear_env():
    remove(root)

@with_setup(setup_collect_files_with_ext, clear_env)
def test_collect_files_with_ext():
    assert_that(os.path.exists(compose_dir(compose_dir(root, "folder1"), "cf.ce"))).is_true()


existed_file = os.path.join( root, "x1.test")
def setup_test_remove_file_if_exists():
    put_file("x1.test", put_folder(root), "hello")

@with_setup(setup_test_remove_file_if_exists, clear_env)    
def test_remove_file_if_exists():
    assert_that(os.path.exists(remove_file_if_exists(existed_file))).is_false()
