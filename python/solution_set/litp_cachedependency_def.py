from core.litp_item import LitpItem

from core.litp_defaults import create_str_property
from core.litp_defaults import create_enum_property

import logging
logger = logging.getLogger('litp.LitpCacheDef')


class LitpCacheDependencyDef(LitpItem):
    def __init__(self):
        super(LitpCacheDependencyDef, self).__init__()

    def allowed_properties(self):
        '''
        Not sure if there are further properties associated with a cache
        but there are likely to be so we define a separate type.
        '''
        ap = dict()
        ap['name'] = {'help': 'This is the component name referenced. ',
                      'type': 'str', 'regexp': '^[\w\-\._/]+$',
                      'optional': False}
        return ap

    def allowed_children(self):
        return None
