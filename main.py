import asyncio
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.handlers import router
from app.database.models import async_main

import app.database.requests as rq


bot = Bot(token='7902075760:AAH4Vg-dfNEqqmwd_jTx_vk5HgXeMDhoG9Q')

#Функция отправки сообщения пользователям полученных с базы данных
async def send_message():
    id_users_list = await rq.get_tg_ids()
    for id_user in id_users_list:
        await bot.send_message(chat_id=id_user, text="Пора на работу!")

#Запуск программы, запуск бота, запуск планировщика для отправки сообщений каждый день в 10 утра
async def main():
    await async_main()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_message, CronTrigger(hour=10, minute=00))
    scheduler.start()
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

#Поимка ошибки для отображения, когда бот отключается
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')