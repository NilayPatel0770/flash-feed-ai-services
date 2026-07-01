from fastapi import APIRouter, HTTPException
from services.recommendation_service import recommend_articles

router = APIRouter()


@router.get("/{article_id}")
def get_recommendations(article_id: str):

    try:

        recommendations = recommend_articles(article_id)

        return {
            "success": True,
            "count": len(recommendations),
            "recommendations": recommendations
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )