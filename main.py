import telebot
import moviepy.editor as mp
import os
import time

bot = telebot.TeleBot('TOKEN')
@bot.message_handler(commands=['start'])
def start(message):
    user = str(message.from_user.first_name)
    if (message.from_user.language_code == "ar"):
        bot.send_message(message.chat.id, f"مرحبا '{user}' في البوت الخاص بي❤️💬")
        bot.send_message(message.chat.id, f"أرسل لي مقطع فيديو وسوف أقوم بتحويله الى مقطع صوت")
        return

    bot.send_message(message.chat.id, f"Welcome '{user}' to my bot❤️💬")
    bot.send_message(message.chat.id, "Send me any video and i will convert it to mp3")


@bot.message_handler(content_types=['video'])
def handle_users(message):
    if message.from_user.language_code == "ar":
        mes = bot.send_message(message.chat.id, "انتظر من فضلك....")
    else:
        mes = bot.send_message(message.chat.id, "Wait ,please...")
    namev = str(time.time()) + ".mp4"
    names = str(time.time()) + ".mp3"

    try:
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f"{namev}", 'wb') as new_file:
            new_file.write(downloaded_file)
        video = mp.VideoFileClip(namev)
        video.audio.write_audiofile(names)
        vid2 = open(names, "rb")
        bot.delete_message(message.from_user.id, mes.id)
        bot.send_audio(message.chat.id, vid2)
    except Exception as e:
        bot.send_message(message.chat.id, "Error!: " + str(e))
    finally:
        os.remove(names)
        os.remove(namev)
bot.infinity_polling()