#!/usr/bin/python3

import _thread
import time

counter = 0

# Define a function for the thread
def print_time( threadName, delay):
   global counter
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %d %s" % ( threadName, counter, time.ctime(time.time()) ))
      counter += 1

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 2, ) )
except:
   print ("Error: unable to start thread")

while 1:
    time.sleep(1)
    print(".", end='')