from fastapi import FastAPI

app = FastAPI(title="Story Roles")


@app.post("/files/process")
async def process_files():
    return {"message": "Files processed successfully"}
