
from core.litp_resource import LitpResource
from core.litp_defaults import create_str_property

import logging
logger = logging.getLogger("litp.jee")


class JEEService(LitpResource):
    def allowed_properties(self):
        ap = dict()
        ap['pre-deploy'] = create_str_property("basic_string",
                dict(regexp="/[/0-9a-zA-Z_\-]+", optional=False,
                    help='Absolute path to the container-predeploy.cli file'
                ))
        return ap

    def get_jee_component(self):
        return self._lookup_parents(types="solution_set.jee_component.JEEComponent")

    def get_jee_component_cli_port(self):
        jee_component = self.get_jee_component()
        return str(9990 + int(jee_component.get_portOffset()))

    def _configure(self, parameters={}):
        try:
            jee_component = self.get_jee_component()          
            self.configuration = []
            
            #YES!! user and password are hardcoded here. This must be fixed!!              
            command = "/opt/{0}/{0}/bin/jboss-cli.sh --controller={1}:{2} " \
                "--connect --user=root --password=shroot --file={3}".format(
                   jee_component.get_instance_name(),
                   jee_component.get_ip_address(),
                   self.get_jee_component_cli_port(),
                   self.get_prop('pre-deploy'))
            exec_config = {
                'type': 'exec',
                'id': command,
                'values': dict(),
            }
            self.configuration.append(exec_config)

            return {'success': 'JEE Service configured successfully'}
        except Exception as e:
            logger.exception("Exception in jee config configure")
            return {'error':
                'JEE service failed to create JBoss CLI command ',
                'message': str(e)}


