import time
from xmlrpc.client import ServerProxy

topic = ServerProxy("http://topic:8000")
topik_order = "order"
topik_payment = "payment"

for i in range(1, 100):
    event_order = f"OrderCreated-{i}"
    topic.terbitkan(topik_order, event_order)
    print(f"[PUBLISHER] [{topik_order}] Publikasi: {event_order}", flush=True)

    event_payment = f"PaymentRequested-{i}"
    topic.terbitkan(topik_payment, event_payment)
    print(f"[PUBLISHER] [{topik_payment}] Publikasi: {event_payment}", flush=True)

    time.sleep(2)