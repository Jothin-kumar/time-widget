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
import tkinter as tk

root = tk.Tk()
mainframe = tk.Frame(master=root)
root.overrideredirect(True)
root.attributes('-topmost', True)
root.geometry('175x50+0+0')
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


def set_time(time: str):
    time_viewer['text'] = time


countries_list_box.grid(row=1, column=0)
time_zone_listbox.grid(row=1, column=1)
time_viewer.grid(row=0, column=0)


def on_enter(event):
    root.geometry('350x500+0+0')


def on_leave(event):
    root.geometry('175x50+0+0')


mainframe.bind('<Enter>', on_enter)
mainframe.bind('<Leave>', on_leave)
mainframe.pack(fill=tk.BOTH)
mainloop = root.mainloop
