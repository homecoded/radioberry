import subprocess

class InetConnection:

    COMMAND_RESET_WLAN = 'sudo /sbin/ifdown wlan0 && sleep 10 && sudo /sbin/ifup --force wlan0'
    COMMAND_REBOOT = 'sudo reboot'
    COMMAND_CHECK_WLAN = 'ping -c 2 -w 1 -q 192.168.0.1 | grep "1 received" > /dev/null 2> /dev/null'

    def __init__(self):
        self.connection_alive = True

    def check(self):
        ping_result = subprocess.call([self.COMMAND_CHECK_WLAN], shell=True)
        print(ping_result)
        if ping_result:
            if self.connection_alive:
                self.reconnect()
            else:
                self.reboot()
            return False
        else:
            return True

    def reconnect(self):
        print 'Attempt reconnect...'
        subprocess.call([self.COMMAND_RESET_WLAN], shell=True)

    def reboot(self):
        print 'Attempt reboot ...'
        subprocess.call([self.COMMAND_REBOOT], shell=True)