from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI(title="CBK Compliance Toolkit", version="1.0.0")

app.mount("/static", StaticFiles(directory="docs"), name="static")

@app.get("/")
async def root():
    with open("docs/index.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/health")
async def health():
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
