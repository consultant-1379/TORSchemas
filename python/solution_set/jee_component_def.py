
from jee.jee_container_def import JEEContainerDef
from core.litp_roledef import LitpRoleDef


class JEEComponentDef(LitpRoleDef):
    def _get_type(self):
        return "solution_set.jee_component.JEEComponent"

    def allowed_children(self):
        return ('^core.litp_(roledef.LitpRoleDef|resourcedef.LitpResourceDef' +
                '|servicedef.LitpServiceDef|solutiondef.LitpSolutionDef)$')
