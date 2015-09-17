#!/usr/bin/python3
# -*- coding: utf8 -*-
#Copyright (C) 2015 Guillaume DUPUY <glorf@glorf.fr>
#This file is part of Poe Watcher.

#PoE Watcher is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#PoE Watcher is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.

#You should have received a copy of the GNU Affero General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>
import tkinter
import tkinter.scrolledtext
import time
import logging
logger = logging.getLogger(__name__)
class Application(tkinter.Frame):
    """A really really simple application to display logs"""
    def __init__(self, actions, initial_state, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.actions = []
        self.active = initial_state
        for pr in actions:
            self.actions.append((pr[1], getattr(self, pr[2])))
    def createWidgets(self):
        self.log_display = tkinter.scrolledtext.ScrolledText(self, state='disabled')
        self.log_display.configure(font='TkFixedFont')
        self.log_display.pack()
    def parse_message(self, msg):
        for abbr, func in self.actions:
            if msg.startswith(abbr):
                func()
    def display_on(self):
        logger.info("Turning on GUI display")
        self.active = True
    def display_off(self):
        logger.info("Turning off GUI display")
        self.active = False
    def isActive(self):
        return self.active
    
