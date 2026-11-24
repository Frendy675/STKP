import time
from xmlrpc.client import ServerProxy

topic = ServerProxy("http://topic:8000")
nama_topik = "order"

while True:
    event = topic.tarik(nama_topik)
    if event:
        print(f"[SUBSCRIBER] [{nama_topik}] Terima: {event}", flush=True)
    time.sleep(1)