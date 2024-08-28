from core.litp_item import LitpItem
from core.litp_roledef import LitpRoleDef

from core.litp_defaults import create_str_property
from core.litp_defaults import create_enum_property

import logging
logger = logging.getLogger('litp.LitpFileSystemRef')


class LitpFileSystemDef(LitpItem):
    def __init__(self):
        super(LitpFileSystemDef, self).__init__()

    def allowed_properties(self):
        ap = dict()
        ap['mountpoint'] = create_str_property("basic_string",
                dict(regexp="/[/0-9a-zA-Z_\-]+", optional=False,
                    help='The name of the place in the filesystem this filesystem must be mounted at.'
                ))
        ap['devicetype'] = create_enum_property(['LOCAL', 'NAS', 'SAN', 'DAS'],
                dict(optional=False,
                    help='The type of filesystem required.'))
        ap['minimumsize'] = create_str_property("basic_string",
                dict(regexp="[0-9]+[K|MG|T|P]?", optional=False,
                    help='The minimum size of the filesystem required by this component. Future versions ' +
                    'of this element will also define growth factors. If the filesystem is defined by more than one component ' +
                    'the total space required will be aggregated and the actual filesystem created with the total space calculation'))
        ap['multiplicationfactor'] = create_str_property("basic_string", dict(help="To be decided what this looks like"))
        return ap

    def allowed_children(self):
        return None
