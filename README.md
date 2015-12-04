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

Let's open the **Scanner.py** file, .py standing for python.


