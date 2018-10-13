import getpass
import sys

from netmiko import ConnectHandler

COMMAND = sys.argv[1]
USER = input('Username: ')
PASSWORD = getpass.getpass()
#ENABLE_PASS = getpass.getpass(prompt='Enter enable password: ')

#DEVICES_IP = ['192.168.100.1', '192.168.100.2', '192.168.100.3']
DEVICES_IP = ['10.100.0.30', '10.100.0.31', '10.100.0.32']

USER = 'cisco'
PASSWORD = 'cisco5'

for IP in DEVICES_IP:
    print('Connection to device {}'.format(IP))
    DEVICE_PARAMS = {
        'device_type': 'juniper_junos',
        'ip': IP,
        'username': USER,
        'password': PASSWORD
#        'secret': ENABLE_PASS
    }

    with ConnectHandler(**DEVICE_PARAMS) as ssh:
        ssh.enable()

        result = ssh.send_command(COMMAND)
        print(result)

'''
(pyneng) python@python:~/pyneng/exercise/19$ python ./4_netmiko.py "show route table inet.0"
Username: cisco
Password: 
Connection to device 10.100.0.30


inet.0: 13 destinations, 13 routes (13 active, 0 holddown, 0 hidden)
+ = Active Route, - = Last Active, * = Both

0.0.0.0/0          *[Static/5] 01:43:16
                    > to 198.51.100.46 via irb.600
10.100.0.0/24      *[Direct/0] 2w4d 20:16:39
                    > via em0.0
10.100.0.30/32     *[Local/0] 2w4d 20:16:39
                      Local via em0.0
10.229.4.0/32      *[Static/5] 01:43:16
                    > to 10.230.0.28 via ae0.0
10.230.0.28/31     *[Direct/0] 01:43:16
                    > via ae0.0
10.230.0.29/32     *[Local/0] 2w4d 20:16:39
                      Local via ae0.0
10.230.0.30/31     *[Direct/0] 01:43:16
                    > via ae0.0
10.230.0.31/32     *[Local/0] 2w4d 20:16:39
                      Local via ae0.0
192.1.0.0/24       *[Direct/0] 01:43:16
                    > via irb.3333
192.1.0.3/32       *[Local/0] 2w4d 20:16:39
                      Local via irb.3333
198.51.100.32/28   *[Direct/0] 01:43:16
                    > via irb.600
198.51.100.36/32   *[Local/0] 2w4d 20:16:39
                      Local via irb.600
224.0.0.22/32      *[IGMP/0] 2w4d 20:06:20
                      MultiRecv

Connection to device 10.100.0.31


inet.0: 11 destinations, 11 routes (7 active, 0 holddown, 4 hidden)
+ = Active Route, - = Last Active, * = Both

10.100.0.0/24      *[Direct/0] 2w4d 13:42:20
                    > via em0.0
10.100.0.31/32     *[Local/0] 2w4d 13:42:20
                      Local via em0.0
10.230.0.32/31     *[Direct/0] 2w4d 13:39:55
                    > via ge-0/0/0.0
10.230.0.33/32     *[Local/0] 2w4d 13:39:57
                      Local via ge-0/0/0.0
192.1.0.0/24       *[Direct/0] 2w4d 13:39:55
                    > via ge-0/0/0.3333
192.1.0.2/32       *[Local/0] 2w4d 13:39:56
                      Local via ge-0/0/0.3333
224.0.0.22/32      *[IGMP/0] 2w4d 13:42:21
                      MultiRecv

Connection to device 10.100.0.32


inet.0: 15 destinations, 15 routes (11 active, 0 holddown, 4 hidden)
+ = Active Route, - = Last Active, * = Both

0.0.0.0/0          *[Static/5] 01:42:25
                    > to 198.51.100.46 via irb.600
10.100.0.0/24      *[Direct/0] 5w0d 04:06:51
                    > via em0.0
10.100.0.32/32     *[Local/0] 5w0d 04:06:51
                      Local via em0.0
10.230.0.34/31     *[Direct/0] 01:42:25
                    > via ae2.0
10.230.0.35/32     *[Local/0] 5w0d 04:06:51
                      Local via ae2.0
10.230.0.36/31     *[Direct/0] 01:42:25
                    > via ae2.0
10.230.0.37/32     *[Local/0] 5w0d 04:06:51
                      Local via ae2.0
192.1.0.0/24       *[Direct/0] 01:42:25
                    > via irb.3333
192.1.0.1/32       *[Local/0] 5w0d 04:06:51
                      Local via irb.3333
198.51.100.32/28   *[Direct/0] 01:42:25
                    > via irb.600
198.51.100.35/32   *[Local/0] 5w0d 04:06:51
                      Local via irb.600
'''
