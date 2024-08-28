
from core.litp_resourcedef import LitpResourceDef


class JEEServiceDef(LitpResourceDef):
    def _get_type(self):
        return "solution_set.jee_service.JEEService"


