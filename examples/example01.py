from ublox_lara_r2 import *

u = Ublox_lara_r2()
u.initialize()
u.reset_power()

# Close debug massage 
u.debug = False

# show module name
if u.sendAT("AT+CGMM\r\n", "OK\r\n"):
    print "\r\nmodule name: ", u.response.split('\r\n')[1]

# get SIM card state
if u.sendAT("AT+CSIM?\r\n", "OK\r\n"):
    print "\r\nSIM state: ", u.response.split('\r\n')[1]

# check rssi
rssi = u.getRSSI()
print "RSSI: ", rssi
