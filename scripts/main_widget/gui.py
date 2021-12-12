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


root = tk.Tk()
mainframe = tk.Canvas(master=root)
root.overrideredirect(True)
root.attributes('-topmost', True)
location_on_screen = get_location_on_screen()
if location_on_screen == left_top:
    root.geometry('200x50+0+0')
elif location_on_screen == right_bottom:
    root.geometry('200x50+' + str(root.winfo_screenwidth() - 200) + '+' + str(root.winfo_screenheight() - 50))
countries_list_box = tk.Listbox(master=mainframe, height=25)


def set_on_country_select(command):
    def onselect(evt):
        try:
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            command(value[-2:])
        except:
            pass

    countries_list_box.bind('<<ListboxSelect>>', onselect)


time_zone_listbox = tk.Listbox(master=mainframe, height=25)


def set_on_timezone_select(command):
    def onselect(evt):
        try:
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            command(value)
        except:
            pass

    time_zone_listbox.bind('<<ListboxSelect>>', onselect)


time_viewer = tk.Label(master=mainframe, text='', font=("Arial", 25))
change_loc_button = tk.Button(master=mainframe)


def set_time(time: str):
    time_viewer['text'] = time


def set_loc_left_top():
    set_location_on_scren(left_top)
    root.geometry('200x50+0+0')
    change_loc_button['text'] = 'Switch to right bottom'
    change_loc_button['command'] = set_loc_right_bottom
    change_loc_button.grid_forget()
    change_loc_button.grid(row=0, column=1)


def set_loc_right_bottom():
    set_location_on_scren(right_bottom)
    root.geometry('200x50+' + str(root.winfo_screenwidth() - 200) + '+' + str(root.winfo_screenheight() - 50))
    change_loc_button['text'] = 'Switch to left top'
    change_loc_button['command'] = set_loc_left_top
    change_loc_button.grid_forget()
    change_loc_button.grid(row=0, column=1)


if location_on_screen == left_top:
    set_loc_left_top()
elif location_on_screen == right_bottom:
    set_loc_right_bottom()
countries_list_box.grid(row=1, column=0)
time_zone_listbox.grid(row=1, column=1)
time_viewer.grid(row=0, column=0)
change_loc_button.grid(row=0, column=1)


def on_enter(event):
    location_on_screen = get_location_on_screen()
    if location_on_screen == left_top:
        root.geometry('350x500+0+0')
    elif location_on_screen == right_bottom:
        root.geometry(f'350x500+' + str(root.winfo_screenwidth() - 350) + '+' + str(root.winfo_screenheight() - 500))


def on_leave(event):
    location_on_screen = get_location_on_screen()
    if location_on_screen == left_top:
        root.geometry('200x50+0+0')
    elif location_on_screen == right_bottom:
        root.geometry('200x50+' + str(root.winfo_screenwidth() - 200) + '+' + str(root.winfo_screenheight() - 50))


mainframe.bind('<Enter>', on_enter)
mainframe.bind('<Leave>', on_leave)
mainframe.pack(fill=tk.BOTH)
mainloop = root.mainloop
