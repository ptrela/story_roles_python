from fastapi import FastAPI

app = FastAPI(title="Story Roles")


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/files/process")
async def process_files():
    return {"message": "Files processed successfully"}
