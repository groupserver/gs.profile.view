# -*- coding: utf-8 -*-
from zope.component import createObject
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from Products.CustomUserFolder.interfaces import IGSUserInfo
from interfaces import *
from zope.app.publisher.browser.menu import getMenu
from AccessControl.security import newInteraction
from gs.viewlet import SiteContentProvider

import logging
log = logging.getLogger('GSProfileContextMenuContentProvider')


class GSProfileContextMenuContentProvider(SiteContentProvider):
    """GroupServer context-menu for the user profile area.
    """

    def __init__(self, context, request, view):
        super(GSProfileContextMenuContentProvider, self).__init__(context,
                                                                request, view)
        self.__updated = False

        newInteraction()

    def update(self):
        self.__updated = True

        self.groupsInfo = createObject('groupserver.GroupsInfo',
          self.context)
        self.userInfo = IGSUserInfo(self.context)

        self.pages = getMenu('user_profile_menu', self.context, self.request)

        self.requestBase = self.request.URL.split('/')[-1]
        self.userId = self.context.getId()

    def render(self):
        if not self.__updated:
            raise interfaces.UpdateNotCalled

        pageTemplate = PageTemplateFile(self.pageTemplateFileName)
        return pageTemplate(view=self)

    #########################################
    # Non standard methods below this point #
    #########################################

    def page_class(self, page):
        if page['selected']:
            retval = 'current'
        else:
            retval = 'not-current'
        assert retval
        return retval
