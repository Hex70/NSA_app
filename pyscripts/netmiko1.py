from netmiko import ConnectHandler
import sys
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.104',
    'username': 'hex70',
    'password': 'riadm13'
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print (output)

config_commands = ['int loop 2', 'ip address 3.3.3.3 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)


