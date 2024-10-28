from fastapi import APIRouter, status, Body

from app.utils.chat_endpoint import get_summary

router = APIRouter(prefix="/summary", tags=["summary"])

@router.post("/get_summary", status_code=status.HTTP_201_CREATED)
async def chat_llm_endpoint(blog_url: str = Body(...)):
    return await get_summary(blog_url=blog_url)