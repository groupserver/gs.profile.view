# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import unicode_literals


def groupInfoSorter(a, b):
    # TODO: Move to Group Membership
    assert hasattr(a, 'name')
    assert hasattr(b, 'name')

    aname = a.name.lower()
    bname = b.name.lower()
    if (aname < bname):
        retval = -1
    elif (aname == bname):
        retval = 0
    else:  # aname > bname
        retval = 1

    assert retval in (-1, 0, 1)
    return retval
