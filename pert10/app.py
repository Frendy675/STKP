import datetime
import time
import os

offset = int(os.getenv("OFFSET", "0"))

try:
    while True:
        waktu_sekarang = (
            datetime.datetime.now()
            + datetime.timedelta(seconds=offset)
        ).strftime("%H:%M:%S")

        print(f"Jam Sekarang: {waktu_sekarang}", end="\r", flush=True)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nJam dihentikan.")
