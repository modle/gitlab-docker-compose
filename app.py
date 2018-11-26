import time

import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/trigger', methods=['POST'])
def triggered():
    message = "triggered the post endpoint\n"
    print(message)
    return message


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello from Docker, yo! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
