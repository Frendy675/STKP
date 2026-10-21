import os, time, threading
from datetime import datetime
from xmlrpc.client import ServerProxy

offset = float(os.getenv("OFFSET", "0"))
SLAVES = ["presentation", "application"]   # nama container slave


def now():
    return time.time() + offset


def sync():
    global offset
    time.sleep(5)
    node = {n: ServerProxy(f"http://{n}:5000") for n in SLAVES}
    while True:
        diff = {n: p.now() - now() for n, p in node.items()}   # selisih vs master
        diff["master"] = 0.0
        avg = sum(diff.values()) / len(diff)
        print(f"\nselisih: { {n: round(d, 1) for n, d in diff.items()} } | rata-rata: {avg:+.1f} s")
        offset += avg                                          # koreksi master
        for n, p in node.items():
            p.adjust(avg - diff[n])                            # kirim koreksi slave
        time.sleep(15)


threading.Thread(target=sync, daemon=True).start()

while True:
    print("Jam Sekarang:", datetime.fromtimestamp(now()).strftime("%H:%M:%S"), end="\r", flush=True)
    time.sleep(1)