"""
MIT License

Copyright (c) 2021 B.Jothin kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author: Jothin kumar (https://jothin.tech)
Github repository of this project: https://github.com/Jothin-kumar/time-widget
"""
import pytz
from datetime import datetime
from time import sleep
from threading import Thread
from _tkinter import TclError

from .countries import countries, Country, get_country_by_iso3166_code
from .gui import MinWidget as MinWidget_, MaxWidget as MaxWidget_

timezone = None


class MinWidget:
    def __init__(self):
        self.widget = MinWidget_()
        self.widget.set_timezone('local time')
        Thread(target=self.refresh_time).start()
        self.configure_switch_to_max = self.widget.configure_switch_to_max
        self.destroy = self.widget.destroy
        self.mainloop = self.widget.mainloop

    def refresh_time(self):
        global timezone
        try:
            while True:
                if timezone:
                    timezone_ = pytz.timezone(timezone)
                    now = datetime.now(timezone_)
                    self.widget.set_timezone(timezone)
                else:
                    now = datetime.now()
                    self.widget.set_timezone('local time')
                time = f'{now.hour}:{now.minute}:{now.second}'
                self.widget.set_time(time)
                sleep(0.1)
        except TclError:
            pass


class MaxWidget:
    def __init__(self):
        self.widget = MaxWidget_()
        self.widget.set_countries(countries)

        def on_country_selected(country):
            self.widget.set_timezones(get_country_by_iso3166_code(country).timezones)

        self.widget.set_on_country_select(on_country_selected)
        self.widget.set_on_timezone_select(self.set_timezone)
        Thread(target=self.refresh_time).start()
        self.configure_switch_to_min = self.widget.configure_switch_to_min
        self.destroy = self.widget.destroy
        self.mainloop = self.widget.mainloop

    def set_timezone(self, timezone_):
        global timezone
        timezone = timezone_

    def refresh_time(self):
        global timezone
        try:
            while True:
                if timezone:
                    timezone_ = pytz.timezone(timezone)
                    now = datetime.now(timezone_)
                else:
                    now = datetime.now()
                time = f'{now.hour}:{now.minute}:{now.second}'
                self.widget.set_time(time)
                sleep(0.1)
        except TclError:
            pass


widget = MinWidget


def main():
    global widget

    def switch_to_max_widget(evt):
        global widget
        try:
            widget.destroy()
        except AttributeError:
            pass
        widget = MaxWidget()
        widget.configure_switch_to_min(switch_to_min_widget)
        widget.mainloop()

    def switch_to_min_widget(evt):
        global widget
        try:
            widget.destroy()
        except AttributeError:
            pass
        widget = MinWidget()
        widget.configure_switch_to_max(switch_to_max_widget)
        widget.mainloop()

    switch_to_min_widget(None)
