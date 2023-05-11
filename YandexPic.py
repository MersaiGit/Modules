# meta developer: @Mersai
from telethon.tl.types import Message
from .. import loader, utils

@loader.tds
class YandexPic(loader.Module):
    """Ищет картинку из Яндекса по вашему запросу."""

    strings = {"name": "YandexPic"}

    @loader.unrestricted
    async def yanscmd(self, message: Message):
        """запрос"""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit("<emoji document_id=5237993272109967450>❌</emoji> Не указан запрос")
            return
        text_with_plus = text.replace(" ", "+")
        await self.inline.form(
            message=message,
            text=f" <emoji document_id=5188217332748527444>🔍</emoji> Ваше фото по запросу \"{text}\" найдено",
            reply_markup=[
                [
                    {
                        "text": "Ссылка на фото",
                        "url": f"https://yandex.uz/images/touch/search/?text={text_with_plus}",
                    }
                ],
                [{"text": "Close", "action": "close"}],
            ],
            **({"photo": f"https://yandex.uz/images/touch/search/?text={text_with_plus}"}),
        )