# -*- coding: utf-8 -*-

import os
import sys

BASE_PATH = '/'.join(os.path.abspath(sys.argv[0]).split('/')[0:-1])

def absolute_path(relative_path):
    return '%s/%s' % (BASE_PATH, relative_path)
