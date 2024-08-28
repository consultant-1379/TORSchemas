
from core.litp_resource import LitpResource
from core.litp_defaults import create_str_property

import logging
logger = logging.getLogger("litp.jee")


class JEEConfig(LitpResource):
    def allowed_properties(self):
        logger.info("JEEConfig : called allowed_properties ...")
        ap = dict()
        ap['messaging.group.address'] = create_str_property("basic_string",
                dict(optional=True,help='jboss.messaging.group.address'))
        ap['messaging.group.port'] = create_str_property("basic_string",
                dict(optional=True,help='jboss.messaging.group.port'))
        ap['jgroups.bind_addr'] = create_str_property("basic_string",
                dict(optional=True,help='jgroups.bind_addr'))
        ap['jgroups.udp.mcast_addr'] = create_str_property("basic_string",
                dict(optional=True,help='jgroups.udp.mcast_addr'))
        ap['jgroups.udp.mcast_port'] = create_str_property("basic_string",
                dict(optional=True,help='jgroups.udp.mcast_port'))
        ap['jgroups.mping.mcast_addr'] = create_str_property("basic_string",
                dict(optional=True,help='jgroups.mping.mcast_addr'))
        ap['jgroups.mping.mcast_port'] = create_str_property("basic_string",
                dict(optional=True,help='jgroups.mping.mcast_port'))
        return ap                
    
    def get_jee_component(self):
        return self._lookup_parents(types="solution_set.jee_component.JEEComponent")
    
    def _configure(self, parameters={}):
        try:
            jee_component = self.get_jee_component()
            instanceName = jee_component.get_instance_name()
            
            self.configuration = []
            target_file = '/opt/{0}/{0}/bin/{0}.conf'.format(instanceName)
            values = {
                'content': "jboss.messaging.group.address={0}\njboss.messaging.group.port={1}\njgroups.bind_addr={2}\n" \
                "jgroups.udp.mcast_addr={3}\njgroups.udp.mcast_port={4}\n" \
                "jgroups.mping.mcast_addr={5}\njgroups.mping.mcast_port={6}\n" \
                "jboss.bind.address.management={7}".format(
                       self.get_prop('messaging.group.address'),
                       self.get_prop('messaging.group.port'),
                       self.get_prop('jgroups.bind_addr'),
                       self.get_prop('jgroups.udp.mcast_addr'),
                       self.get_prop('jgroups.udp.mcast_port'),
                       self.get_prop('jgroups.mping.mcast_addr'),
                       self.get_prop('jgroups.mping.mcast_port'),
                       jee_component.get_ip_address())
                      
            }
            file_config = {'type': 'file',
                'id': target_file,
                'values': values
            }
            self.configuration.append(file_config)
            return {'success': 'JEE container configured successfully'}
        except Exception as e:
            logger.exception("Exception in JEEConfig configure")
            return {'error':
                'JEEConfig failed to create properties file',
                'message': str(e)}


