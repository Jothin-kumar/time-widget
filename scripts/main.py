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
"""
import pytz
from datetime import datetime
from tkinter import END

from countries import countries, Country
import gui


def get_time(timezone):
    return datetime.now(pytz.timezone(timezone))


for country in countries:
    gui.countries_list_box.insert(END, f'{country.full_name} - {country.iso3166_code}')


def set_timezones(iso3166_code):
    gui.time_zone_listbox.delete(0, END)
    for timezone in Country(iso3166_code).timezones:
        gui.time_zone_listbox.insert(END, timezone)


def show_time(timezone):
    timezone_ = pytz.timezone(timezone)
    now = datetime.now(timezone_)
    time = f'{now.hour}:{now.minute}:{now.second}'
    gui.set_time(time)


gui.set_on_country_select(set_timezones)
gui.set_on_timezone_select(show_time)
gui.mainloop()
