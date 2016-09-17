from jnpr.junos import Device
from lxml import etree

dev = Device(host='x.x.x.x', user='demo', password='demo' )

dev.open()

cnf = dev.rpc.get_config()

print etree.tostring(cnf)
