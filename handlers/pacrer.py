from aiogram import Router,F,Bot
from aiogram.types import Message
from filters.main_filter import Key_words
import logging

log = logging.getLogger(__name__)

router = Router()

@router.message(F.chat.id == -5183894278,Key_words(["цена"]))
async def check_data(message:Message,bot:Bot):
    username = message.from_user.username
    data = message.text
    await bot.send_message(chat_id = 8223796770,text = f'{username} Написал сообщение:"{data}"')
    log.info("Сообщение от %s было отправлено администратору",username)