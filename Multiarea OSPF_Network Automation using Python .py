#!/usr/bin/env python

from netmiko import ConnectHandler
import os

iosv_l3_r1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.11',
    'username': 'badrik',
    'password': 'cisco',
}

iosv_l3_r2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.12',
    'username': 'badrik',
    'password': 'cisco',
}

iosv_l3_r3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.13',
    'username': 'badrik',
    'password': 'cisco',
}

def configuration():
         net_connect = ConnectHandler(**devices)
         output = net_connect.send_config_set(lines)
         print(output)

def output():
        net_connect = ConnectHandler(**devices)
        #net_connect.find_prompt()
        command = raw_input("Type the priviledge mode command to find required information")
        output = net_connect.send_command(command)
        return output

all_devices = [iosv_l3_r1,iosv_l3_r2,iosv_l3_r3]

for devices in all_devices:
        if devices == iosv_l3_r1:
                with open('R1.txt') as f:
                    lines = f.read().splitlines()
                print(lines)
                configuration()
                output()

        if devices == iosv_l3_r2:
                with open('R2.txt') as f:
                    lines = f.read().splitlines()
                print(lines)
                configuration()

        if devices == iosv_l3_r3:
                with open('R3.txt') as f:
                    lines = f.read().splitlines()
                print(lines)
                configuration()

print("\nType the device name from the mentioned below:")
for devices in all_devices:
        print(devices)
device = raw_input("Enter the name: \t")
net_connect = ConnectHandler(**device)
command = raw_input("\nType the priviledge mode command to find required information")
output = net_connect.send_command(command)
print(output)

File = raw_input("\nDo you want to save output in a file.?")
        if File == "Yes" or "yes":
                os.system("touch output.txt")
        with open("output.txt","w") as f:
                f.write(output)
