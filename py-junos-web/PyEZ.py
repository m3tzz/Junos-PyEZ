import sys
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from jnpr.junos.op.fpc import FpcHwTable
from jnpr.junos.op.fpc import FpcInfoTable
from getpass import getpass
from pprint import pprint as pp
from sys import exit
from lxml import etree


import code

# Here a class is defined, which matches our requirements.
# 1.  Uptime of each device
# 2.  Current software version
# 3.  Device serial number
# 4.  MAC address for each active Ethernet interface


class NetworkInfo(object):
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
        #return_string += 64*"="
        #return_string += "\n"
        #return_string += 16*"<b>Report</b>"
        #return_string += "\n"
        #return_string += 64*"="
        #return_string += "\n\n"
        return_string += "<b>Hostname:</b> &nbsp;" + self._hostname
        return_string += "\n\n"
        return_string += "<b>Model:</b> &nbsp;" + self._model
        return_string += "\n\n"
        return_string += "<b>Uptime:</b> &nbsp;" + self._up_time
        return_string += "\n\n"
        return_string += "<b>Version:</b> &nbsp;" + self._version
        return_string += "\n\n"
        return_string += "<b>Serial:</b> &nbsp;" + self._serial
        return_string += "\n\n"

        # As tables in PyEZ are iterable and since we've bound our table to our device, we can now do this.

        for port in self._device.eth_ports:
            return_string += "<b>Interface:</b> &nbsp;" + port.name + "&nbsp;&nbsp;&nbsp;<b> MAC Address:</b> &nbsp;" + port.macaddr + "\n" # or you can do it like this: + port['macaddr'] + "n"

        #return_string += "\n"
        #return_string += 64*"="
        #return_string += "\n"
        #return_string += 21*"<b>End of Report</b>"
        #return_string += "\n"
        #return_string += 64*"="

        return return_string.replace("\n","<br>")

        return return_string


def return_NetworkRequirements(hostname):

    # Create our device object and assign the hostname or IP address, username and password
    dev1 = Device( host=hostname, user='r1', password='estrondeira!' )
    print "DEBITA A INFO CRL!"
    # Open a connection to the device. Please note, we're doing some very simple exception handling!
    dev1.open()
    # Let's create our object and initialise it
    SRX1 = NetworkInfo(dev1.facts['RE0']['up_time'], dev1.facts['version'], dev1.facts['serialnumber'], dev1.facts['hostname'], dev1.facts['model'], dev1)
    # Now let's see if our class works and print out the data! Once we call this special class function, the string is returned as expected.
    dev1.close()

    return SRX1

def return_FPC_Chassis_info(hostname):

    # Create our device object and assign the hostname or IP address, username and password
    dev = Device( host=hostname, user='r1f', password='Estrondeira!' )
    print "DEBITA A INFO FPC CRL!"
    dev.open()

    #print FPC hardware Table
    #get-chassis-inventory
    #print "\n----------------------------------------------------------------------------------------"
    #print "Chassis Installed FPC Details "
    fpcs = FpcHwTable(dev)
    fpcs.get()
    #print fpcs
    #for fpc in fpcs:
             #print fpc.key," Description:", fpc.desc, "Model:", fpc.model,"Serial:", fpc.sn, "Part-number:", fpc.pn

    dev.close()

    return fpcs

def return_FPC_Status_info(hostname):

    # Create our device object and assign the hostname or IP address, username and password
    dev = Device( host=hostname, user='r1', password='Estrondeira' )
    print "DEBITA A INFO FPC CRL!"
    dev.open()

    #invoke get fpc information
    #print "\n----------------------------------------------------------------------------------------"
    #print  "Device FPC Status Details "
    jfpcs = FpcInfoTable(dev)
    jfpcs.get()
    #print jfpcs
    #for item in jfpcs:
    #        print "Slot:", item.key,  "State:", item.state, "Memory Util%:", item.memory, "CPU%:", item.cpu

    dev.close()
    return jfpcs

def return_all_config(hostname):

    # Create our device object and assign the hostname or IP address, username and password
    dev = Device( host=hostname, user='r1', password='Estrondeira!' )
    print "DEBITA A CONFIG CRL!"
    dev.open()
    cnf = dev.rpc.get_config()
    #print etree.tostring(cnf)
    dev.close()
    return etree.tostring(cnf)
