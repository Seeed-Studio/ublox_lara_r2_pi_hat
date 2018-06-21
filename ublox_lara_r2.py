#!/usr/bin/python

import os
import thread
import serial
import time
import RPi.GPIO as GPIO

class ublox_lara_r2():
    def __init__(self):
        self.cmd_done = False
        self.power_pin = 29
        self.reset_pin = 31
        self.keep_receive_alive = True        
        self.debug = False
        self.recv_buffer = ""

        self.comm = serial.Serial("/dev/ttyAMA0", 115200)
   
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
                self.recv_buffer += line
                if self.debug:
                    print '<'+line,

    def start_receive_handle(self):
        thread.start_new_thread(self.handle_receive, ())
    
    # def 
    def send(self, cmd):        
        self.recv_buffer = ""
        self.comm.write(cmd)
        if self.debug:        
            print("> " + cmd)
        

    def sendAT(self, cmd, response = None, timeout=1):        
        self.cmd_done=False
        self.recv_buffer = ""
        attempts = timeout 
        while not self.cmd_done and attempts >= 0:            
            self.comm.write(cmd)
            if self.debug:
                print '>'+cmd,
            time.sleep(0.5)
            if None != response:            
                if self.recv_buffer.find(response)>=0:
                    self.cmd_done = True
            elif None == response:
                self.cmd_done = True
            attempts = attempts - 1 
            time.sleep(0.5)       

        return (attempts >= 0)

    def getSignalRSSI(self):
        rssi = ""
        self.sendAT("AT+CSQ\r\n", 'OK\r\n')
        if self.recv_buffer != "":
            parts = self.recv_buffer.split('\r\n')
            # print parts
            for part in parts:
                parse_index = part.find('+CSQ: ')
                if parse_index is not -1:
                    rssi = part[6:].split(',')[0]
                    break
        return rssi

if __name__ == "__main__":
    ublox = ublox_lara_r2()
    ublox.debug = True
    ublox.initialize()    

    if not ublox.sendAT("AT\r\n", "OK\r\n"):
        ublox.power_on()
        while not ublox.sendAT("AT\r\n", 'OK\r\n'):
            print('waking...')

    print 'Signal RSSI: ' + ublox.getSignalRSSI()
    ublox.sendAT("AT+CFUN?\r\n", 'OK\r\n')
    # print ublox.recv_buffer    
   
    ublox.sendAT("AT+CGMM\r\n", 'OK')
    # print ublox.recv_buffer

