#!/bin/sh

sudo mount -t vfat -ouid=1000 -ogid=1000 /dev/sda1/media/usbName

sudo python /home/pi/Scanner.py 
