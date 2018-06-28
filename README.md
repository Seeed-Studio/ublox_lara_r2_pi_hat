# ublox_lara_r2_pi_hat

This python module is used for Ublox lara r2 cellular module should only runs on Raspberry Pi.

### Using pip to install 
```
pip install ublox_lara_r2
```

**or**

### Download the source code to install
```
git clone https://github.com/Seeed-Studio/ublox_lara_r2_pi_hat
sudo python setup.py install
```

### Test
```
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
```

```
40-pin GPIO header detected
Enabling CTS0 and RTS0 on GPIOs 16 and 17
rts cts on
waking up...
module name:  LARA-R211
RSSI:  3
```
