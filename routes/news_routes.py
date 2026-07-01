from fastapi import APIRouter
from services.rss_service import fetch_rss_news

router = APIRouter()

@router.get("/rss")
def rss_news():

    result = fetch_rss_news()

    return {
        "success": True,
        "data": result
    }