# Deep-Freeze-Fucker
A program able to close and uninstall Deep Freeze from your computer

# How it works?
This programs uses subprocess to close deep freeze and delete the program folder

# Example
```
import subprocess
subprocess.call("TASKKILL /F /IM DFServ.exe /T")
