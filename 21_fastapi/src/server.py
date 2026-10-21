from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(
    host="http://localhost:11434",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/contactMe")
def contact_me():
    return {"message": "You can contact me at: kushagra@email.com"}

@app.post("/chat")
def chat(
    message: str = Body(..., description="The message to send to the Ollama model")
):
    response = client.chat(
        model="qwen2.5:1.5b",
        messages=[{"role": "user", "content": message}],
    )
    return {"response": response.message.content}
