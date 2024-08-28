
from jee.jee_container import JEEContainer
from core.litp_defaults import create_str_property

class JEEComponent(JEEContainer):
    def __init__(self, params=None):
        """
        Constructor
        """
        super(JEEComponent, self).__init__()

    def allowed_properties(self):
        """
        List of allowed properties.
        @return: Descriptions of allowed properties with help, type and
        validation regexp
        """
        ap = super(JEEComponent, self).allowed_properties()
        ap['instance-name'] = create_str_property("basic_name_string",
            dict(help="Unique name of instance", optional=False))
        ap['port-offset'] = create_str_property("basic_name_string",
            dict(help="Used for multiple instances on different ports",
                default="0"))
        ap['process-user'] = create_str_property("basic_name_string",
            dict(help="Optional install user"))
        ap['process-group'] = create_str_property("basic_name_string",
            dict(help="Optional install group"))
        ap['Xms'] = create_str_property("basic_name_string",
            dict(help="Xms : default is 1024M",
                default="1024M"))
        ap['Xmx'] = create_str_property("basic_name_string",
            dict(help="Xmx : default is 1024M",
                default="1024M"))
        ap['MaxPermSize'] = create_str_property("basic_name_string",
            dict(help="MaxPermSize : default is 256M",
                default="256M"))
        
        return ap

    def _get_install_destination(self):
        return "/opt/%s" % (self.get_prop('instance-name'),)
    
    def _get_java_opts(self):
        instanceName = self.get_prop('instance-name')
        properties_file = '/opt/{0}/{0}/bin/{0}.conf'.format(instanceName)
        r = " -DXms=%s" % (self.get_prop('Xms'))
        r += " -DXmx=%s" % (self.get_prop('Xmx'))
        r += " -DXX:MaxPermSize=%s" % (self.get_prop('MaxPermSize'))
        r += " -Dcom.ericsson.oss.sdk.node.identifier=%s" % (instanceName)
        if self.get_prop('port-offset'):
            r += " -Djboss.socket.binding.port-offset=%s" % (
                 self.get_prop('port-offset'),)
        r += " -Djboss.node.name=%s" % (instanceName)
        r += " --properties=%s" % (properties_file)
        return r
    
    def _get_process_user(self):
        return self.get_prop('process-user') or self.get_prop('instance-name')

    def _get_process_group(self):
        return self.get_prop('process-group') or self.get_prop('instance-name')
    
    def get_portOffset(self):
        return self.get_prop('port-offset')
    
    def get_parent_node(self):
        return self._lookup_parents(types="core.litp_node.LitpNode")
    
    def get_ip_address(self):
        parent = self.get_parent_node()
        return parent.get_ip_address()
    
    def get_instance_name(self):
        return self.get_prop('instance-name')

    def _configure(self, parameters={}):
        '''
        Configure JEEContainer
        This generates a puppet manifest to install and configure
        jboss instance
        '''
        parentNode = self.get_parent_node()
        try:
            values = {
                'service':              self.get_prop('instance-name'),
                'install_destination':  self._get_install_destination(),
                'bindaddr':             self.get_ip_address(),
                'java_opts':            self._get_java_opts(),
                'process_user':         self._get_process_user(),
                'process_group':        self._get_process_group(),               
            }
            if self.get_prop("install-source"):
                values['install_source'] = "file://%s" % (
                    self.get_prop("install-source"),)
            if "deconfigure" in parameters:
                values['absent'] = 'true'
            config = {'type': 'jboss::container',
                      'id': self.get_prop('instance-name'),
                      'values': values
                     }
            self.configuration.append(config)

            return {'success':
                    'JEE container configured successfully'}
        except Exception as e:
            return {'error':
                'JEE container failed to configure ',
                'message': str(e)}

    def _verify(self, parameters={}):
        ''' Verify JEE Container
            Queries the node for this containers running service
        '''
        try:
            parentnode = self.get_parent_node()
            result, stdout, stderr = parentnode.execute(["service %s status" \
                % (self.get_prop('instance-name'),)])
            if result:
                return {'error': 'Verify failed for JEE container %s: %s' % (
                    self.get_prop('instance-name'), stderr)}
            else:
                if "is running" in stdout:
                    return {'success': "JEE container %s is running" % (
                        self.get_prop('instance-name'), )}
                else:
                    return {'error': "JEE container %s not running" % (
                        self.get_prop('instance-name'),)}
        except Exception, e:
            return {'error': 'Error verifying JEE container %s: %s' % (
                self.get_prop('instance-name'), e.message)}
