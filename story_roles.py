import os
from fastapi import FastAPI
from TTS.api import TTS
from datetime import datetime
from s3_client import S3Client
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Story Roles")
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
s3_client = S3Client()


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/files/process")
async def process_files():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    output_path = f"output_{timestamp}.wav"
    text = "Hello, this is a test message from Story Roles text to speech system."
    
    tts.tts_to_file(text=text, file_path=output_path)
    
    bucket_name = os.getenv('S3_BUCKET_NAME')
    s3_url = s3_client.upload_file(output_path, bucket_name)
    
    return {"message": "Files processed successfully", "audio_file": output_path, "s3_url": s3_url}
