##
# Copyright (c) 2013, Go West Robotics, Inc.
# All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial 3.0
# United States License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/3.0/us/ or send a letter to
# Creative Commons, 444 Castro Street, Suite 900, Mountain View, California,
# 94041, USA or view the LICENSE file included in this project.
##

import kivy
kivy.require('1.7.0')

from kivy.app import App

from mainwidget import MainWidget
from kivy.clock import Clock

class MoneyWatchApp(App):
    def build(self):
        mw = MainWidget()
        Clock.schedule_interval(mw.update, 0.05)
        return mw

    def on_pause(self):
        return True

    def on_resume(self):
        pass


