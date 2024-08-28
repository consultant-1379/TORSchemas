from core.litp_roledef import LitpRoleDef

from core.litp_defaults import create_str_property
from core.litp_defaults import create_enum_property

class LitpSolutionSet(LitpRoleDef):
    def __init__(self):
        super(LitpSolutionSet, self).__init__()

    def allowed_properties(self):
        ap = dict()
        ap['name'] = create_str_property("basic_string", dict(
            help="The name of this solution set.",
            regexp="[0-9a-zA-Z]+", optional=False)
        )
        ap['description'] = create_str_property("basic_string", dict(
            help="A brief description of this solution set",
            optional=False)
        )
        ap['version'] = create_str_property("version_string", dict(
            help="The version of the solution set",
            optional=False)
        )
        ap['type'] = create_enum_property(['BASIC', 'COMMERCIAL'], dict (
            help="The type of solution set. A basic solution set is one that is required to enable\n " +
            "basic functionality of the TOR platform. A commercial solution set is one which provides\n " +
            "a solution of direct benefit to a customer",
            optional=False))
        return ap


    def allowed_children(self):
        return '(solution_set.litp_component.LitpComponent)|' +\
            '(solution_set.litp_componentdefinition.LitpComponentDefinition)'
