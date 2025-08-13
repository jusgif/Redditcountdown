import praw
from datetime import datetime, timezone
import os

# Target date for countdown
TARGET_DATE = datetime(2025, 11, 10, 0, 0, 0, tzinfo=timezone.utc)

# Reddit API credentials (from GitHub Secrets)
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Post ID from secrets
POST_ID = os.getenv("REDDIT_POST_ID")

def get_countdown():
    now = datetime.now(timezone.utc)
    delta = TARGET_DATE - now
    if delta.total_seconds() <= 0:
        return "**🎉 The day has arrived! 🎉**"
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"## ⏳ Countdown to November 10, 2025\n**{days} days, {hours} hours, {minutes} minutes left**"

post = reddit.submission(id=POST_ID)
post.edit(get_countdown())
print("✅ Countdown updated.")
