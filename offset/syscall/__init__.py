# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.


import sys

from . import proxy

# patch the os module
os = proxy.OsProxy()
sys.modules['offset.syscall.os'] = os

# patch the select module
select = proxy.SelectProxy()
sys.modules['select.syscall.select'] = select
