#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
#  Copyright (C) 2015 Daniel Rodriguez
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import collections
import glob
import re
import Queue
import os
import os.path
import shutil
import threading


from utils.mvc import DynamicClass, PubSend


@DynamicClass(moddirs=['modules'])
class MainModel(threading.Thread):

    def __init__(self):
        super(MainModel, self).__init__()

        self.q = Queue.Queue()

        self.daemon = True  # exit on shutdown
        self.start()

        self.rexp = ''
        self.workdir = ''
        self.knownextensions = ''
        self.dirspurgeempty = False
        self.dirsdelete = False

        self.rundry = False

        self.regexpdirectorize = ''
        self.dirdirectorize = ''
        self.movedirectorize = False

        self.fentries = collections.OrderedDict()
        self.dentries = collections.OrderedDict()
        self.fdirect = collections.OrderedDict()

    MSG_REFRESH, MSG_EXECUTE, \
        MSG_REFRESHDIRECTORIZE, MSG_EXECUTEDIRECTORIZE = range(4)

    def run(self):
        while True:
            msg = self.q.get(block=True, timeout=None)
            if msg is None:
                return

            if msg == self.MSG_REFRESH:
                self.refreshing()

            elif msg == self.MSG_EXECUTE:
                self.executing()

            elif msg == self.MSG_REFRESHDIRECTORIZE:
                self.refreshing_directorize()

            elif msg == self.MSG_EXECUTEDIRECTORIZE:
                self.executing_directorize()

    @PubSend('model.refreshing.entries')
    def refresh(self):
        self.q.put(self.MSG_REFRESH)

    @PubSend('model.refreshed.entries')
    def refreshing(self):
        # Prepare the regular expression and extensions
        rexp = re.compile(self.rexp)
        kexts = ['.' + x.strip() for x in self.knownextensions.split(';')]

        self.fentries = collections.OrderedDict()
        self.dentries = collections.OrderedDict()

        for entry in sorted(os.listdir(self.workdir)):
            fqentry = os.path.join(self.workdir, entry)

            match = rexp.match(entry)
            if not match:
                continue

            if os.path.isfile(fqentry):
                froot, fext = os.path.splitext(entry)
                if fext and fext in kexts:
                    newentry = match.group(1) + fext
                    self.fentries[entry] = newentry

            elif os.path.isdir(fqentry):
                # must look into the directory - match known extensions
                subdirentries = os.listdir(fqentry)
                if not subdirentries:
                    if self.dirspurgeempty:
                        self.dentries[entry] = ''
                else:
                    for subentry in subdirentries:
                        fname, fext = os.path.splitext(subentry)
                        if not fext or fext not in kexts:
                            continue
                        newentry = match.group(1) + fext
                        dentry = os.path.join(entry, subentry)
                        self.dentries[dentry] = newentry
                        break

        return self.dentries, self.fentries

    @PubSend('model.refreshing.directorize')
    def refresh_directorize(self):
        self.q.put(self.MSG_REFRESHDIRECTORIZE)

    @PubSend('model.refreshed.directorize')
    def refreshing_directorize(self):
        # Prepare the regular expression and extensions
        rexp = re.compile(self.regexpdirectorize)
        kexts = [x.strip() for x in self.knownextensions.split(';')]

        self.fdirect = collections.OrderedDict()

        for entry in sorted(os.listdir(self.workdir)):
            fqentry = os.path.join(self.workdir, entry)

            if os.path.isfile(fqentry):
                match = rexp.match(entry)
                if match:
                    if match.group(3) in kexts:
                        dirname = match.group(1)
                        season = 'Season' + match.group(2)
                        newentry = os.path.join(dirname, season, entry)
                        self.fdirect[entry] = newentry

        return self.fdirect

    @PubSend('model.executing.directorize')
    def execute_directorize(self):
        self.q.put(self.MSG_EXECUTEDIRECTORIZE)

    @PubSend('model.executed.directorize')
    def executing_directorize(self):
        if not self.fdirect:
            self.log('- No items to directorize')
            return

        if not self.dirdirectorize:
            self.log('- No target directory specified')
            return

        # Prepare the target dir is needed
        if self.movedirectorize and self.dirdirectorize:
            if not os.path.isdir(self.dirdirectorize):
                self.log('- Making final targetdir: %s' % self.dirdirectorize)
                if not self.rundry:
                    os.mkdir(self.dirdirectorize)

        for entry, newentry in self.fdirect.items():
            basedir, sdir, _ = newentry.split(os.sep)

            if self.movedirectorize and self.dirdirectorize:
                fbasedir = os.path.join(self.dirdirectorize, basedir)
            else:
                fbasedir = os.path.join(self.workdir, basedir)

            if not os.path.isdir(fbasedir):
                self.log('- Making basedir: %s' % fbasedir)
                if not self.rundry:
                    os.mkdir(fbasedir)

            fsdir = os.path.join(fbasedir, sdir)
            if not os.path.isdir(fsdir):
                self.log('- Making sdir: %s' % fsdir)
                if not self.rundry:
                    os.mkdir(fsdir)

            self.log('- Moving file to dir')
            src = os.path.join(self.workdir, entry)
            dst = os.path.join(self.dirdirectorize, newentry)
            self.log('%s -> %s' % (src, dst))
            if not self.rundry:
                shutil.move(src, dst)

    @PubSend('model.log')
    def log(self, msg):
        return msg

    @PubSend('model.executing.entries')
    def execute(self):
        self.q.put(self.MSG_EXECUTE)

    @PubSend('model.executed.entries')
    def executing(self):
        self.log('- Execution Started')
        if self.rundry:
            self.log('- Dry Run')

        self.log('- Workdir %s' % self.workdir)

        self.log('- Processing Directories')
        for src, dst in self.dentries.items():
            if not dst:
                self.log('- Removing Empty Dir')
                srcdir = os.path.join(self.workdir, src)
                self.log('-- %s' % srcdir)
                if not self.rundry:
                    shutil.rmtree(srcdir)
                continue

            self.log('- Moving + Renaming')
            self.log('-- %s -> %s' % (src, dst))
            if not self.rundry:
                src = os.path.join(self.workdir, src)
                dst = os.path.join(self.workdir, dst)
                shutil.move(src, dst)

            if self.dirsdelete:
                self.log('- Removing Directory')
                srcdir = os.path.dirname(src)
                self.log('-- %s' % srcdir)
                if not self.rundry:
                    shutil.rmtree(srcdir)

        self.log('- Processing Files')
        for src, dst in self.fentries.items():
            self.log('- Renaming')
            self.log('-- %s -> %s' % (src, dst))
            if not self.rundry:
                src = os.path.join(self.workdir, src)
                dst = os.path.join(self.workdir, dst)
                shutil.move(src, dst)

        self.log('Execution Finished')
