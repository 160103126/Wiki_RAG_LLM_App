from fastapi import FastAPI
from app.routers import api_v1
import os
from dotenv import load_dotenv
from functools import lru_cache
import uvicorn

load_dotenv()



app = FastAPI(title="Wiki RAG Assistant")
app.include_router(api_v1.router)

@lru_cache(maxsize=1)
def get_env_var(key: str, default=None):
    """Fetches and caches environment variables."""
    return os.getenv(key, default)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@lru_cache()
def run_server():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



if __name__=='__main__':
    run_server()