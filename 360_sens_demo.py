# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:26:29 2021

@author: Gona Sai Nikhil
"""



import numpy as np
import serial
import time
import threading


ser = serial.Serial('com3',baudrate=1000000)

def multiprocessing_func(k):
    print("avoid_obssssssssssssssssssssssss")
    time.sleep(2)
    print("avoideddddddddddddddddd")

start_word = False

if __name__ == "__main__":
    while True:
        try:
            ser_bytes = ser.readline() # read Arduino serial data
            decoded_bytes = ser_bytes.decode('utf-8') # decode data to utf-8
            data = (decoded_bytes.replace('\r','')).replace('\n','')
            #print(data)
            if start_word:
                j = data.split(",")
                angle1 = j[0]
                dist1 = j[1]
                angle2 = j[2]
                dist2 = j[3]
                dist1 = int(float(dist1))
                dist2 = int(float(dist2))
                angle1 = int(float(angle1))
                angle2 = int(float(angle2))
                print(angle1, dist1, angle2, dist2)
                if dist1<=60 and dist1!=0 and angle1<=30:
                    if angle1 == 0:
                        print("right")
                        x = threading.Thread(target=multiprocessing_func, args=(1,))
                        x.start()
                        #x.join()
                if dist2<=60 and dist2!=0 and angle2>= 330:
                    print("right")
                    #x = threading.Thread(target=multiprocessing_func, args=(1,))
                    #x.start()
                    #x.join()
                if dist1<=60 and dist1!=0 and angle1>=150:
                    print("left")
                if dist2<=60 and dist2!=0 and angle2<= 210:
                    print("left")                                        
                if dist1<=60 and dist1!=0 and angle1 in range(60,120):
                    print("front")
                if dist2<=60 and dist2!=0 and angle2 in range(240,300):
                    print("back") 
                else:
                    print("safe")
            else:
                if data=='Radar Start':# stard word on Arduno
                    start_word = True # wait for Arduino to output start word
                    print('Radar Starting...')
                else:
                    continue
        except KeyboardInterrupt:
            #plt.close('all')
            print('Keyboard Interrupt')
            break
            
        
