# Импорт библиотек
import logging  # Логгирование
import os
from aiogram import Bot, Dispatcher  #
from aiogram.types import Message  #
from aiogram.filters.command import Command  #

# 2. Инициализация объекта
# Подключаем бота
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
# Включаем логгирование
logging.basicConfig(level=logging.INFO)
# 3. Обработка команды старт
@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Введи свои фамилию, имя и отчество для транслитерации:'
    logging.info(f'{user_name} {user_id} - запустил бота')
    await bot.send_message(chat_id=user_id, text=text)
    # await bot.send_message(chat_id=admin, text=text)

# 4. Обработка всех сообщений
@dp.message()
async def send_echo(message: Message):
    DICTIONARY = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I',
                  'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
                  'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y', 'Ъ': 'IE',
                  'Э': 'E', 'Ю': 'IU', 'Я': 'IA', ' ': ' '}

    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    trans_text = ''
    for letter in text.upper():
        trans_text += DICTIONARY.get(letter, letter)
    logging.info(f'{user_name} {user_id} - отправил сообщение: {text}')
    await message.answer(text=trans_text)

# 5. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)

