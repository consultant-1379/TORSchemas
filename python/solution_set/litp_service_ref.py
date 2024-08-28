from core.litp_item import LitpItem
from core.litp_roledef import LitpRoleDef

from core.litp_defaults import create_str_property

import logging
logger = logging.getLogger('litp.LitpServiceRef')


class LitpServiceRef(LitpItem):
    def __init__(self):
        super(LitpServiceRef, self).__init__()

    def allowed_properties(self):
        ap = dict()
        ap['name'] = {'help': 'This is the Service name referenced. ',
                      'type': 'str', 'regexp': '^[\w\-\._/]+$',
                      'optional': False}
        ap['version'] = create_str_property("version_string")
        return ap

    def allowed_children(self):
        return None
