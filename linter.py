#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Nikki Erwin Carpio Ramirez
# Copyright (c) 2016 Nikki Erwin Carpio Ramirez
#
# License: MIT
#

"""This module exports the Htmllint plugin class."""

from SublimeLinter.lint import NodeLinter


class Htmllint(NodeLinter):
    """Provides an interface to htmllint."""

    defaults = {
        'selector': 'text.html'
    }
    cmd = ['htmllint', '${file}']
    config_file = ('--rc', '.htmllintrc')
    regex = r'^.+: line (?P<line>\d+), col (?P<col>\d+), (?P<message>.+)'
    tempfile_suffix = '-'
