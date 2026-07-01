from fastapi import FastAPI
from routes.news_routes import router
from routes.recommendation_routes import router as recommendation_router

app = FastAPI(
    title="Flash Feed AI Service"
)

app.include_router(
    router,
    prefix="/news",
    tags=["News"]
)
app.include_router(
    recommendation_router,
    prefix="/recommend",
    tags=["Recommendation"]
)