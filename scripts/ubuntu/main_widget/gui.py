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

Author: Jothin kumar (https://jothin-kumar.github.io/)
Github repository of this project: https://github.com/Jothin-kumar/time-widget
"""
import tkinter as tk

left_top = 'left-top'
right_bottom = 'right-bottom'


def get_location_on_screen():
    with open('location_on_screen.txt') as loc:
        return loc.read().strip('\n')


def set_location_on_scren(location):
    with open('location_on_screen.txt', 'w') as loc:
        loc.write(location)


class MinWidget:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.resizable(False, False)
        self.time_viewer = tk.Label(master=self.root, text='', font=("Arial", 25))
        self.timezone_viewer = tk.Label(master=self.root, text='', font=("Arial", 15))
        self.time_viewer.pack()
        self.timezone_viewer.pack()
        self.mainloop = self.root.mainloop
        self.destroy = self.root.destroy

        def on_middle_button(event):
            location_on_screen = get_location_on_screen()
            if location_on_screen == left_top:
                set_location_on_scren(right_bottom)
            elif location_on_screen == right_bottom:
                set_location_on_scren(left_top)
            self.refresh_size_and_location()

        self.root.bind('<Button-2>', on_middle_button)
        self.refresh_size_and_location()

    def refresh_size_and_location(self):
        location_on_screen = get_location_on_screen()
        self.root.update()
        if location_on_screen == left_top:
            self.root.geometry('+0+0')
        elif location_on_screen == right_bottom:
            w = int(self.root.winfo_geometry().split('+')[0].split('x')[0])
            h = int(self.root.winfo_geometry().split('+')[0].split('x')[1])
            self.root.geometry(
                '+' + str(self.root.winfo_screenwidth() - w) + '+' + str(self.root.winfo_screenheight() - h)
            )

    def set_time(self, time: str):
        self.time_viewer['text'] = time
        self.refresh_size_and_location()

    def set_timezone(self, timezone: str):
        self.timezone_viewer['text'] = timezone
        self.refresh_size_and_location()

    def configure_switch_to_max(self, command):
        self.root.bind('<Button-3>', command)


class MaxWidget:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.resizable(False, False)
        self.time_viewer = tk.Label(master=self.root, text='', font=("Arial", 25))
        self.mainloop = self.root.mainloop
        self.destroy = self.root.destroy
        self.countries_list_box = tk.Listbox(master=self.root, height=25)
        self.time_zone_listbox = tk.Listbox(master=self.root, height=25)
        self.countries_list_box.grid(row=1, column=0)
        self.time_zone_listbox.grid(row=1, column=1)
        self.time_viewer.grid(row=0, column=0)

        def on_middle_button(event):
            location_on_screen = get_location_on_screen()
            if location_on_screen == left_top:
                set_location_on_scren(right_bottom)
            elif location_on_screen == right_bottom:
                set_location_on_scren(left_top)
            self.refresh_size_and_location()

        self.root.bind('<Button-2>', on_middle_button)
        self.refresh_size_and_location()

    def refresh_size_and_location(self):
        location_on_screen = get_location_on_screen()
        self.root.update()
        if location_on_screen == left_top:
            self.root.geometry('+0+0')

            def to_right_bottom():
                set_location_on_scren(right_bottom)

        elif location_on_screen == right_bottom:
            w = int(self.root.winfo_geometry().split('+')[0].split('x')[0])
            h = int(self.root.winfo_geometry().split('+')[0].split('x')[1])
            self.root.geometry(
                '+' + str(self.root.winfo_screenwidth() - w) + '+' + str(self.root.winfo_screenheight() - h)
            )

            def to_left_top():
                set_location_on_scren(left_top)

    def set_countries(self, countries: list):
        self.countries_list_box.delete(0, tk.END)
        for country in countries:
            self.countries_list_box.insert(tk.END, f'{country.full_name} - {country.iso3166_code}')
        self.refresh_size_and_location()

    def set_timezones(self, timezones: list):
        self.time_zone_listbox.delete(0, tk.END)
        for timezone in timezones:
            self.time_zone_listbox.insert(tk.END, timezone)
        self.refresh_size_and_location()

    def set_on_country_select(self, command):
        def onselect(evt):
            try:
                w = evt.widget
                index = int(w.curselection()[0])
                value = w.get(index)
                command(value[-2:])
            except:
                pass

        self.countries_list_box.bind('<<ListboxSelect>>', onselect)

    def set_on_timezone_select(self, command):
        def onselect(evt):
            try:
                w = evt.widget
                index = int(w.curselection()[0])
                value = w.get(index)
                command(value)
            except:
                pass

        self.time_zone_listbox.bind('<<ListboxSelect>>', onselect)

    def set_time(self, time: str):
        self.time_viewer['text'] = time
        self.refresh_size_and_location()

    def configure_switch_to_min(self, command):
        self.root.bind('<Button-3>', command)
