from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import traceback

from services.personalized_recommendation import (
    personalized_recommendations
)

router = APIRouter()


class EmbeddingRequest(BaseModel):
    embedding: list[float]


@router.post("/personalized")
def recommend(request: EmbeddingRequest):

    try:

        recommendations = personalized_recommendations(
            request.embedding
        )

        return {
            "success": True,
            "count": len(recommendations),
            "recommendations": recommendations
        }

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )