# Deep-Freeze-Fucker
A program able to close and uninstall Deep Freeze from your computer

# How it works?
This programs uses subprocess to close deep freeze and delete the program folder
# Before Using the program
You need to install upx to use the build.py
You need to execute build.py and next, execute your executable file inside of dist folder

# Example
```
import subprocess
subprocess.call("TASKKILL /F /IM DFServ.exe /T")
