import numpy as np
import math
import threading
import time
from datetime import datetime
from random import randint

time_cycle = 80
THOLD = 1000

class MyAlgorithm(threading.Thread):

    def __init__(self, laser, motors, pose3d, machine):
        self.laser = laser
        self.motors = motors
        self.pose3d = pose3d
        self.machine = machine
        self.stop_event = threading.Event()
        self.kill_event = threading.Event()
        self.lock = threading.Lock()
        threading.Thread.__init__(self, args=self.stop_event)

    def run (self):

        while (not self.kill_event.is_set()):
           
            start_time = datetime.now()

            if not self.stop_event.is_set():
                self.execute()

            finish_Time = datetime.now()

            dt = finish_Time - start_time
            ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
            #print (ms)
            if (ms < time_cycle):
                time.sleep((time_cycle - ms) / 1000.0)

    def stop (self):
        self.motors.sendV(0)
        self.motors.sendW(0)
        self.stop_event.set()

    def play (self):
        if self.is_alive():
            self.stop_event.clear()
        else:
            self.machine.setStateActive(0, True)
            self.start()
		
    def kill (self):
        self.kill_event.set()

    def execute(self):
        #GETTING THE IMAGES
        #imageLeft = self.cameraL.getImage()
        #imageRight = self.cameraR.getImage()


        # Add your code here
        print ("Running")
     
        #EXAMPLE OF HOW TO SEND INFORMATION TO THE ROBOT ACTUATORS
        #self.motors.setV(10)
        #self.motors.setW(5)
        #self.motors.sendVelocities()


	#EXAMPLE OF HOW TO GET DATA FROM LASER SENSOR
	#data = self.laser.getLaserData()
	#for i in range(180):
	#	print(data.distanceData[i])
