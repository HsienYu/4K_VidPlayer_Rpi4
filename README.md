# 4K_VidPlayer_Rpi4
4k Video player with auto-mount and loop in files in USB stick, base on LIbreELEC.

autoplay & loop and read videos from usb stick
----------------------------------------------
For Leia Version https://libreelec.tv/raspberry-pi-4/  
 mv autoexec.py ~/.kodi/userdata/   
 chmod +x ~/.kodi/userdata/autoexec.py  

remove OSD menu when looping videos
-----------------------------------
 cp /usr/share/kodi/addons/skin.estuary ~/.kodi/addons/  
 mv DialogSeekBar.xml ~/.kodi/addons/skin.estuary/xml/DialogSeekBar.xml  

reboot
