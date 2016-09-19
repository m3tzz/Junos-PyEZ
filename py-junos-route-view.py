from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable

dev = Device(host='x.x.x.x', user='demo', password='demo', gather_facts=False)
dev.open()

tbl = RouteTable(dev)
tbl.get()

print tbl
for item in tbl:
    print 'protocol:', item.protocol
    print 'age:', item.age
    print 'via:', item.via
    print 'nexthop:', item.nexthop
    print
dev.close()
