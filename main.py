import os 
import asyncio
from telegram import Bot
from dotenv import load_dotenv 
from lc_api import get_leetcode_daily_question
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()

TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def send_telegram_message(): # async inherent for telegram bots, allows for "concurrency" of tasks (all things defined in the function / the function itself)
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    question = get_leetcode_daily_question()
    
    if question:
        message = (
            f"📌 *LeetCode Daily Challenge*\n\n"
            f"🔢 *ID:* {question['id']}\n"
            f"📌 *Title:* {question['title']}\n"
            f"⚡ *Difficulty:* {question['difficulty']}\n"
            f"🔗 [Solve here]({question['link']})"
        )
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode="Markdown")
    else:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Failed to fetch the daily question")

async def send_sanity_check_message():
    await send_telegram_message()

async def main(): # for just simple CRON jobs and no event listener, no need for application_BUILD
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_telegram_message, "cron", hour=9, minute=0)
    scheduler.start()

    while True:
        user_input = input("Enter command: ")
        if user_input.strip().lower() == "sanity":
            await send_sanity_check_message()
        elif user_input.strip().lower() == "exit":
            print("Stopping bot")
            scheduler.shutdown()
            break

if __name__ == "__main__":
    asyncio.run(main())