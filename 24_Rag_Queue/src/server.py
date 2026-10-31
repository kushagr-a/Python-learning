from fastapi import FastAPI, Query # type: ignore[reportMissingImports]

if __package__:
    from .client.rq_client import queue
    from .queue.worker import process_query
else:
    from client.rq_client import queue
    from queue.worker import process_query

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "Server is up and running!"}


@app.post("/chat")
def chat(
        query: str = Query(..., description="The query to process"),
):
    job = queue.enqueue(process_query, query)

    return { "status": "Query has been enqueued for processing.", "job_id": job.id }


@app.get("/result")
def get_result(
        job_id: str = Query(..., description="The ID of the job to retrieve the result for"),
):
    queued_job = queue.fetch_job(job_id)
    result = queued_job.result if queued_job else None
    return {"status": "Result retrieved.", "result": result}