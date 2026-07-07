from apscheduler.schedulers.blocking import BlockingScheduler
from services.news_fetcher import fetch_news

scheduler = BlockingScheduler()

scheduler.add_job(
    fetch_news,
    "interval",
    minutes=30
)

print("Scheduler Started...")

scheduler.start()