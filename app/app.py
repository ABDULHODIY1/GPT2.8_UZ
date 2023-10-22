from aiogram import Dispatcher,executor,Bot,types
from pytube import YouTube
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API_TOKEN="6273869092:AAG-gm8D0ULD_Iq6GgmImn9xdkMh-JnM7MI"


bot=Bot(token=API_TOKEN, parse_mode="HTML")
dp=Dispatcher(bot, storage=MemoryStorage())

# dp=Dispatcher(bot)
# @dp.message_handler()
# async def echo(message: types.Message):
    # await message.answer(f"{message.text}")
async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
        ]
    )
@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer(text="salom o`zimni tanishtray men youtube dan video yuklab  beraman buning uchun menga videoni silkasini ulashing")

@dp.message_handler()
async def video(message: types.Message):
    await message.answer(text="iltimos biros kuting!!")
    if video == True:
        await message.delete()
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if url == "https://www.youtu.be" or "https://www.youtube.com/":
        await bot.send_message(chat_id,f'vedeo nomi:{yt.title}\n'
            f"{yt.views} video martta korildi")
        await dawnload_youtube_video(url,message,bot)

async def  dawnload_youtube_video(url,message,bot):
    yt=YouTube(url)
    stream = yt.streams.filter(progressive=True ,file_extension="mp4")
    stream.get_highest_resolution().download(f"{message.chat.id}",f"{message.chat.id}")
    with open(f"{message.chat.id}/{message.chat.id}",'rb') as video:
        await bot.send_video(message.chat.id, video, caption="video muvofaqiatli tarzda yuklandi!!", parse_mode="Markdown")
        os.remove(f"{message.chat.id}/{message.chat.id}")
async def on_startup(dispatcher):
    # komandalar
    await set_default_commands(dispatcher)
    # bot ishga tushdi yoki adminga habar
    # await on_startup_notify(dispatcher)

if __name__=="__main__":
    executor.start_polling(dp, on_startup=on_startup)
