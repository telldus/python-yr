#!/usr/bin/env python2

import yr.libyr
print('/home/pm/.local/lib/python3.4/site-packages/yr/libyr.py') # ~> is wrong!
print('/usr/local/lib/python3.4/dist-packages/yr/libyr.py') # ~> is ok!
print(yr.libyr.__file__)
