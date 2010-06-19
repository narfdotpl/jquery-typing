#!/usr/bin/env python
# encoding: utf-8
"""
This file is used to make certain development tasks less annoying.

To take full advantage of it, you'll need Python, Fabric, Java, Ruby
and Haml.
"""

from os.path import dirname, join, realpath

from fabric.api import cd, env, local, put, run


__author__ = 'Maciej Konieczny <hello@narf.pl>'


REPO_DIR = dirname(realpath(__file__))
DEMO_DIR = join(REPO_DIR, 'demo')
PLUGIN_DIR = join(REPO_DIR, 'plugin')

COMPILER_PATH = join(REPO_DIR, 'closure-compiler/compiler.jar')
PLUGIN_PATH = join(PLUGIN_DIR, 'jquery.typing.js')
COMPRESSED_PLUGIN_PATH = join(PLUGIN_DIR, 'jquery.typing.min.js')


env.hosts = ['narf.megiteam.pl']


def build():
    """
    Create compressed version of the plugin and build demo.
    """

    compress()
    demo()


def compress():
    """
    Create compressed version of the plugin.
    """

    # compress
    local('java -jar {0} --js={1} --js_output_file={2}'.format(
          COMPILER_PATH, PLUGIN_PATH, COMPRESSED_PLUGIN_PATH))

    # copy info comment from development version
    info = ''
    with open(PLUGIN_PATH) as f:
        for line in f:
            if line.startswith('//'):
                info += line

    # add info comment to compressed version
    if info:
        with open(COMPRESSED_PLUGIN_PATH) as f:
            compressed = f.read()

        with open(COMPRESSED_PLUGIN_PATH, 'w') as f:
            f.write(info + compressed)


def demo():
    """
    Build demo.
    """

    # copy compressed plugin
    local('cp {0} {1}'.format(COMPRESSED_PLUGIN_PATH, DEMO_DIR))

    # render haml
    haml = join(DEMO_DIR, 'demo.haml')
    html = join(DEMO_DIR, 'index.html')
    local('haml {0} > {1}'.format(haml, html))


def deploy():
    """
    Update MegiTeam and push to GitHub.
    """

    # update MegiTeam
    megi()

    # push to GitHub
    local('git push --tags')


def megi():
    """
    Update MegiTeam.
    """

    # archive demo
    archive_name = 'typing.tar.bz2'
    archive_path = '/tmp/' + archive_name
    with cd(DEMO_DIR):
        local('tar -cj --exclude *.haml -f {0} *'.format(archive_path))

    # set remote directory names
    main_dir = 'narf.pl/main/on-the-stage'
    typing_dir_name = 'jquery-typing'
    typing_dir = join(main_dir, typing_dir_name)

    # create jQuery-typing directory
    with cd(main_dir):
        run("""if [ -d {0} ]; then
                rm -rf {0}/*
            else
                mkdir {0}
            fi""".format(typing_dir_name))

    # upload
    put(archive_path, typing_dir)

    # extract and remove remote archive
    with cd(typing_dir):
        run('tar xf ' + archive_name)
        run('rm ' + archive_name)

    # remove local archive
    local('rm ' + archive_path)
