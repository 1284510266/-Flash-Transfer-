import os
import shutil
from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import socket
from typing import List

app = FastAPI()

def get_local_ip():
    try:
        # Create a dummy socket to detect the preferred interface IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# In-memory clipboard
clipboard_content = "欢迎使用跨设备互传工具！"

class ClipboardUpdate(BaseModel):
    content: str

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    # Basic safety: limit filename length or characters if needed, but for local use it's fine
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "size": os.path.getsize(file_path)}

@app.get("/files")
async def list_files():
    files = []
    for filename in os.listdir(UPLOAD_DIR):
        path = os.path.join(UPLOAD_DIR, filename)
        if os.path.isfile(path):
            files.append({
                "name": filename,
                "size": os.path.getsize(path),
                "mtime": os.path.getmtime(path)
            })
    # Sort by mtime descending
    files.sort(key=lambda x: x['mtime'], reverse=True)
    return files

@app.get("/download/{filename}")
async def download_file(filename: str):
    path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path, filename=filename)

@app.delete("/files/{filename}")
async def delete_file(filename: str):
    path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(path):
        os.remove(path)
        return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="File not found")

@app.get("/info")
async def get_info():
    return {
        "local_ip": get_local_ip(),
        "port": 8000
    }
async def get_clipboard():
    return {"content": clipboard_content}

@app.post("/clipboard")
async def update_clipboard(data: ClipboardUpdate):
    global clipboard_content
    clipboard_content = data.content
    return {"message": "Updated"}

if __name__ == "__main__":
    # In a local network, 0.0.0.0 is needed for other devices to access
    uvicorn.run(app, host="0.0.0.0", port=8000)
