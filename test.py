import time
import logging
import logging.handlers
import random

vector_host = 'vector-4cp6ed.bunnyenv.com:80'
vector_url = '/'
handler = logging.handlers.HTTPHandler(vector_host, vector_url, method='POST')

logger = logging.getLogger('example')
logger.addHandler(handler)
logger.setLevel(logging.INFO)
while True:
    messages = ['Error', 'Warning', 'Info']
    message = random.choice(messages)
    if message == 'Error':
        logger.error('This is an error log')
    elif message == 'Warning':
        logger.warning('This is a warning log')
    else:
        logger.info('This is an info log')
    time.sleep(3)
    print("next iteration")

