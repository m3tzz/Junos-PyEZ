from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='x.x.x.x', user='demo', password='demo', gather_facts=False)
dev.open()

cu = Config(dev)
data = """<applications>
        <application>
            <name>test-12345</name>
            <protocol>tcp</protocol>
            <destination-port>12345-12345</destination-port>
         </application>
    </applications>"""
print cu.load(data)
if cu.commit_check():
   print "Commi_check - OK!\n Commit - Done!"
   cu.commit()
else:
   print "Rollback!"
   cu.rollback()
