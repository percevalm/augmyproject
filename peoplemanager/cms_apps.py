from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register # register the application
class PeoplemanagerApphook(CMSApp):
    app_name = "peoplemanager"
    name = "People Application"
    def get_urls(self, page=None, language=None, **kwargs):
        return ["peoplemanager.urls"]
