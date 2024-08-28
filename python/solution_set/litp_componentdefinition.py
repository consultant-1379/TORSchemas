from core.litp_roledef import LitpRoleDef

from core.litp_defaults import create_str_property
from core.litp_defaults import create_enum_property

import logging
logger = logging.getLogger('litp.LitpComponentDefinition')


class LitpComponentDefinition(LitpRoleDef):
    def __init__(self):
        super(LitpComponentDefinition, self).__init__()

    def allowed_properties(self):
        ap = dict()
        ap['availabilitymodel'] = create_enum_property(['SINGLETON',
            'NWAY-ACTIVE', 'ACTIVE-PASSIVE'],
            dict(optional=False, help='The Core Middleware availability model'))
        ap['description'] = create_str_property("basic_string", dict(
            help="A brief description of this solution set",
            optional=False)
        )
        return ap

    def allowed_children(self):
        return "(solution_set.litp_component.LitpComponent)|" +\
            "(solution_set.litp_componentdependency_def.LitpComponentDependencyDef)|" + \
            "(solution_set.litp_cachedependency_def.LitpCacheDependencyDef)|" + \
            "(solution_set.litp_service_ref.LitpServiceRef)|" + \
            "(solution_set.litp_servicedependency_def.LitpServiceDependencyDef)|" + \
            "(solution_set.litp_filesystem_def.LitpFileSystemDef)|" + \
            "(solution_set.litp_posixuser_def.LitpPosixUserDef)"
