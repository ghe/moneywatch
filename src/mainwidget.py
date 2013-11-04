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

from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty,
    BooleanProperty,
)
from kivy.clock import Clock

class MainWidget(Widget):
    wanna_quit = BooleanProperty(False)
    running = BooleanProperty(False)
    total = NumericProperty(0.00)
    total_at_last_start = NumericProperty(0.00)
    time_at_last_start = NumericProperty(0.00)
    rate = NumericProperty(0.00)

    def update(self, dt):
       if (self.running):
           run_time = Clock.get_boottime() - self.time_at_last_start
           self.total = self.total_at_last_start + (run_time * (self.rate / 3600.0))

    def on_btn_start(self, str_rate):
        try:
            rate = float(str_rate)
        except ValueError:
            return

        self.rate = rate
        self.running = True
        self.time_at_last_start = Clock.get_boottime()
        self.total_at_last_start = self.total

    def on_btn_stop(self):
        self.running = False

    def on_btn_reset(self):
        self.time_at_last_start = Clock.get_boottime()
        self.total_at_last_start = 0
        self.total = 0

    def on_btn_exit(self):
        wanna_quit = True
