# PiBar-Logging
A full walk-through for a self-logging barcode scanner using a Raspberry Pi

**This will be a blog-styled walk-through:**

Simplicity. Functionality.  Often times you do not hear, or see, those two words next to each other in today's society.
This documentation will supply you with a complete walk-through, and part list, a "how-to" if you will, on turning your personal Raspberry Pi into an elegantly designed, self-logging bardcode scanner.  I like to call this **PiBar-Logging**.


### Supplies

First, lets talk about the items you'll need.

At the time being, the cheap option via Amazon was to buy Canakit's "Raspberry Pi 2 Ultimate Starter kit (clear case)" bundle. This may not be the case anymore.

For your project you'll need the following items:
  
  * 1  Raspberry Pi 2 Model B (I chose this one for the amount of USB ports the device had (4))
  * 1  Micro SD card with NOOBS installed
  * 1  Wifi Dongle
  * 1  USB Flash Drive (any size 1GB or larger will work)
  * 1  2.5A Power Supply for Raspberry Pi's
  * 1  USB Barcode Scanner (any scanner will do -- for my build, I used one from Alacrity)
  
Gather those items, and you'll be set!  

### Diving into the code


This project is very simple, and only requires two small scripts, one in python, and one in bash, both of which you'll write the code on the Raspberry Pi itself. Before we dive into the code, you'll need to hook up your Raspberry Pi.  There are two main methods of working on your Pi, SSH'ing (Secure Shell) into your Pi from your main PC, and working from the command line.  This path is slightly more difficult, and will not be covered in this guide.  I chose the "old-fashioned" method, externalling hooking up a mouse, keyboard, and monitor(HDMI) to the device.  It's like having the hard copy of a good book, compared to reading it on a tablet.


Review the two files listed in this repository, they will be direct access to working code, but I highly suggest you type the code yourselves, so you understand what you're doing, and what I'll be talking about.

#### Going over "Scanner.py"
Let's open the **Scanner.py** file, ".py" standing for python.  

This small script will run continuously, until it meets one of the two conditions are met, idNumber equalling the integer 777777777, which in my scenario will never happen(you need to set this value to something that will never be scanned...or structure your loop differently, or idNumber equalling the string "terminate"(this **WILL** happen).

**PLEASE PAY ATTENTION THE INDENTATIONS ON THE Scanner.py FILE!! THEY ARE EXTREMELY IMPORTANT IN THE LANGUAGE**


from datetime import datetime
now = datetime.now(); 
import os 

global idNumber
idNumber = raw_imput(' ')

* while idNumber != 777777777:
* 	if idNUmber == 'terminate' 
* 		os.system('Shutdown now -h')
* 	appendFile = open**('/media/usbName', 'a')**  
* 	appendFile.write(str(idNumber) + str(' ') + str(now) + '\n')
* 	appendFile.close()
* 	idNumber = raw_input(' ')

**Another important thing to note...you will HAVE to substitude YOUR usbName.  This will ONLY work for the one Usb, using this configuration**

If you want to use multiple USB's you could create something that finds the USB name, and passes it in as an argument...but that wasn't necessary for this project.

#### Going over "Launcher.sh"

>`#!/bin/sh`

>sudo mount -t vfat -ouid=1000 -ogid=1000 /dev/sda1/media/usbName

>sudo python /home/pi/Scanner.py 

**NOTE**  If you saved these files in another location, you'll need to use the appropriate path name

This is a very small, effective script!  When this script executes, and we will get to how it executes in a moment, it will simply mount your flashdrive under "/dev/sda1/media/**usbName**", and start your python code.  Now "Launcher" makes a little more sense, huh?

In my scenario, the Raspberry Pi will be used without any peripherals: keyboard, monitor, mouse, etc.  The only things plugged in will be the barcode scanner, and USB drive.  I needed a way to start the "Launch" shell script, which will mount my drive, and start my python program.

####Tying it all together

/etc/rc.local
What a beautiful file.  rc.local is a file under the "/etc/" directory, that runs when the Pi boots up, more specifically, before user information is asked (this saves us the trouble of requiring a password bypass - easy to do, just more work).

rc.local is where you'll put a single line of code that will execute our launching script. To do this, open your terminal, and type

>sudo nano /etc/rc.local

this will open the rc.local file in an editor called nano, if you're familiar and more comfortable with other ediors, like VI, use them! Add commands below the comment, but leave the line exit 0 at the end, then save the file and exit.  Lets call the launching script now, by adding this line under the "fi":

>sh /home/pi/launcher.sh

**NOTE**  If you saved these files in another location, you'll need to use the appropriate path name
