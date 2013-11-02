#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
from lib.tracker import *
from lib.lessie import *
from lib.less_file import *
from lib.absolute_path import absolute_path
from subprocess import Popen

class NochLess(gtk.Window):

    def destroy(self, widget, data = None):
        for lessie in self.vbox.get_children():
            lessie.terminate_compiler_subprocess()
        Popen(['killall', 'inotifywait'])
        gtk.main_quit()
      
    def new_file(self, widget, context, x, y, data, info, time):
        "Callback when a new file is dropped in the app window"
        context.finish(True, False, time) # http://www.pygtk.org/docs/pygtk/class-gdkdragcontext.html

        less_file = LessFile(data.get_text())

        result = self.tracker.add(less_file)
        if result == True:
            self.vbox.add(Lessie(self, less_file))
        else:
            dialog = gtk.MessageDialog(
                self,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_ERROR,
                gtk.BUTTONS_CLOSE,
                result
            )
            dialog.run()
            dialog.destroy()

    def __init__(self):
        """
        Instance variables: vbox, tracker
        """

        super(NochLess, self).__init__()
        self.set_border_width(10)
        self.set_title('Noch Less')
        self.set_size_request(400, 600)

        fixed = gtk.Fixed()
        self.add(fixed)

        self.vbox = gtk.VBox(False, 0)
        self.vbox.set_spacing(10)
        fixed.add(self.vbox)

    	self.tracker = Tracker.Instance()
    	for lessie in self.tracker.all():
            less_file = LessFile(id = lessie['id'], source = lessie['source'], destination = lessie['destination'])
            self.vbox.add(Lessie(self, less_file))

        self.connect('destroy', self.destroy)

        drop = gtk.Image()
        drop.set_from_file(absolute_path('assets/drop.png'))
        fixed.put(drop, 176, 500)

        fixed.put(gtk.Label('Add files just by dropping them here!'), 78, 555)

        self.drag_dest_set(gtk.DEST_DEFAULT_MOTION | gtk.DEST_DEFAULT_HIGHLIGHT | gtk.DEST_DEFAULT_DROP, [('text/plain', 0, 0)], gtk.gdk.ACTION_COPY)
        self.connect('drag_data_received', self.new_file)

        # done view layout
        self.show_all()
        self.set_resizable(False)
        self.set_icon_from_file(absolute_path('assets/lessie.png'))

    def start(self):
        gtk.main()

if __name__ == '__main__':
    app = NochLess()
    app.start()
