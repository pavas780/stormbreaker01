
import os 
import sys
save=os.popen('netsh wlan show profiles').read()
print(save)
available=os.popen('netsh wlan show networks').read() 
print(available)

preferred_ssid=input('enter the wifi to connect :')
res=os.popen("netsh wlan disconnect" ).read() 
print(res)
if preferred_ssid not in save:
  print("profile for"+preferred_ssid+"is not saved in system" ) 
  print("sorry") 
  sys.exit()
else:
  print("profie for"+preferred_ssid+" saved") 
  while true: 
    avail=os.popen('netsh wlan show networks').read() 
    if preferred_ssid in avail:
      print('found') break print("------connecting-------")
      res=os.popen('netsh wlan connect name='+'"'+preferred_ssid+'"').read() 
      print(res)
