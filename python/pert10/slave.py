import os, time, threading
from datetime import datetime
from xmlrpc.server import SimpleXMLRPCServer

offset = float(os.getenv("OFFSET", "0"))

def now():
    return time.time() + offset

def adjust(delta):
    global offset
    offset += delta
    print(f"\nkoreksi {delta:+.1f} s")
    return True

server = SimpleXMLRPCServer(("0.0.0.0", 5000), logRequests=False)
server.register_function(now)
server.register_function(adjust)
threading.Thread(target=server.serve_forever, daemon=True).start()

while True:
    print("Jam Sekarang:", datetime.fromtimestamp(now()).strftime("%H:%M:%S"), end="\r", flush=True)
    time.sleep(1)