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
from gs.viewlet.viewlet import SiteViewlet
from zope.cachedescriptors.property import Lazy
from zope.component import createObject

# I know the base-class may seem strange, but bare with me. This viewlet
#   is shown on the site homepage. It is not shown in the context of
#   a profile. Because of this we use the generic (ish) SiteViewlet
#   rather than gs.profile.base.viewlet.Viewlet


class SiteHomeSummaryViewlet(SiteViewlet):
    @property
    def show(self):
        retval = not(self.loggedInUser.anonymous)
        return retval

    @Lazy
    def userInfo(self):
        return self.loggedInUser

    @Lazy
    def salutation(self):
        retval = self.context.DivisionConfiguration.get(b'greeting',
                                                        'Welcome')
        return retval

    @Lazy
    def groups(self):
        retval = createObject('groupserver.GroupsInfo', self.context)
        return retval

    @Lazy
    def memberGroups(self):
        u = self.userInfo.user
        mg = self.groups.get_member_groups_for_user(u, u)
        retval = [createObject('groupserver.GroupInfo', g) for g in mg]
        return retval
