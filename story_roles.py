from fastapi import FastAPI
from TTS.api import TTS

app = FastAPI(title="Story Roles")
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/files/process")
async def process_files():
    output_path = "output.wav"
    text = "Hello, this is a test message from Story Roles text to speech system."
    tts.tts_to_file(text=text, file_path=output_path)
    return {"message": "Files processed successfully", "audio_file": output_path}
