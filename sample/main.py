import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import sqlite3
import os

working_directory = os.path.abspath(os.path.dirname(__file__))
gui_file_path = os.path.join(working_directory, "sample.glade")


class Handler:
    def on_click_search_button(self, *args):
        print("Welcome to Linux Playa")

builder = Gtk.Builder()
builder.add_from_file(gui_file_path)
builder.connect_signals(Handler())

def main():
    global builder

    win = builder.get_object("SampleWindow")
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
