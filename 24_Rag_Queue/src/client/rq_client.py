# this file is used for basic rq connections

from redis import Redis # type: ignore
from rq import Queue # type: ignore

queue = Queue(
    connection=Redis(
        host  = "localhost",
        port  = 6379,
    )
)