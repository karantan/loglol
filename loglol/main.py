"""
If you just want a simple logging for your local script then replace
`TimedRotatingFileHandler` with `logging.FileHandler(LOGFILE)` otherwise just use
`TimedRotatingFileHandler`.

You also usually want to have `utc=True` because you don't know where are your servers
located.

When setting up TimedRotatingFileHandler you need to specify `when` and `interval`.

Example: `when="M", interval=30` -> this will rotate every 30 minutes.
"""

from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


import logging

LOGFILE = Path("loglol.log")


logger = logging.getLogger(__file__)
logging.basicConfig(
    level=logging.INFO,
    format="%(threadName)s %(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        TimedRotatingFileHandler(
            LOGFILE, when="D", interval=1, backupCount=7, utc=True
        ),
    ],
)


def test():
    return huh() + asd()


logger.info("hello world")

# Use logging.exception from within the except: handler/block to log the current
# exception along with the trace information,
try:
    test()
except Exception as err:
    logger.exception(err)

# Or use `exc_info=True` to get the full traceback
try:
    test()
except Exception as err:
    logger.error(err, exc_info=True)
