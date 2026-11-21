from fastapi import FastAPI

app = FastAPI(title="Ask Your Data")


@app.get("/health")
def health():
    """Simple check that the server is running."""
    return {"status": "ok"}