
import subprocess
import platform

def ping(host):
    param = '-n' if platform.system().lower() == "windows" else '-c'
    command = ['ping', '-c', '10', host]
    return subprocess.call(command)


host = "google.com"
print(ping(host))

