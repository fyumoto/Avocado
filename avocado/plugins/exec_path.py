# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright: Red Hat Inc. 2013-2015
"""
Libexec PATHs modifier
"""

from pkg_resources import resource_filename
from avocado.core.output import LOG_UI
from avocado.core.plugin_interfaces import CLICmd


class ExecPath(CLICmd):

    """
    Implements the avocado 'exec-path' subcommand
    """

    name = 'exec-path'
    description = 'Returns path to avocado bash libraries and exits.'

    def run(self, args):
        """
        Print libexec path and finish

        :param args: Command line args received from the run subparser.
        """
        LOG_UI.debug(resource_filename("avocado", "libexec"))
