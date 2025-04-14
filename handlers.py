from aiogram import Router, F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
from cards import cards

router = Router()

@router.message(F.text.capitalize().in_(cards.keys()))
async def echo_card(msg: Message):
    key = msg.text.capitalize()
    # photo = FSInputFile(f"./img/{key}.png")
    # await msg.answer_photo(
    #     caption=f"*{key}*\n" + cards[key],
    #     parse_mode='Markdown',
    #     photo=photo
    # )

# TODO При вводе карты дать возможность задать вопрос (через FSM + redis)
# Вопрос и заготовка отправляется на API GigaChat -> Дается ответ из нейронки
# TODO Меченная ссылка

@router.message()
async def error(msg: Message):
    await msg.answer("Кажется, вы ввели что-то не то.\nПожалуйста, попробуйте ещё раз!")