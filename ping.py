import time
import subprocess
import concurrent.futures
import argparse

parser = argparse.ArgumentParser(description='Use ping in multiple threads')
parser.add_argument('-q', default=True,
                    help='quiet')
parser.add_argument('-t', default=12,
                    help='threads')
parser.add_argument('--host', default='google.com',
                    help='quiet')
parser.add_argument('-c', default="5",
                    help='ping count')
parser.add_argument('-i', default="0,2",
                    help='time intervall between pings')
args = parser.parse_args()


host = args.host
ping_count = args.c
threads = args.t
time_intervall_between_pings = args.i
quiet = args.q


def ping(host, time_intervall_between_pings, ping_count, quiet):

    options = []

    if quiet:
        options.append("-q")
    if time_intervall_between_pings:
        options.append("-i")
        options.append(str(time_intervall_between_pings))
    if ping_count:
        options.append("-c")
        options.append(str(ping_count))

    command = ['ping']
    command+=options
    command.append(host)
    print(command)

    return subprocess.call(command)


start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    for _ in range(threads):
        executor.submit(ping, host, time_intervall_between_pings, ping_count, quiet)

end = time.perf_counter()

print("PING COUNT:", int(threads)*int(ping_count))
print("DURATION:", round(end - start, 4), "second(s)")
