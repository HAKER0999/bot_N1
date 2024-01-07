import telebot
from keyboard import monitors
from parsing_noutbuks import noutbuklar
from keyboard import phone_number, payment
from parsing import data_Base
from parsing_ofis import ofis
from parsing_phons import phone
from parsing_acsesuar import acses

token = "6501643022:AAEaB-d1OifsPIOrBSFO6oFaCi9XePa9X18"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_id = message.from_user.id
    username = message.from_user.username
    bot.send_message(chat_id, f"SALOM🤚🤚 {first_name} botdan foydalanish uchun kontaktingizni yuboring!!!",reply_markup=phone_number())
    bot.register_next_step_handler(message, get_phone_number)

def get_phone_number(message):
    chat_id = message.chat.id
    phone_number = message.contact.phone_number
    bot.send_message(chat_id, f"Sizning raqaningiz: {phone_number}\n, Quyidagilardan birini tanlang!!!"
                              , reply_markup=monitors())
    bot.register_next_step_handler(message, laptop)

def laptop(message):
    chat_id = message.chat.id
    if message.text == "Noutbuklar💻":

        for note in noutbuklar:
            product_name = note["Product_name"]
            product_price = note["Product_price"]
            product_image = note["Product_image"]
            bot.send_photo(chat_id, product_image, caption=f"Mahsulot nomi: {product_name}\nNarxi: {product_price}",
                reply_markup=payment("https://ultrashop.uz/ru/store/noutbuki"))


    elif message.text == "Monitorlar🖥":
        for moni in data_Base :
            product_name = moni["Product_name"]
            product_price = moni["Product_price"]
            product_image = moni["Product_image"]
            bot.send_photo(chat_id, product_image, caption=f"Mahsulot nomi: {product_name}\nNarxi: {product_price}",
                reply_markup=payment("https://ultrashop.uz/ru/store/monitory"))



    elif message.text == "Ofis jihozlari🖨":
        for printer in ofis:
            product_name = printer["Product_name"]
            product_price = printer["Product_price"]
            product_image = printer["Product_image"]
            bot.send_photo(chat_id, product_image, caption=f"Mahsulot nomi: {product_name}\nNarxi: {product_price}",
                reply_markup=payment("https://ultrashop.uz/ru/store/pechatnaya-tehnika"))


    elif message.text == "Telefonlar📱":
        for c in phone:
            product_name = c["Product_name"]
            product_price = c["Product_price"]
            product_image = c["Product_image"]
            bot.send_photo(chat_id, product_image, caption=f"Mahsulot nomi: {product_name}\nNarxi: {product_price}",
                reply_markup=payment("https://ultrashop.uz/ru/store/pechatnaya-tehnika"))



    elif message.text == "Aksesuarlar📲":
        for ac in acses:
            product_name = ac["Product_name"]
            product_price = ac["Product_price"]
            product_image = ac["Product_image"]
            bot.send_photo(chat_id, product_image, caption=f"Mahsulot nomi: {product_name}\nNarxi: {product_price}",
                reply_markup=payment("https://ultrashop.uz/ru/store/aksessuary"))



    bot.send_message(chat_id, f"Quyidagilardan birini tanlang!!!"
                     , reply_markup=monitors())
    bot.register_next_step_handler(message, laptop)



bot.polling(none_stop=True)