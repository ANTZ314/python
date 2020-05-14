# -*- coding: utf-8 -*-
"""
author: Antony Smith

description: 

Path: cd /home/antz/GIT314/python/threading

Run: python3 timethread1.py
"""
import threading
import time
import atexit

def do_work():

  i = 0
  @atexit.register
  def goodbye():
    print ("'CLEANLY' kill sub-thread with value: %s [THREAD: %s]" %
           (i, threading.currentThread().ident))

  while True:
    print i
    i += 1
    time.sleep(1)

t = threading.Thread(target=do_work)
t.daemon = True
t.start()

def after_timeout():
  print "KILL MAIN THREAD: %s" % threading.currentThread().ident
  raise SystemExit

threading.Timer(2, after_timeout).start()