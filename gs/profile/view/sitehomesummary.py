# coding=utf-8
from gs.viewlet.viewlet import SiteViewlet
from zope.cachedescriptors.property import Lazy

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

