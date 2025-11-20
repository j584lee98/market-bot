from fastapi import FastAPI

app = FastAPI()

@app.get("/api/index")
def read_root():
    return {"message": "hello world"}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}