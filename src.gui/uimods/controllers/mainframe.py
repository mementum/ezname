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

from uimods.aboutdialog import AboutDialog
from utils.mvc import DynBind, PubRecv
import utils.wxfb as wxfb
import wx

import models.mainmodel as mainmodel

if True:
    # @DynBind.EVT_BUTTON.Button.AboutDialog
    @DynBind.EVT_TOOL.Tool.AboutDialog
    @DynBind.EVT_MENU.MenuItem.AboutDialog
    def OnEventAboutDialog(self, event):
        event.Skip()
        dialog = AboutDialog(self)
        dialog.ShowModal()

if True:
    # @DynBind.EVT_BUTTON.Button.ClearRegistry
    # @DynBind.EVT_TOOL.Tool.ClearRegistry
    @DynBind.EVT_MENU.MenuItem.ClearRegistry
    def OnEventClearRegistry(self, event):
        event.Skip()
        config = wx.Config.Get()
        config.DeleteAll()
        self.Close()

if True:
    def __init__(self, parent):
        # Path to scan
        wxfb.BindingDirPicker('workdir')

        # Path to move dirs to in directorize
        wxfb.BindingDirPicker('dirdirectorize')

        # ListBoxes for source and destination
        wxfb.BindingListBox('fnoriginal', config=False)
        wxfb.BindingListBox('fnfinal', config=False)

        # Buttons
        wxfb.BindingButton('refresh', pubmethod=self.OnButtonRefresh)
        wxfb.BindingButton('execute', pubmethod=self.OnButtonExecute)

        wxfb.BindingButton('executedirectorize',
                           pubmethod=self.OnButtonExecuteDirectorize)
        wxfb.BindingButton('refreshdirectorize',
                           pubmethod=self.OnButtonRefreshDirectorize)

        wxfb.BindingButton('openlog', pubmethod=self.OnOpenLog)

        # CheckBoxes for Options
        wxfb.BindingCheckBox('loadonstart', default=True)

        wxfb.BindingCheckBox('dirsdelete', default=True)
        wxfb.BindingCheckBox('dirspurgeempty', default=True)
        wxfb.BindingCheckBox('movedirectorize', default=True)
        wxfb.BindingCheckBox('rundry', default=False)

        # Input extensions and matching re
        wxfb.BindingTextCtrlFocus('knownextensions',
                                  default='mp4;mkv;avi;mpg;mpeg2')

        wxfb.BindingTextCtrlFocus('rexp', default=r'(.+)\[.+\]\.?.*')

        # Matches: NameSXXEYYMORENAMES.ext
        # Skips the entry iy MORENAMES has []
        wxfb.BindingTextCtrlFocus(
            'regexpdirectorize', default=r'(.+)\.S([0-9]+)E.+\.[^\[\]]+\.(.+)')

        self.model = mainmodel.MainModel()
        if self.loadonstart.value:
            self.do_refresh()

if True:
    btext = {False: 'Open Log', True: 'Hide Log'}

    def OnOpenLog(self, msg):
        newstatus = not self.m_panelLog.IsShown()
        self.m_panelLog.Show(newstatus)
        self.m_buttonOpenLog.SetLabel(btext[newstatus])

        # Recalculate size and fit the window to the minimum new size
        self.view.SetMinSize(self.view.GetSizer().GetMinSize())
        self.view.Fit()

if True:
    def do_refresh(self):
        self.do_prepare_model()
        self.model.refresh()

    def do_execute(self):
        self.do_prepare_model()
        self.model.execute()

if True:
    def do_refreshdirectorize(self):
        self.do_prepare_model()
        self.model.refresh_directorize()

    def do_executedirectorize(self):
        self.do_prepare_model()
        self.model.execute_directorize()

if True:
    def do_prepare_model(self):
        self.model.rexp = self.rexp.value
        self.model.workdir = self.workdir.value or '.'  # safe default
        self.model.knownextensions = self.knownextensions.value
        self.model.dirspurgeempty = self.dirspurgeempty.value
        self.model.dirsdelete = self.dirsdelete.value
        self.model.regexpdirectorize = self.regexpdirectorize.value
        self.model.movedirectorize = self.movedirectorize.value
        self.model.dirdirectorize = self.dirdirectorize.value

        self.model.rundry = self.rundry.value

if True:
    @PubRecv.evt_dirpicker_changed.workdir
    def OnDirPickerChanged(self, msg):
        self.do_refresh()

if True:
    def OnButtonRefresh(self, msg):
        self.do_refresh()

if True:
    def OnButtonExecute(self, msg):
        self.do_execute()

if True:
    def OnButtonRefreshDirectorize(self, msg):
        self.do_refreshdirectorize()

if True:
    def OnButtonExecuteDirectorize(self, msg):
        self.do_executedirectorize()

if True:
    @PubRecv.evt_listbox.fnoriginal
    def OnListBoxFnOriginal(self, selection):
        self.fnfinal.selection = selection

if True:
    @PubRecv.evt_listbox.fnfinal
    def OnListBoxFnFinal(self, selection):
        self.fnoriginal.selection = selection

if True:
    @PubRecv.model.executed.entries
    def OnModelExecutedEntries(self, msg):
        self.do_refresh()

if True:
    @PubRecv.model.executed.directorize
    def OnModelExecutedDirectorize(self, msg):
        self.do_refreshdirectorize()
