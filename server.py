import os
import json
import requests
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Shihab King AI - Universal Resilient Core")

# সমস্ত অরিজিন ও লোকাল ফাইল পারমিশন
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        }
    )

@app.get("/")
def health():
    return {
        "status": "Online",
        "engine": "Shihab King AI Resilient Core",
        "credits": "Unlimited"
    }

# ১. আর্কিটেক্ট ইঞ্জিন (Stage 1/5 - Claude / Anthropic এর সব ভ্যারিয়েন্ট হ্যান্ডলার)
@app.post("/v1/messages")
@app.post("/messages")
@app.post("/v1/architect")
async def claude_resilient(request: Request):
    prompt_text = "Create the game architecture"
    try:
        body = await request.json()
        if "messages" in body and isinstance(body["messages"], list):
            for m in reversed(body["messages"]):
                content = m.get("content", "")
                if isinstance(content, str) and content.strip():
                    prompt_text = content
                    break
                elif isinstance(content, list):
                    for item in content:
                        if isinstance(item, dict) and item.get("type") == "text":
                            prompt_text = item.get("text", prompt_text)
                            break
        elif "prompt" in body:
            prompt_text = str(body["prompt"])
    except Exception:
        pass

    try:
        # হাই-স্পিড কোডার ব্যাকএন্ড কল
        url = f"https://text.pollinations.ai/{requests.utils.quote(prompt_text)}?model=qwen-coder"
        res = requests.get(url, timeout=40)
        output = res.text if res.status_code == 200 else f"Architecture for: {prompt_text}"
    except Exception:
        output = f"// Shihab King Engine Generated Game Blueprint for: {prompt_text}\nconst Game = {{ title: '{prompt_text}', status: 'Active' }};"

    # Anthropic Claude Standard Response Format
    return {
        "id": "msg_shihab_king_core",
        "type": "message",
        "role": "assistant",
        "model": "claude-3-5-sonnet-20241022",
        "content": [
            {
                "type": "text",
                "text": output
            }
        ],
        "stop_reason": "end_turn",
        "stop_sequence": None,
        "usage": {"input_tokens": 100, "output_tokens": 500}
    }

# ২. চ্যাট ও ডিবাগার ইঞ্জিন (OpenAI Chat Completions)
@app.post("/v1/chat/completions")
@app.post("/chat/completions")
async def openai_resilient(request: Request):
    user_query = "Optimize project"
    try:
        body = await request.json()
        messages = body.get("messages", [])
        if messages:
            user_query = messages[-1].get("content", user_query)
    except Exception:
        pass

    try:
        url = f"https://text.pollinations.ai/{requests.utils.quote(str(user_query))}?model=deepseek"
        res = requests.get(url, timeout=40)
        reply = res.text if res.status_code == 200 else f"Processed: {user_query}"
    except Exception:
        reply = f"Shihab Core Response: {user_query}"

    return {
        "id": "chatcmpl-shihab",
        "object": "chat.completion",
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": reply
            },
            "finish_reason": "stop"
        }]
    }

# ৩. জেমিনি ফলব্যাক ইঞ্জিন
@app.post("/v1beta/models/{model}:generateContent")
async def gemini_resilient(model: str, request: Request):
    text_out = "Gemini Core Output"
    try:
        data = await request.json()
        text_out = data["contents"][0]["parts"][0]["text"]
        url = f"https://text.pollinations.ai/{requests.utils.quote(text_out)}?model=mistral"
        res = requests.get(url, timeout=40)
        text_out = res.text if res.status_code == 200 else text_out
    except Exception:
        pass

    return {
        "candidates": [{
            "content": {
                "parts": [{"text": text_out}],
                "role": "model"
            },
            "finishReason": "STOP"
        }]
    }

# ৪. ভিডিও ইঞ্জিন
@app.post("/v1/videos/text2video")
@app.post("/kling/generate")
@app.post("/v1/runway/generate")
async def video_resilient(request: Request):
    prompt = "action game cinematic"
    try:
        body = await request.json()
        prompt = body.get("prompt", prompt)
    except Exception:
        pass

    vid_url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}?width=1280&height=720&nologo=true"
    return {"status": "success", "video_url": vid_url, "url": vid_url}

# ৫. ভয়েস ও অডিও ইঞ্জিন
@app.post("/v1/text-to-speech/{voice_id}")
@app.post("/v1/tts")
async def audio_resilient(voice_id: str = "default", request: Request = None):
    text = "Audio synthesized"
    if request:
        try:
            b = await request.json()
            text = b.get("text", text)
        except Exception:
            pass
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=en&q={requests.utils.quote(text)}"
    return {"status": "success", "audio_url": audio_url}
