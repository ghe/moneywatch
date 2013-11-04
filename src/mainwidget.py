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
    StringProperty,
)
from kivy.clock import Clock

from datetime import timedelta

class MainWidget(Widget):
    running = BooleanProperty(False)
    total = NumericProperty(0.00)
    time_str = StringProperty("0:00:00")
    time_at_last_start = NumericProperty(0.00)
    total_time = NumericProperty(0.00)
    saved_time = NumericProperty(0.00)
    rate = NumericProperty(0.00)

    def update(self, dt):
       if (self.running):
           self.total_time = self.saved_time + Clock.get_boottime() - self.time_at_last_start
           self.total = self.total_time * (self.rate / 3600.0)
           self.time_str = str(timedelta(seconds=int(self.total_time)))

    def on_btn_start(self, str_rate):
        try:
            rate = float(str_rate)
        except ValueError:
            return

        self.rate = rate
        self.running = True
        self.time_at_last_start = Clock.get_boottime()

    def on_btn_stop(self):
        self.running = False
        self.saved_time = self.total_time

    def on_btn_reset(self):
        self.time_at_last_start = Clock.get_boottime()
        self.saved_time = 0.0
        self.time_str = "0:00:00"
        self.total = 0
