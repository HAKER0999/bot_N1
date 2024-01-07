from telebot import types



def phone_number():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phone_number = types.KeyboardButton(text="Kontaktingizni yuboring!", request_contact=True)
    keyboard.row(phone_number)
    return keyboard


def monitors():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    laptops = types.KeyboardButton(text="Noutbuklar💻")
    phons = types.KeyboardButton(text="Telefonlar📱")
    monitors = types.KeyboardButton(text="Monitorlar🖥")
    ofisniy_acsesuars = types.KeyboardButton(text="Ofis jihozlari🖨")
    acsesuars = types.KeyboardButton(text="Aksesuarlar📲")
    kompyuter_acsesuars = types.KeyboardButton(text="ORQAGA🔙")
    keyboard.row(laptops, monitors)
    keyboard.row(ofisniy_acsesuars, phons )
    keyboard.row(acsesuars, kompyuter_acsesuars)
    return keyboard

def payment(url):
    keyboard = types.InlineKeyboardMarkup()
    btn_payment = types.InlineKeyboardButton(text="Tolov!", url=url)
    keyboard.row(btn_payment)
    return keyboard



