from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq


router = Router()

#Команда начала работы с ботом и добавление пользователя в бд
@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в бота напоминалку!', reply_markup=kb.main)

#Команда на отображение помощи по боту
@router.message(F.text == 'Помощь')
async def help_me(message: Message):
    await message.answer('Данный бот обеспечивает напоминание о работе, каждый день в 10 утра. Для записи нажмите кнопку «Настройки бота».')

#Команда на выбор включения и выключения отправки уведомления
@router.message(F.text == 'Настройки бота')
async def settings(message: Message):
    await message.answer('Вот доступные настройки:', reply_markup=kb.catalog)

#Команда на включение отправки уведомления
@router.callback_query(F.data == 'turn_on')
async def turn_on(callback: CallbackQuery):
    await rq.set_yes(callback.from_user.id)
    await callback.answer('Вы изменили напоминание')
    await callback.message.answer('Вы включили напоминание')

#Команда на выключение отправки уведомления
@router.callback_query(F.data == 'turn_off')
async def turn_off(callback: CallbackQuery):
    await rq.set_not(callback.from_user.id)
    await callback.answer('Вы изменили напоминание')
    await callback.message.answer('Вы выключили напоминание')