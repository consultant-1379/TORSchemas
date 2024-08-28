from core.litp_item import LitpItem

from core.litp_defaults import create_str_property
from core.litp_defaults import create_enum_property

import logging
logger = logging.getLogger('litp.LitpServiceDef')


class LitpServiceDependencyDef(LitpItem):
    def __init__(self):
        super(LitpServiceDependencyDef, self).__init__()

    def allowed_properties(self):
        ap = dict()
        ap['name'] = {'help': 'This is the name of the service referenced in this dependency. ',
                      'type': 'str', 'regexp': '^[\w\-\._/]+$',
                      'optional': False}
        ap['min-version'] = create_str_property("version_string", dict(
            help='The minimum version of the service required to satisfy the dependency'))
        ap['scope'] = create_enum_property(['container', 'host', 'cluster'],
                dict(help="The scope in which this dependency must be satisfied, if required."))
        ap['dependency-type'] = create_enum_property(['positive', 'negative'], dict(optional=False,
                help='A positive dependency indicates that this component must be present in the defined scope. ' +
                    'A negative dependency indicates that this component must not be present in the defined scope.'))
        return ap

    def allowed_children(self):
        return None
