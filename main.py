import os 
import asyncio
from telegram import Bot
from dotenv import load_dotenv 
from lc_api import get_leetcode_daily_question
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()

TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_BOT_USERNAME = os.getenv("TELEGRAM_BOT_USERNAME")

async def send_telegram_message():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    question = get_leetcode_daily_question()
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=question, parse_mode="Markdown")

def schedule_daily_message():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_telegram_message, "cron", hour=9, minute=0)
    scheduler.start()

if __name__ == "__main__":
    
    schedule_daily_message()

    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")