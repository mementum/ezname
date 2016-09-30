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

from utils.mvc import PubRecv
import wx

if True:
    @PubRecv.model.refreshed.entries
    def OnModelRefreshed(self, msg):
        dentries, fentries = msg
        self.fnoriginal.items = dentries.keys() + fentries.keys()
        self.fnfinal.items = dentries.values() + fentries.values()

if True:
    @PubRecv.model.refreshed.directorize
    def OnModelRefreshedDirectorize(self, msg):
        fdirect = msg
        self.fnoriginal.items = fdirect.keys()
        self.fnfinal.items = fdirect.values()

if True:
    @PubRecv.model.executing.entries
    def OnModelLogEntries(self, msg):
        self.m_textCtrlLogExecution.Clear()

if True:
    @PubRecv.model.executing.directorize
    def OnModelLogDirectorize(self, msg):
        self.m_textCtrlLogExecution.Clear()

if True:
    @PubRecv.model.log
    def OnModelLog(self, msg):
        self.m_textCtrlLogExecution.AppendText(msg + '\n')
