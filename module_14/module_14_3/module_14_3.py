from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import os

from course1.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()




def kb_menu():
    kb_list = [
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]
    ]
    kb = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return kb

def inline_menu():
    kb_list = [
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return kb

def inl_product():
    kb_list = [
        [
        InlineKeyboardButton(text='Product1', callback_data="product_buying"),
        InlineKeyboardButton(text='Product2', callback_data="product_buying"),
        InlineKeyboardButton(text='Product3', callback_data="product_buying"),
        InlineKeyboardButton(text='Product4', callback_data="product_buying")
         ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=kb_list)
    return kb



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_menu())



@dp.message_handler(text = 'Рассчитать')
async def menu_main(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_menu())


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.Message):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5',
                              reply_markup=inline_menu())




@dp.callback_query_handler(text='calories')
async def set_age(call: types.Message):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()

    age = float(data['first'])
    growth = float(data['second'])
    weight = float(data['third'])
    result = (age * 5) + (growth * 6.25) + (weight * 10) + 5

    await message.answer(f'Ваша (мужская) норма калорий: {result}')
    await state.finish()

@dp.message_handler(text='Информация')
async def info(message: types.Message):
    await message.answer('Информация о боте!')

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    files = os.listdir('filess')
    for n, file in enumerate(files, start=1):
        img = os.path.join('filess', file)
        list_ = (
            f'Название: Product{n} | '
            f'Описание: описание {n} | '
            f'Цена: {n * 100}\n\n'

        )
        with open(img, 'rb') as image:
            await message.answer_photo(photo=image, caption=list_)
    await message.answer('Выберите продукт для покупки:', reply_markup=inl_product())

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт', reply_markup=kb_menu())
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)