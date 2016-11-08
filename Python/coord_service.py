from coord_imp import CoordResource
from csvfiles import store, readrate
import configparser
import binascii as ba

# Read Config from config.ini
config = configparser.ConfigParser()
config.read("config.ini")
# Serial Config
port = config.get('Serial', 'port')
baud = config.getint('Serial', 'baud')
# Xbee Config
addr_64_s = config.get('Xbee', 'addr').split(',')
addr_64 = [ba.a2b_qp(a) for a in addr_64_s]
# Files Config
prefix_d = config.get('Files', 'prefixData')
prefix_s = config.get('Files', 'prefixSetup')
extension = config.get('Files', 'extension')
datafiles = [prefix_d + str(id_node+1) + extension for id_node in range(len(addr_64))]
setupfiles = [prefix_s + str(id_node+1) + extension for id_node in range(len(addr_64))]
datalocation = config.get('Files', 'locData')
setuplocation =  config.get('Files', 'locSetup')

with CoordResource(port=port, baud=baud) as coordinator:
    while True:
        try:
            packet = coordinator.received()
            print(packet)
            if packet is not None:
                id_node = addr_64.index(packet['addr_long'])
                packet.update({'sensor': id_node+1})
                store(datalocation + datafiles[id_node], packet)
                rate = readrate(setuplocation + setupfiles[id_node])
                coordinator.respond(packet['addr_long'], packet['addr'], rate)
        except KeyboardInterrupt:
            break
