
from core.litp_resourcedef import LitpResourceDef


class JEEConfigDef(LitpResourceDef):
    def _get_type(self):
        return "solution_set.jee_config.JEEConfig"
