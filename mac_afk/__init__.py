#!/usr/bin/env python
# -*- coding: utf-8 -*-
import public
import runcmd


@public.add
def seconds():
    return int(runcmd.run(["afk"])._raise().out)
