from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from scripts.price_script import price
from aiogram.enums import ParseMode

router = Router()

@router.callback_query(F.data == "delete")
async def test_call(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await callback_query.answer()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text="HELLO!")

@router.message(Command(commands='price'))
async def price_command(message: Message):
    btn = InlineKeyboardButton(text="Delete", callback_data="delete")
    kb = InlineKeyboardMarkup(inline_keyboard=[[btn]])
    price_text = price(message.text[6:])

    await message.reply(text=price_text,  parse_mode=ParseMode.HTML, reply_markup=kb)