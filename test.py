import time
import logging
import logging.handlers
import random

from urllib.parse import unquote_plus

vector_host = 'vector-xl4avw.bunnyenv.com'
vector_url = '/'
handler = logging.handlers.HTTPHandler(vector_host, vector_url, method='POST', secure=True)

# Set the Content-Type header to text/plain
handler.setFormatter(logging.Formatter('%(message)s'))
handler.addFilter(lambda record: not record.args)

logging.basicConfig(encoding="utf-8", level=logging.INFO, handlers=[handler])

while True:
    logging.info(f'This is a random log message: {random.randint(1, 100)}')
    time.sleep(1)
