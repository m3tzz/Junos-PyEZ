from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable

import code

# Here a class is defined, which matches our requirements.
# 1.  Uptime of each device
# 2.  Current software version
# 3.  Device serial number
# 4.  MAC address for each active Ethernet interface

class style:
   BOLD = '\033[1m'
   END = '\033[0m'


class NetworkRequirements(object):
    _hostname = ''
    _model = ''
    _uptime =  ''
    _version = ''
    _serial = ''
    _interfaces = []
    _device = []

    def __init__(self, uptime, version, serial, hostname, model, device):
        # This is our constructor. Populate each variable.
        self._up_time = uptime
        self._version = version
        self._serial = serial
        self._hostname = hostname
        self._model = model
        self._device = device

        # Here we bind an EthPortTable called 'eth_ports' to our device object field within the class.
        self._device.bind(eth_ports = EthPortTable)
        # Then we call '.get()' to populate the table.
        self._device.eth_ports.get()


    def __str__(self):

        x = 0
        return_string = ''
        return_string += 64*"="
        return_string += "\n"
        return_string += 16*" " + style.BOLD + "Element Report" + style.END
        return_string += "\n"
        return_string += 64*"="
        return_string += "\n"
        return_string += style.BOLD + "Hostname:\t" + style.END + self._hostname
        return_string += "\n"
        return_string += style.BOLD + "Model:\t" + style.END + self._model
        return_string += "\n"
        return_string += style.BOLD + "Uptime:\t" + style.END + self._up_time
        return_string += "\n"
        return_string += style.BOLD + "Version:\t" + style.END + self._version
        return_string += "\n"
        return_string += style.BOLD + "Serial:\t" + style.END + self._serial
        return_string += "\n"

        # As tables in PyEZ are iterable and since we've bound our table to our device, we can now do this.

        for port in self._device.eth_ports:
            return_string += style.BOLD + "Interface: " + style.END + port.name + style.BOLD + "\tMAC Address:\t" + style.END + port.macaddr + "\n" # or you can do it like this: + port['macaddr'] + "n"

        return_string += "\n"
        return_string += 64*"="
        return_string += "\n"
        return_string += 21*" " + style.BOLD + "End of Element Report" + style.END
        return_string += "\n"
        return_string += 64*"="

        return return_string


if __name__ == '__main__':

    # Create our device object and assign the hostname or IP address, username and password
    dev1 = Device( host='x.x.x.x', user='demo', password='demo' )

    # Open a connection to the device. Please note, we're doing some very simple exception handling!
    dev1.open()

    # Let's create our object and initialise it
    SRX01 = NetworkRequirements(dev1.facts['RE0']['up_time'], dev1.facts['version'], dev1.facts['serialnumber'], dev1.facts['hostname'], dev1.facts['model'], dev1)

    # Now let's see if our class works and print out the data! Once we call this special class function, the string is returned as expected.

    print SRX01

    dev1.close()
