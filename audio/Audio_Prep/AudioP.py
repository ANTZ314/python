# -*- coding: utf-8 -*-
"""
Created on Feb 3rd 10:08:20 2017
@author: Antony Smith
@description: Class of Audio Operators
"""
import AudioClassP as AudioP

def main():
    silence = True                          # 
    Time=0                                  #    
    
    # Instantiate the class
    Aud = AudioP.AudioClass()               # Create object to access 'Audioclass' Class
    Aud.message("ENGAGE!")                  # Pass test message to the class
    
    print ("Get device info...")
    devinfo1 = Aud.find_device()            # Pass Device number to next process
    
    print ("\nStart listening...")	
    Aud.listen(silence,Time,devinfo1)       # pass found audio device details
    
    print("\nComplete...")
    
if __name__ == "__main__": main()