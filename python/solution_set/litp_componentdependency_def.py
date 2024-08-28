from core.litp_item import LitpItem

from core.litp_defaults import create_str_property
from core.litp_defaults import create_enum_property

import logging
logger = logging.getLogger('litp.LitpComponentDependencyDef')


class LitpComponentDependencyDef(LitpItem):
    def __init__(self):
        super(LitpComponentDependencyDef, self).__init__()

    def allowed_properties(self):
        ap = dict()
        ap['name'] = {'help': 'This is the name of the component referenced in this dependency.',
                      'type': 'str', 'regexp': '^[\w\-\._/]+$',
                      'optional': False}
        ap['min-version'] = create_str_property("version_string",
                dict(optional=False, help="The minimum version of this component that must be present"))
        ap['scope'] = create_enum_property(['container', 'host', 'cluster'], dict(optional=False,
            help='The scope in which the dependency must be resolved (container, host or cluster)'))
        ap['dependency-type'] = create_enum_property(['positive', 'negative'], dict(optional=False,
            help='A positive dependency indicates that this component must be present in the defined scope. ' +
                'A negative dependency indicates that this component must not be present in the defined scope.'))
        return ap

    def allowed_children(self):
        return None
