from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)

#Создание клавиатуры для помощи и настройки 
main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Помощь'),
                                      KeyboardButton(text='Настройки бота')]],
                            resize_keyboard=True)

#Создание клавиатуры для настроек бота 
catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Включить напоминание на 10 утра', callback_data = 'turn_on')],
    [InlineKeyboardButton(text='Выключить напоминание', callback_data = 'turn_off')]])