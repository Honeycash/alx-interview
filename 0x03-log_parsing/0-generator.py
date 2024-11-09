#!/usr/bin/python3
'''A script that generates random HTTP request logs in a consistent format.'''

import random
import sys
import datetime
from time import sleep

for i in range(10000):
    sleep(random.random())
    log_line = "{:d}.{:d}.{:d}.{:d} - [{}] \"GET {} HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        datetime.datetime.now().strftime('%d/%b/%Y:%H:%M:%S -0000'),  # Updated date format
        '/projects/260',  # Updated path to match the parser's expected format
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    )
    sys.stdout.write(log_line)
    sys.stdout.flush()
