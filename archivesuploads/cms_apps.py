from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ArchivesuploadsApp(CMSApp):
    name = _("Publication App")
    urls = ["archivesuploads.urls"]
    app_name = "archivesuploads"

apphook_pool.register(ArchivesuploadsApp)
