import serial
from xbee import ZigBee
from ctypes import c_int8
import binascii as ba
import struct


class CoordResource:
    def __init__(self, port, baud=9600):
        self.port = port
        self.baud = baud

    def __enter__(self):
        class Coordinator:
            def __init__(self, port, baud):
                self.serial_port = serial.Serial(port, baud)
                self.xbee = ZigBee(self.serial_port)

            def stop(self):
                self.serial_port.close()

            def received(self):
                response = self.xbee.wait_read_frame()
                if response['id'] == 'rx':
                    packet = dict()
                    packet['addr_long'] = ba.b2a_hex(response['source_addr_long'])
                    packet['addr'] = ba.b2a_hex(response['source_addr'])
                    data = response['rf_data']
                    packet['temp'] = c_int8(data[0]).value + (c_int8(data[1]).value / 100.0)
                    packet['humidity'] = data[2] + (data[3] / 100.0)
                    return packet

            def respond(self, addr_long, addr, value):
                da_long = ba.a2b_hex(addr_long)
                da = ba.a2b_hex(addr)
                dat = struct.pack('>B', value)
                self.xbee.send("tx", dest_addr_long=da_long, dest_addr=da, data=dat)

        self.coordinator = Coordinator(self.port, self.baud)
        return self.coordinator

    def __exit__(self, exc_type, exc_value, traceback):
        self.coordinator.stop()
