#!/usr/bin/env python
# -*- Mode: Python; tab-width: 4 -*-
#
# Fix for setuploader
#
# Copyright (C) 2004 Sherpya <sherpya@netfarm.it>
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
# ======================================================================

from sys import argv, exit

if len(argv) < 2:
    print 'Usage: fixloader.py ntldr'
    exit()

data = open(argv[1], 'rb').read()

if data.find('setupldr.exe')==-1:
    print 'Wrong file'
    exit()

if data[:2] == 'MZ':
    print 'Loader already fixed'
    exit()

data = 'MZ' + data.split('MZ', 1).pop()

open(argv[1], 'wb').write(data)
print 'Loader fixed'