# Coordinator of Sensor Cirrus
A coordinator is an small computer which has
* a coordinator XBee through which nodes values are received(see [cirrus_node](https://github.com/112358fn/cirrus_node))
* an internet connection for data sync
## How-to
Here you will find a Doc folder which contains the XBee library used and a Python folder with the needed code for the Coordinator task. To execute this python program follow this steps:

* Install the dependencies
````bash
$ cd Python
$ sudo pip install -r dependencies.txt
````
* Edit the configuration file ```config.ini``` 
````
[Serial]
port: /dev/tty.usbserial-142
baud: 9600

[Xbee]
addr = 0013a200407abab0,0013a200407abad1,0013a200407abae9,0013a200407abaa8

[Files]
prefixData = DataNode
prefixSetup = SetupNode
extension = .csv
locData = Data/
locSetup = Setup/
````
* Make sure the coordinator XBee has the correct firmware and configuration. 
This is present on [cirrus_node](https://github.com/112358fn/cirrus_node) under Firmware
* Execute:
````bash
$ python coord_service
````
