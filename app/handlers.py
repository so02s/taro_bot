from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
from cards import cards

router = Router()

@router.message(F.text.capitalize().in_(cards.keys()))
async def echo_card(msg: Message):
    key = msg.text.capitalize()
    photo = FSInputFile(f"./img/{key}.png")
    await msg.answer_photo(
        caption=f"*{key}*\n" + cards[key],
        parse_mode='Markdown',
        photo=photo
    )

@router.message(CommandStart())
async def start(msg: Message):
    await msg.answer("Привет! Я могу раскрыть вашу судьбу\nВсе, что нужно сделать - ввести название карты, что вам выпала")

@router.message()
async def error(msg: Message):
    await msg.answer("Кажется, вы ввели что-то не то.\nПожалуйста, попробуйте ещё раз!")