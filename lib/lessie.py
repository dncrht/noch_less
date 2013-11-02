# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
from tracker import *
from absolute_path import absolute_path
from subprocess import Popen

class Lessie(gtk.VBox):
    "Custom widget to represent each of the files tracked"

    def delete_me(self, widget, data = None):
        "Callback on deleting the file from the list"
        self.terminate_compiler_subprocess()
        self.tracker.remove(self.less_file)
        self.destroy()

    def change_destination(self, widget, data = None):
        "Callback on changing destination"
        label = gtk.Label('Enter new path')
        dialog = gtk.Dialog(
            'Change destination',
            self.parent_window,
            gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
            (gtk.STOCK_OK, gtk.RESPONSE_ACCEPT, gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT)
        )
        dialog.set_border_width(10)
        dialog.vbox.add(label)
        dialog.vbox.set_spacing(10)
        destination = self.__label_destination.get_text()
        entry = gtk.Entry()
        entry.set_text(destination)
        #entry.select_region(6, len(destination))
        dialog.vbox.add(entry)
        dialog.show_all()
        response = dialog.run() # http://stackoverflow.com/questions/4657344/how-to-repeatedly-show-a-dialog-with-pygtk-gtkbuilder
        if response == gtk.RESPONSE_ACCEPT:
            self.__change_destination_label_and_file(entry.get_text())

        dialog.destroy()

    def force_compilation(self, widget, data = None):
        "Callback on force compilation"
        self.__fork_compiler_subprocess()

    def __init__(self, parent_window, less_file):
        """
        Public instance variables: tracker, less_file, parent_window, compiler_subprocess
        """

        super(Lessie, self).__init__()
        self.set_spacing(10)

        self.parent_window = parent_window
        self.less_file = less_file

        self.compiler_subprocess = None
        self.__fork_compiler_subprocess()

        self.tracker = Tracker.Instance()

        fixed = gtk.Fixed()
        label = gtk.Label("<b>%s</b>" % less_file.id)
        label.set_use_markup(True)
        fixed.put(label, 0, 0)
        label = gtk.Label(less_file.source)
        fixed.put(label, 0, 25)

        image = gtk.Image()
        image.set_from_file(absolute_path('assets/remove.png'))
        image.set_tooltip_text('Remove')
        event_box = gtk.EventBox()
        event_box.add(image)
        #event_box.window.set_cursor(gtk.gdk.Cursor(gtk.gdk.HAND1))
        event_box.connect('button_press_event', self.delete_me)
        fixed.put(event_box, 364, 0)

        hbox = gtk.HBox(False, 0)
        hbox.set_spacing(10)
        self.__label_destination = gtk.Label(less_file.destination)
        hbox.add(self.__label_destination)
        image = gtk.Image()
        image.set_from_file(absolute_path('assets/refresh.png'))
        image.set_tooltip_text('Refresh')
        event_box = gtk.EventBox()
        event_box.add(image)
        event_box.connect('button_press_event', self.force_compilation)
        hbox.add(event_box)
        image = gtk.Image()
        image.set_from_file(absolute_path('assets/change.png'))
        image.set_tooltip_text('Change destination')
        event_box = gtk.EventBox()
        event_box.add(image)
        event_box.connect('button_press_event', self.change_destination)
        hbox.add(event_box)
        fixed.put(hbox, 0, 50)

        self.add(fixed)
        self.add(gtk.HSeparator())
        self.show_all()

    def __change_destination_label_and_file(self, destination):
        # we have to avoid that destination is compiled into source dir
        # because that would trigger compilation again
        if self.less_file.source.split('/')[0:-1] == destination.split('/')[0:-1]:
            return

        # all clear: change label and recompile
        self.__label_destination.set_text(destination)
        self.less_file.destination = destination
        self.tracker.modify(self.less_file)
        self.__fork_compiler_subprocess()

    def terminate_compiler_subprocess(self):
        if self.compiler_subprocess: # terminate only if already exists
            self.compiler_subprocess.terminate()

    def __fork_compiler_subprocess(self):
        self.terminate_compiler_subprocess()
        self.compiler_subprocess = Popen([absolute_path('compiler_subprocess.sh'), absolute_path('lessphp/plessc'), self.less_file.source, self.less_file.destination])
