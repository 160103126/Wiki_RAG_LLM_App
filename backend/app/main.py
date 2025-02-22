from fastapi import FastAPI
from app.routers import api_v1

app = FastAPI(title="Wiki RAG Assistant")
app.include_router(api_v1.router)



@app.get("/health")
async def health_check():
    return {"status": "healthy"}