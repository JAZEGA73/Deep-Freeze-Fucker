import subprocess

path = "C:\Program Files (x86)/Faronics"

subprocess.call("TASKKILL /F /IM DFServ.exe /T")
subprocess.call("TASKKILL /F /IM DFLocker64.exe /T")
subprocess.call("TASKKILL /F /IM FrzState2k.exe /T")
subprocess.call("del ")
