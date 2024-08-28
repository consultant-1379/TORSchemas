from core.litp_item import LitpItem
from core.litp_roledef import LitpRoleDef

from core.litp_defaults import create_str_property
from core.litp_defaults import create_enum_property

import logging
logger = logging.getLogger('litp.LitpFileSystemRef')


class LitpPosixUserDef(LitpItem):
    def __init__(self):
        super(LitpPosixUserDef, self).__init__()

    def allowed_properties(self):
        ap = dict()
        ap['name'] = {'help': 'POSIX User Account Name',
                      'type': 'str',
                      'optional': False,
                      'regexp': '^[A-Za-z0-9_][A-Za-z0-9_-]{0,31}$'}
        ap['groups'] = {'help': 'POSIX User Account Group ' +
                                'memberships (comma separated)',
                        'type': 'str',
                        'optional': True,
                        'regexp': '^([A-Za-z0-9_][A-Za-z0-9_-]{0,30}' +
                                  '([A-Za-z0-9_-]?))' +
                                  '(,([A-Za-z0-9_][A-Za-z0-9_-]{0,30}' +
                                  '([A-Za-z0-9_-]?)))*$'}
        ap['seluser'] = {'help': 'SELinux user type',
                         'type': 'str',
                         'optional': True,
                         'regexp': '^[a-zA-Z_]+$'}

        return ap

    def allowed_children(self):
        return None
