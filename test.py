import time
import logging
import logging.handlers
import random

vector_host = 'vector-xl4avw.bunnyenv.com'
vector_url = '/'
handler = logging.handlers.HTTPHandler(vector_host, vector_url, method='POST', secure=True)

logging.basicConfig(encoding="utf-8", level=logging.INFO, handlers=[handler])

while True:
    logging.info(f'This is a random log message: {random.randint(1, 100)}')
    time.sleep(1)
