from src import scheduler
from src.models import User
from src.email_utils import send_email
import openai
import os

def generate_news_brief(topics):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    prompt = f"Generate a brief summary of the latest world news for the following topics: {topics}."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error generating news: {e}"

def send_daily_briefs(app):
    with app.app_context():
        users = User.query.all()
        for user in users:
            if user.topics:
                news_brief = generate_news_brief(user.topics)
                subject = "Your Daily News Brief"
                send_email(subject, user.email, news_brief)

def start_scheduler(app):
    scheduler.add_job(
        func=lambda: send_daily_briefs(app),
        trigger='interval',
        days=1,
        id='daily_brief'
    )
    scheduler.start()
