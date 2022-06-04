
import subprocess
import platform
import threading

def ping(host="google.com"):
    param = '-n' if platform.system().lower() == "windows" else '-c'
    command = ['ping', '-c', '10', host]
    return subprocess.call(command)


host = "google.com"

for _ in range(10):
    t = threading.Thread(target=ping, args=[host])
    t.start()

