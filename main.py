import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State

state_storage = StateMemoryStorage()
# Вставить свой токет или оставить как есть, тогда мы создадим его сами
bot = telebot.TeleBot("6456510784:AAHnMRagp4oVkH0cDSDEORQ2Yietm8Lejgk",
                      state_storage=state_storage, parse_mode='Markdown')


class PollState(StatesGroup):
    name = State()
    age = State()


class HelpState(StatesGroup):
    wait_text = State()


text_poll = "Регистарция"  # Можно менять текст
text_button_1 = "Что такое умскул?"  # Можно менять текст
text_button_2 = "Виктория Ланская"  # Можно менять текст
text_button_3 = "Ссылки для подготовки к ЕГЭ"  # Можно менять текст
text_button_4 = "Артем Фролов"  # Можно менять текст
text_button_5 = "Дима Купер"  # Можно менять текст
text_button_6 = "Ссылки для подготовки к ОГЭ"  # Можно менять текст

menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_poll,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    ),
    telebot.types.KeyboardButton(
        text_button_3,
    )
)


@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'Привет, я бот Умскул! Хочешь записатья на крусы?',  # Можно менять текст
        reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_poll == message.text)
def first(message):
    bot.send_message(message.chat.id, 'Супер! Для начала давай познакомимся. Как тебя зовут?')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.name, message.chat.id)


@bot.message_handler(state=PollState.name)
def name(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    bot.send_message(message.chat.id, 'Очень приятно! В каком классе вы обучаетесь?')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.age, message.chat.id)


@bot.message_handler(state=PollState.age)
def age(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text
    bot.send_message(message.chat.id,
                     'Спасибо за регистрацию! Можете записаться на крусы прямо сейчас на [нашем сайте](https://umschool.net/)',
                     reply_markup=menu_keyboard)  # Можно менять текст
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Умскул — онлайн-школа подготовки к ЕГЭ И ОГЭ",
                     reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id,
                     "Готовит к ЕГЭ по информатике с 2018 года. *Сдала ЕГЭ по информатике на 100 баллов в 2018 и 2023 году*. *Выпустила 54 стобалльника*, _879 учеников сдали на 90+_. Выпускница КФУ ИТИС по направлению программная инженерия. Явялется *Django-разработчиком*. Покажет тебе, что информатика — это про возможности и творчество.",
                     reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id,
                     "[Telegram](https://t.me/infa_vikusya). [YouTube](https://www.youtube.com/@umsch_inf). [VK](https://vk.com/umsch_i)",
                     reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_4 == message.text)
def help_command(message):
    bot.send_message(message.chat.id,
                     "Преподет информатику с 2020 года. *Сдал ЕГЭ по информатике на 95 баллов*. _Подготовил 1206 учеников на 5_. Студент Мосполитеха на направлении «Информационные технологии». *Победитель* национальных соревнований профессионального мастерства по разработке _AR/VR приложений WorldSkills Russia, DigitalSkills Russia, хакатон VRARFest в Сколково_. Максимум визуализации и прикладных навыков, минимум зубрежки",
                     reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_5 == message.text)
def help_command(message):
    bot.send_message(message.chat.id,
                     "Преподет информатику с 2013 года. *Сдал ЕГЭ по информатике в 2021 на 95 баллов*. _Окончил МГГУ по специальности прикладная информатика в экономике с красным дипломом_. Действующий эксперт ОГЭ с 2019 года. Действующий школьный учитель первой категории. Преподаватель в университете МИСИС (2019-2023), готовил абитуриентов к ЕГЭ. Провел более 15 000 уроков",
                     reply_markup=menu_keyboard)  # Можно менять


@bot.message_handler(func=lambda message: text_button_6 == message.text)
def help_command(message):
    bot.send_message(message.chat.id,
                     "[Telegram](https://t.me/twocod). [YouTube](https://www.youtube.com/@umsch_i_oge). [VK](https://vk.com/umsch_i_oge)",
                     reply_markup=menu_keyboard)  # Можно менять текст


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()