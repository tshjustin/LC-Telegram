import os 
from typing import Final 
from telegram import Update
from dotenv import load_dotenv 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    await update.message.reply_text("Let the Grind start :)") # /start

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    await update.message.reply_text("Provides Daily update at 08:30 SGD time for Daily Leetcode Problem") # /help


# Responses 
def handle_responses(text: str) -> str: 
    pass 