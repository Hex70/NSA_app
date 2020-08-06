from django.shortcuts import render


import os
from subprocess import run,PIPE,Popen


def index(request): 
    return render(request, 'pages/index.html')

def about(request): 
   ##  devic = devices.object.all()
     return render(request, 'pages/about.html') 

def external(request): 
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #out = run([sys.executable,os.path.join(BASE_DIR,'pyscripts\\netmiko1.py')],shell=True,stdout=PIPE)
    p = Popen(["python", os.path.join(BASE_DIR,'pyscripts\\netmiko1.py')], stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print(out)
    print(err)
    ##sys.executable,os.path.join(BASE_DIR,'pyscripts
    return render(request, 'pages/index.html',{'data1':out})