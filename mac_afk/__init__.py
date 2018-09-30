#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public import public
import runcmd

@public
def seconds():
    return int(runcmd.run(["afk"])._raise().out)
