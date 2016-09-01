#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):
    TRANSFERS_FILES = True
    def run(self, tmp=None, task_vars=None):

        ''' handler for file transfer operations '''
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        remote_user = task_vars.get('ansible_ssh_user') or self._play_context.remote_user

        self._transfer_file(u"/etc/resolv.conf", u"/tmp/resolv.conf")
        self._fixup_perms(u"/tmp/resolv.conf", remote_user)
        self._remove_tmp_path(u"/tmp/resolv.conf")

        return {}
