from core.litp_roledef import LitpRoleDef

from core.litp_defaults import create_str_property
from core.litp_defaults import create_enum_property

import logging
logger = logging.getLogger('litp.LitpComponent')


class LitpComponent(LitpRoleDef):
    '''
    This class defines just the name and version of a component, so that the type can
    be used in both the solution set definition and in the component defintinio without needing
    to include the entire component definition in the solution set definition.
    '''
    def __init__(self):
        super(LitpComponent, self).__init__()

    def allowed_properties(self):
        ap = dict()
        ap['name'] = {'help': 'The name of the component referenced by this component definition.',
                      'type': 'str', 'regexp': '^[\w\-\._/]+$',
                      'optional': False}
        ap['version'] = create_str_property("version_string", dict(optional=False))
        return ap

    def allowed_children(self):
        return None
