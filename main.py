import time
import subprocess
import concurrent.futures


def ping(pingable_host, size, time_intervall_between_pings, ping_count):
    command = [
        'ping',
        '-q'
        '-c', str(ping_count),
        # '-s', str(size), todo
        # '-i', time_intervall_between_pings,
        pingable_host
    ]
    return subprocess.call(command)


host = "google.com"
ping_count = 4
threads = 50
size = 200
time_intervall_between_pings = 100

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    for _ in range(threads):
        executor.submit(ping, host, size, time_intervall_between_pings, ping_count)

end = time.perf_counter()

print("DURATION:", round(end - start, 4), "second(s)")
