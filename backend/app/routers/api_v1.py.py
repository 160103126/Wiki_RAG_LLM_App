from fastapi import APIRouter, Depends
from app.services.rag import RAGService
from app.schemas.requests import QuestionRequest
from app.database.session import get_db
from sqlmodel import Session
from datetime import date

router = APIRouter(prefix="/api/v1", tags=["v1"])

@router.post("/ask")
async def ask_question(
    request: QuestionRequest, 
    db: Session = Depends(get_db)
):
    rag = RAGService("your-hf-token")  # In practice, use settings.HF_API_TOKEN
    context = rag.get_wiki_content(request.question)
    answer = rag.generate_answer(context, request.question)
    
    return {
        "question": request.question,
        "answer": answer,
        "sources": [request.question]
    }

@router.get("/retreive_data")
async def ask_question(
    start_date: date, 
    end_time:date,
    db: Session = Depends(get_db)
):
    return None