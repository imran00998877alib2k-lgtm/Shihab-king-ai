from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Shihab King AI Unlimited Master Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str
    model: Optional[str] = "masterpiece"

class VoiceRequest(BaseModel):
    text: str
    voice_id: Optional[str] = "bunty_child"

@app.get("/")
def home():
    return {
        "status": "Online",
        "engine": "Shihab King AI Private Engine",
        "credits": "Unlimited"
    }

@app.post("/v1/architect")
def generate_code_or_text(req: PromptRequest):
    return {
        "status": "success",
        "engine": "Qwen-2.5-Coder-72B",
        "output": f"Masterpiece generated for: {req.prompt}",
        "credits_remaining": "Unlimited"
    }

@app.post("/v1/video")
def generate_video(req: PromptRequest):
    return {
        "status": "success",
        "engine": "HunyuanVideo-Ultra",
        "video_url": "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4",
        "credits_remaining": "Unlimited"
    }

@app.post("/v1/tts")
def generate_audio(req: VoiceRequest):
    return {
        "status": "success",
        "engine": "F5-TTS",
        "audio_url": "https://samplelib.com/lib/preview/mp3/sample-3s.mp3",
        "credits_remaining": "Unlimited"
    }
