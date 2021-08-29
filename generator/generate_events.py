import time
import random
import threading

import requests

def run():
    while True:
        try:
            requests.get("http://0.0.0.0:23333/info/load")
            requests.get("http://0.0.0.0:23333/info/uptime")

        except:
            pass


if __name__ == '__main__':
    for _ in range(4):
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

    while True:
        time.sleep(1)
