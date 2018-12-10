# -*- coding: utf-8 -*-

# This software is released under the MIT License.
#
# Copyright (c) 2018 Orange Cloud for Business / Cloudwatt
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


NAME = 'compute.servers'

FIXTURES = [{'OS-DCF:diskConfig': 'AUTO',
  'OS-EXT-AZ:availability_zone': 'nova',
  'OS-EXT-SRV-ATTR:hypervisor_hostname': None,
  'OS-EXT-SRV-ATTR:instance_name': None,
  'OS-EXT-SRV-ATTR:user_data': None,
  'OS-EXT-STS:power_state': 1,
  'OS-EXT-STS:task_state': None,
  'OS-EXT-STS:vm_state': 'active',
  'OS-SCH-HNT:scheduler_hints': None,
  'OS-SRV-USG:launched_at': '2018-11-09T13:39:42.000000',
  'OS-SRV-USG:terminated_at': None,
  'accessIPv4': '',
  'accessIPv6': '',
  'addresses': {'tellurium_net': [{'OS-EXT-IPS-MAC:mac_addr': '02:4f:41:34:32:b4',
                                   'OS-EXT-IPS:type': 'fixed',
                                   'addr': '192.168.0.6',
                                   'version': 4}]},
  'adminPass': None,
  'block_device_mapping_v2': None,
  'config_drive': '',
  'created': '2018-11-09T13:39:38Z',
  'flavor': {'id': '17',
             'links': [{'href': 'https://compute.fr1.cloudwatt.com/9824a7403a1b411d8d207d26218597ce/flavors/17',
                        'rel': 'bookmark'}]},
  'flavorRef': None,
  'hostId': '84246cf2f8ac920628901e7a84a054b45f246f2d77f6df3f6c30cc43',
  'id': '99c42e21-5099-4903-9121-063925aad299',
  'image': {},
  'imageRef': None,
  'key_name': 'tellurium-key',
  'links': [{'href': 'https://compute.fr1.cloudwatt.com/v2/9824a7403a1b411d8d207d26218597ce/servers/99c42e21-5099-4903-9121-063925aad299',
             'rel': 'self'},
            {'href': 'https://compute.fr1.cloudwatt.com/9824a7403a1b411d8d207d26218597ce/servers/99c42e21-5099-4903-9121-063925aad299',
             'rel': 'bookmark'}],
  'metadata': {},
  'name': 'Ubuntu 14.04',
  'networks': None,
  'os-extended-volumes:volumes_attached': [{'id': '8ca10346-fe4c-4e68-9a18-98df875d1ecc'}],
  'personality': None,
  'progress': 0,
  'security_groups': [{'name': 'http'}, {'name': 'default'}],
  'status': 'ACTIVE',
  'tenant_id': '9824a7403a1b411d8d207d26218597ce',
  'updated': '2018-11-09T13:39:42Z',
  'user_id': '7f71ea7b8abd41e5a1f303f4a1bc16b9'},
 {'OS-DCF:diskConfig': 'MANUAL',
  'OS-EXT-AZ:availability_zone': 'nova',
  'OS-EXT-SRV-ATTR:hypervisor_hostname': None,
  'OS-EXT-SRV-ATTR:instance_name': None,
  'OS-EXT-SRV-ATTR:user_data': None,
  'OS-EXT-STS:power_state': 1,
  'OS-EXT-STS:task_state': None,
  'OS-EXT-STS:vm_state': 'active',
  'OS-SCH-HNT:scheduler_hints': None,
  'OS-SRV-USG:launched_at': '2018-11-09T04:54:35.000000',
  'OS-SRV-USG:terminated_at': None,
  'accessIPv4': '',
  'accessIPv6': '',
  'addresses': {'tellurium_net': [{'OS-EXT-IPS-MAC:mac_addr': '02:3d:ec:f6:f8:25',
                                   'OS-EXT-IPS:type': 'fixed',
                                   'addr': '192.168.0.3',
                                   'version': 4}]},
  'adminPass': None,
  'block_device_mapping_v2': None,
  'config_drive': '',
  'created': '2018-11-09T04:54:32Z',
  'flavor': {'id': '42',
             'links': [{'href': 'https://compute.fr1.cloudwatt.com/9824a7403a1b411d8d207d26218597ce/flavors/42',
                        'rel': 'bookmark'}]},
  'flavorRef': None,
  'hostId': 'dd853263647ff603cfe0726dc78e34e0b9b2fc092bead501af233bcf',
  'id': '2cf8db13-312a-4307-ba38-43b727ebcce6',
  'image': {'id': '8254d703-e46f-4101-88ff-6f40bf7df51a',
            'links': [{'href': 'https://compute.fr1.cloudwatt.com/9824a7403a1b411d8d207d26218597ce/images/8254d703-e46f-4101-88ff-6f40bf7df51a',
                       'rel': 'bookmark'}]},
  'imageRef': None,
  'key_name': 'tellurium-key',
  'links': [{'href': 'https://compute.fr1.cloudwatt.com/v2/9824a7403a1b411d8d207d26218597ce/servers/2cf8db13-312a-4307-ba38-43b727ebcce6',
             'rel': 'self'},
            {'href': 'https://compute.fr1.cloudwatt.com/9824a7403a1b411d8d207d26218597ce/servers/2cf8db13-312a-4307-ba38-43b727ebcce6',
             'rel': 'bookmark'}],
  'metadata': {},
  'name': 'tellurium_win_instance',
  'networks': None,
  'os-extended-volumes:volumes_attached': [],
  'personality': None,
  'progress': 0,
  'security_groups': [{'name': 'default'}],
  'status': 'ACTIVE',
  'tenant_id': '9824a7403a1b411d8d207d26218597ce',
  'updated': '2018-11-09T04:55:58Z',
  'user_id': '7f71ea7b8abd41e5a1f303f4a1bc16b9'},
 {'OS-DCF:diskConfig': 'MANUAL',
  'OS-EXT-AZ:availability_zone': 'nova',
  'OS-EXT-SRV-ATTR:hypervisor_hostname': None,
  'OS-EXT-SRV-ATTR:instance_name': None,
  'OS-EXT-SRV-ATTR:user_data': None,
  'OS-EXT-STS:power_state': 1,
  'OS-EXT-STS:task_state': None,
  'OS-EXT-STS:vm_state': 'active',
  'OS-SCH-HNT:scheduler_hints': None,
  'OS-SRV-USG:launched_at': '2018-11-09T04:57:15.000000',
  'OS-SRV-USG:terminated_at': None,
  'accessIPv4': '',
  'accessIPv6': '',
  'addresses': {'tellurium_net': [{'OS-EXT-IPS-MAC:mac_addr': '02:cb:33:6b:60:f2',
                                   'OS-EXT-IPS:type': 'fixed',
                                   'addr': '192.168.0.5',
                                   'version': 4}]},
  'adminPass': None,
  'block_device_mapping_v2': None,
  'config_drive': '',
  'created': '2018-11-09T04:54:32Z',
  'flavor': {'id': '42',
             'links': [{'href': 'https://compute.fr1.cloudwatt.com/9824a7403a1b411d8d207d26218597ce/flavors/42',
                        'rel': 'bookmark'}]},
  'flavorRef': None,
  'hostId': 'b357f8b6b7368a07bb2aed776c6579d132c90f7dcb2f28a2a34c98e8',
  'id': 'b6316031-e629-48b8-aac5-3f1b21ffe0f3',
  'image': {'id': '8254d703-e46f-4101-88ff-6f40bf7df51a',
            'links': [{'href': 'https://compute.fr1.cloudwatt.com/9824a7403a1b411d8d207d26218597ce/images/8254d703-e46f-4101-88ff-6f40bf7df51a',
                       'rel': 'bookmark'}]},
  'imageRef': None,
  'key_name': 'tellurium-key-phrase',
  'links': [{'href': 'https://compute.fr1.cloudwatt.com/v2/9824a7403a1b411d8d207d26218597ce/servers/b6316031-e629-48b8-aac5-3f1b21ffe0f3',
             'rel': 'self'},
            {'href': 'https://compute.fr1.cloudwatt.com/9824a7403a1b411d8d207d26218597ce/servers/b6316031-e629-48b8-aac5-3f1b21ffe0f3',
             'rel': 'bookmark'}],
  'metadata': {},
  'name': 'tellurium_win_instance_ssh_pass',
  'networks': None,
  'os-extended-volumes:volumes_attached': [],
  'personality': None,
  'progress': 0,
  'security_groups': [{'name': 'default'}],
  'status': 'ACTIVE',
  'tenant_id': '9824a7403a1b411d8d207d26218597ce',
  'updated': '2018-11-09T04:59:08Z',
  'user_id': '7f71ea7b8abd41e5a1f303f4a1bc16b9'},
 {'OS-DCF:diskConfig': 'MANUAL',
  'OS-EXT-AZ:availability_zone': 'nova',
  'OS-EXT-SRV-ATTR:hypervisor_hostname': None,
  'OS-EXT-SRV-ATTR:instance_name': None,
  'OS-EXT-SRV-ATTR:user_data': None,
  'OS-EXT-STS:power_state': 1,
  'OS-EXT-STS:task_state': None,
  'OS-EXT-STS:vm_state': 'active',
  'OS-SCH-HNT:scheduler_hints': None,
  'OS-SRV-USG:launched_at': '2018-11-09T04:54:36.000000',
  'OS-SRV-USG:terminated_at': None,
  'accessIPv4': '',
  'accessIPv6': '',
  'addresses': {'tellurium_net': [{'OS-EXT-IPS-MAC:mac_addr': '02:20:6d:f7:16:da',
                                   'OS-EXT-IPS:type': 'fixed',
                                   'addr': '192.168.0.4',
                                   'version': 4}]},
  'adminPass': None,
  'block_device_mapping_v2': None,
  'config_drive': '',
  'created': '2018-11-09T04:54:32Z',
  'flavor': {'id': '16',
             'links': [{'href': 'https://compute.fr1.cloudwatt.com/9824a7403a1b411d8d207d26218597ce/flavors/16',
                        'rel': 'bookmark'}]},
  'flavorRef': None,
  'hostId': 'a5586828459ec792613bc24c0807801ce4341a562d47ff3203d41722',
  'id': '4add78fa-93df-4550-aaf7-aba2239ba00a',
  'image': {'id': 'dd7d4b21-79b8-42f0-8464-0d1a5274c638',
            'links': [{'href': 'https://compute.fr1.cloudwatt.com/9824a7403a1b411d8d207d26218597ce/images/dd7d4b21-79b8-42f0-8464-0d1a5274c638',
                       'rel': 'bookmark'}]},
  'imageRef': None,
  'key_name': 'tellurium-key',
  'links': [{'href': 'https://compute.fr1.cloudwatt.com/v2/9824a7403a1b411d8d207d26218597ce/servers/4add78fa-93df-4550-aaf7-aba2239ba00a',
             'rel': 'self'},
            {'href': 'https://compute.fr1.cloudwatt.com/9824a7403a1b411d8d207d26218597ce/servers/4add78fa-93df-4550-aaf7-aba2239ba00a',
             'rel': 'bookmark'}],
  'metadata': {},
  'name': 'tellurium_instance',
  'networks': None,
  'os-extended-volumes:volumes_attached': [],
  'personality': None,
  'progress': 0,
  'security_groups': [{'name': 'default'}],
  'status': 'ACTIVE',
  'tenant_id': '9824a7403a1b411d8d207d26218597ce',
  'updated': '2018-11-09T05:22:45Z',
  'user_id': '7f71ea7b8abd41e5a1f303f4a1bc16b9'}]