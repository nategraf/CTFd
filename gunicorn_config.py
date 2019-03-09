import multiprocessing
import os
import base64

# http://docs.gunicorn.org/en/stable/settings.html
# https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py

bind='0.0.0.0:8000'

# Worker settings
worker_class=os.environ.get('WORKER_CLASS', 'geventwebsocket.gunicorn.workers.GeventWebSocketWorker')
worker=int(os.environ.get('WORKERS', 2*multiprocessing.cpu_count()))

# Logging settings
loglevel='info'
log_folder = os.environ['LOG_FOLDER']
accesslog=os.environ.get('ACCESS_LOG', '-')
errorlog=os.environ.get('ERROR_LOG', '-')

if not os.environ.get('USE_RELOAD') or os.environ.get('USE_RELOAD').lower() == 'true':
    # Reload on code changes. Useful for development
    reload=True
    # poll consumes more resources than inotify, but is more compatible
    reload_engine='poll'

# TLS / SSL
# Check out Let's Encrypt for free certificates https://letsencrypt.org/
if os.environ.get('TLS_KEY') and os.environ.get('TLS_CERT'):
    keyfile=os.path.join(os.environ.get('TLS_KEY'))
    certfile=os.path.join(os.environ.get('TLS_CERT'))
