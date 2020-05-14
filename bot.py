import asyncio
import parser
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from loader import bot, storage
BOT_TOKEN="1243697551:AAEAzgjjGt3EynR2R9cgMdIWSTCPrOzF104"
import telebot
async def on_shutdown(dp):
    await bot.close()
    await storage.close()
from keyboards.default import menu
from handlers.users import menu
loop =asyncio.get_event_loop()
bot=Bot(BOT_TOKEN,parse_mode="HTML")
dp=Dispatcher(bot,loop=loop)
if __name__=="__main__":
    from handlers1 import dp,send_to_message
    executor.start_polling(dp,on_startup=send_to_message)
    from handlers.users import menu
    from aiogram import executor

    executor.start_polling(dp, on_shutdown=on_shutdown)

