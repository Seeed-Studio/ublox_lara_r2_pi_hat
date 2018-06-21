#!/usr/bin/python

import os
import thread
import serial
import time
import RPi.GPIO as GPIO

class Ublox_lara_r2():
    def __init__(self, port = "/dev/ttyAMA0", baudrate = 115200):
        self.cmd_done = False
        self.power_pin = 29
        self.reset_pin = 31
        self.keep_receive_alive = True        
        self.debug = True
        self.response = ""

        self.comm = serial.Serial(port, baudrate)
   
    def __del__(self):
        self.disabel_rtscts()
        self.cmd_done = True
        self.keep_receive_alive = False

       
    def initialize(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.power_pin, GPIO.OUT) # Setup module power pin
        GPIO.setup(self.reset_pin, GPIO.OUT) # Setup module reset pin 
        GPIO.output(self.power_pin, False)
        GPIO.output(self.reset_pin, False)
        self.enable_rtscts()
        self.start_receive_handle()
        
    
    def enable_rtscts(self):
        os.system("rpirtscts on")
        if self.debug:
            print("rts cts on")


    def disabel_rtscts(self):
        os.system("rpirtscts off")
        if self.debug:
            print("rts cts off")

    def power_on(self):
        GPIO.output(self.power_pin, True)
        time.sleep(1.0)
        GPIO.output(self.power_pin, False)

    def power_off(self):
        GPIO.output(self.power_pin, True)
        time.sleep(1.2)
        GPIO.output(self.power_pin, False)

    def handle_receive(self):        
        while True == self.keep_receive_alive:                     
            if self.comm.readable():                
                line = self.comm.readline()
                self.response += line
                if self.debug:
                    print '<'+line,

    def start_receive_handle(self):
        thread.start_new_thread(self.handle_receive, ())
    
    # def 
    def send(self, cmd):        
        self.response = ""
        self.comm.write(cmd)
        if self.debug:        
            print("> " + cmd)
        

    def sendAT(self, cmd, response = None, timeout=1):        
        self.cmd_done=False
        self.response = ""
        attempts = timeout 
        while not self.cmd_done and attempts >= 0:            
            self.comm.write(cmd)
            if self.debug:
                print '>'+cmd,
            time.sleep(0.5)
            if None != response:            
                if self.response.find(response)>=0:
                    self.cmd_done = True
            elif None == response:
                self.cmd_done = True
            attempts = attempts - 1 
            time.sleep(0.5)       

        return (attempts >= 0)

    def getRSSI(self):
        rssi = ""
        self.sendAT("AT+CSQ\r\n", 'OK\r\n')
        if self.response != "":
            parts = self.response.split('\r\n')
            # print parts
            for part in parts:
                parse_index = part.find('+CSQ: ')
                if parse_index is not -1:
                    rssi = part[6:].split(',')[0]
                    break
        return rssi

if __name__ == "__main__":
    ublox = Ublox_lara_r2()
    # ublox.debug = True
    ublox.initialize()    

    if not ublox.sendAT("AT\r\n", "OK\r\n"):
        ublox.power_on()
        while not ublox.sendAT("AT\r\n", 'OK\r\n'):
            print('waking...')

    print 'Signal RSSI: ' + ublox.getRSSI()
    ublox.sendAT("AT+CFUN?\r\n", 'OK\r\n')
    print ublox.response    
   
    ublox.sendAT("AT+CGMM\r\n", 'OK')
    print ublox.response

