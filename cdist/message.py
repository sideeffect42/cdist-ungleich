# -*- coding: utf-8 -*-
#
# 2013 Nico Schottelius (nico-cdist at schottelius.org)
#
# This file is part of cdist.
#
# cdist is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cdist is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cdist. If not, see <http://www.gnu.org/licenses/>.
#
#

import fcntl
import logging
import os
import shutil
import tempfile

log = logging.getLogger(__name__)


class Message(object):
    """Support messaging between types

    """
    def __init__(self, prefix, messages):
        self.prefix = prefix
        self.global_messages = messages

        in_fd, self.messages_in = tempfile.mkstemp(suffix='.cdist_message_in')
        out_fd, self.messages_out = tempfile.mkstemp(
                suffix='.cdist_message_out')

        os.close(in_fd)
        os.close(out_fd)

        self._copy_messages()

    @property
    def env(self):
        env = {}
        env['__messages_in'] = self.messages_in
        env['__messages_out'] = self.messages_out

        return env

    def _copy_messages(self):
        """Copy global contents into our copy"""
        with open(self.global_messages, 'r+') as fmsg_global:
            try:
                fcntl.lockf(fmsg_global, fcntl.LOCK_EX)
                with open(self.messages_in, 'w') as fmsg_local:
                    shutil.copyfileobj(fmsg_global, fmsg_local)
            finally:
                fcntl.lockf(fmsg_global, fcntl.LOCK_UN)

    def _cleanup(self):
        """remove temporary files"""
        if os.path.exists(self.messages_in):
            os.remove(self.messages_in)
        if os.path.exists(self.messages_out):
            os.remove(self.messages_out)

    def _merge_messages(self):
        """Merge newly written lines into global messages file.

        Writing to the global messages file is synchronized using an fcntl lock,
        because
        """
        with open(self.global_messages, 'a') as fmsg_global:
            try:
                fcntl.lockf(fmsg_global, fcntl.LOCK_EX)
                with open(self.messages_out, 'r') as fmsg_local:
                    for line in fmsg_local:
                        fmsg_global.write('%s:%s' % (self.prefix, line))
            finally:
                fcntl.lockf(fmsg_global, fcntl.LOCK_UN)

    def merge_messages(self):
        self._merge_messages()
        self._cleanup()
