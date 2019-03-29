# Copyright (C) 2019 Cancer Care Associates

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version (the "AGPL-3.0+").

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License and the additional terms for more
# details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# ADDITIONAL TERMS are also included as allowed by Section 7 of the GNU
# Affero General Public License. These additional terms are Sections 1, 5,
# 6, 7, 8, and 9 from the Apache License, Version 2.0 (the "Apache-2.0")
# where all references to the definition "License" are instead defined to
# mean the AGPL-3.0+.

# You should have received a copy of the Apache-2.0 along with this
# program. If not, see <http://www.apache.org/licenses/LICENSE-2.0>.


"""A command line interface for the management of log files.
"""


from ..logfile import orchestration_cli


def logfile_cli(subparsers):
    logfile_parser = subparsers.add_parser(
        'logfile', help="A toolbox for managing logfiles.")
    logfile_subparsers = logfile_parser.add_subparsers(dest='logfile')

    logfile_orchestration(logfile_subparsers)


def logfile_orchestration(logfile_subparsers):
    parser = logfile_subparsers.add_parser(
        'orchestration',
        help=(
            "Manages the orchestration of Elekta Linac fetching and indexing. "
            "Designed to be scheduled to run nightly. Requires two "
            "configuration csv files to be created, one for Mosaiq SQL "
            "configuration and the other for logfile configuration."
        ))

    parser.add_argument('data_directory', type=str)

    parser.add_argument('-m', '--mosaiq_sql', type=str,
                        default=None)
    parser.add_argument('-l', '--linac_details', type=str,
                        default=None)

    parser.set_defaults(func=orchestration_cli)
