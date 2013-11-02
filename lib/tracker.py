# -*- coding: utf-8 -*-

from ConfigParser import RawConfigParser
from singleton import *
from os.path import expanduser

@Singleton
class Tracker:
    "Provides a unique access point to the configuration file"

    MAX = 5
    CONFIG_FILE = '%s/.noch_less.cnf' % expanduser('~')

    def __init__(self):
        """
        Instance variables: config
        """

        try:
            self.config = RawConfigParser()
            self.config.read(self.CONFIG_FILE)
            self.remove_excess()
        except:
            pass

    def add(self, less_file):
        if self.count() >= self.MAX:
            return "You can't add more than %s files." % self.MAX

        if self.config.has_section(less_file.id):
            return "The file %s is already being tracked." % less_file.id

        self.config.add_section(less_file.id)
        self.config.set(less_file.id, 'source', less_file.source)
        self.config.set(less_file.id, 'destination', less_file.destination)
        self.save()
        return True

    def modify(self, less_file):
        self.config.set(less_file.id, 'destination', less_file.destination)
        self.save()

    def remove(self, less_file):
        self.config.remove_section(less_file.id)
        self.save()

    def remove_excess(self):
        if self.count() >= self.MAX:
            count = 0
            for section in self.config.sections():
                count += 1
                if count > self.MAX:
                    self.config.remove_section(section)
            self.save()

    def all(self):
        all_sections = []
        for section in self.config.sections():
            lessie = {'id': section}
            lessie['source'] = self.config.get(section, 'source')
            lessie['destination'] = self.config.get(section, 'destination')
            all_sections.append(lessie)
        return all_sections

    def save(self):
        with open(self.CONFIG_FILE, 'wb') as file:
            self.config.write(file)

    def count(self):
        return len(self.config.sections())
