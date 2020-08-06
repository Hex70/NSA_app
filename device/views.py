from django.shortcuts import render,redirect
from django.db import models
from .models import Device
# Create your views here.
def index(request): 
    av = 'active'

         # new info here
  #  return render(request, 'pages/index.html', context,contextp)


    
    dev = Device.objects.all()




    return render(request, 'device/Managedevices.html', {'dev': dev, 'av': av} )

def add_device(request): 
    return render(request, 'device/add_device.html')
def add_deviceclick(request): 
  
    dv = Device(  IP_address= request.POST.get("ip_address"),
                    username= request.POST.get("ip_address"),
                   Password = request.POST.get("password"),
    
                    )
    dv.save()
   
    #print(ip_address)
 
   # return render(request, 'device/add_device.html',contxet)
    return redirect('/device/')



def deleteDevice(request,device_id): 
    devdel = Device.objects.get(id=device_id)
    
 #  if request.method == "POST":
    if request.method == "POST" :
        
        devdel.delete()
        return redirect('/device/')

    context = {'item':devdel}

    return render(request, 'device/delete.html', context)


#def deleteDevice(request, device_id):

#dev
	#devdel = Devices.objects.get(id=device_id)

#	if request.method == "POST":
#		devdel.delete()
#		return redirect('/devices/')

#	context = {'item':devdel}
#	device_ids=1
#    return render(request, 'devices/delete.html')
 

def Analyse(request,device_id): 
        
    from netmiko import ConnectHandler
    from netmiko.ssh_exception import NetMikoTimeoutException
    from paramiko.ssh_exception import SSHException
    from netmiko.ssh_exception import AuthenticationException
    import time
    import datetime
    import os
   
    
    NET_TEXTFSM = '/home/hex70/Downloads/TEXTFSM/ntc-templates/templates'
    analysedev = Device.objects.get(id=device_id)

    TNOW = datetime.datetime.now().replace(microsecond=0)

    IP_LIST = [analysedev.IP_address]

    for IP in IP_LIST:
        print ('\n  '+ IP.strip() + ' \n' )
        RTR = {
        'ip':   '192.168.43.140',
        'username': 'hex70',
        'password': 'seddikpain',
        'device_type': 'cisco_ios',
        }

        try:
            net_connect = ConnectHandler(**RTR)
        except NetMikoTimeoutException:
            print ('Device not reachable.')
            continue
        except AuthenticationException:
            print ('Authentication Failure.')
            continue
        except SSHException:
            print ('Make sure SSH is enabled in device.')
            continue

    output = net_connect.send_command('show version')
   # ihostname = [i['hostname'] for i in output ]
   # analysedev.hostname = ihostname
  #  analysedev.save()

    return redirect('/device/')