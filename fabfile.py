#!/usr/bin/env python
# encoding: utf-8
"""
Requires Python (2.6 <= version < 3.0) and [Fabric][] 0.9.

  [Fabric]: http://fabfile.org/
"""

from os.path import dirname, join, realpath

from fabric.api import local


REPO_DIR = dirname(realpath(__file__))
COMPILER_PATH = join(REPO_DIR, 'closure-compiler/compiler.jar')
PLUGIN_DIR = join(REPO_DIR, 'plugin')


def build():
    """
    Create compressed version.
    """

    local('java -jar {0} --js={1} --js_output_file={2}'.format(
        COMPILER_PATH,
        join(PLUGIN_DIR, 'jquery.typing.js'),
        join(PLUGIN_DIR, 'jquery.typing.min.js')
    ))
