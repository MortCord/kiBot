import datetime
from datetime import timedelta, datetime

import pandas as pd
from aiogram import Bot, executor, Dispatcher
from aiogram import types
from aiogram.utils.exceptions import (MessageCantBeDeleted,
                                      MessageToDeleteNotFound)

bot = Bot(token="5654399576:AAH-g2j853q8fAoGIUiWHrdiUmlqJScVmtk")
dp = Dispatcher(bot)
isTrue = True
week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
now = datetime.now()
day = week_days[now.weekday()]
maini = 0
users = {}






# week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
# now = datetime.datetime.now()
# day = week_days[now.weekday()]
# print(now)
# match day:
#     case 'Thursday':
#         bot.send_message(chat_id=message.chat.id, text="Write an integer")
#     case other:
#         print("Сьогодні вихідний пар немає")

@dp.message_handler(commands = ['para'])
async def new_timer_message(message: types.Message):
        week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        now = datetime.now()
        day = week_days[now.weekday()]
        # match day:
        #         case 'Monday':
        #             await bot.send_message(chat_id=message.chat.id, text="1.Гр.Осв. - 202 || 8:30 - 9:20")
        #             await bot.send_message(chat_id=message.chat.id, text="2.Матем. - 307 ||  9:30 - 10:20")
        #             await bot.send_message(chat_id=message.chat.id, text="3.Інф. - 311/304 || 10:40 - 11:30")
        #             await bot.send_message(chat_id=message.chat.id, text="4.ФК.(чисельник) - сп.з. || 11:40 - 12:30")
        #             await bot.send_message(chat_id=message.chat.id, text="4.Геогр.(знаменник) - 405 || 11:40 - 12:30")
        #         case 'Tuesday':
        #             await bot.send_message(chat_id=message.chat.id, text="1.Хімія(чисельник) - 302 || 8:30 - 9:20")
        #             await bot.send_message(chat_id=message.chat.id, text="1.БЖ(знаменник) - 409 ||  8:30 - 9:20")
        #             await bot.send_message(chat_id=message.chat.id, text="2.Укр.мова - 302 || 9:30 - 10:20")
        #             await bot.send_message(chat_id=message.chat.id, text="3.ФіА - 408 || 10:40 - 11:30")
        #             await bot.send_message(chat_id=message.chat.id, text="4.Укр.літ - 401 || 11:40 - 12:30")
        #         case 'Wednesday':
        #             await bot.send_message(chat_id=message.chat.id, text="1.Заруб.літ - 203 || 8:30 - 9:20")
        #             await bot.send_message(chat_id=message.chat.id, text="2.Ін.м. - 107/16 || 9:30 - 10:20")
        #             await bot.send_message(chat_id=message.chat.id, text="3.БЕ - 406 || 10:40 - 11:30")
        #         case 'Thursday':
        #             await message.answer(text="1.Соц(чисельник). - 203 || 8:30 - 9:20")
        #             await bot.send_message(chat_id=message.chat.id, text="1.Нічого(Знаменник)")
        #             await bot.send_message(chat_id=message.chat.id, text="2.Матем. - 307 || 9:30 - 10:20")
        #             await bot.send_message(chat_id=message.chat.id, text="3.К.Пр. - 304 || 10:40 - 11:30")
        #             await bot.send_message(chat_id=message.chat.id, text="4.Гр.Осв.(чисельник) - 202 || 11:40 - 12:30")
        #             await bot.send_message(chat_id=message.chat.id, text="4.Вс.Іст.(знаменник) - 301 || 11:40 - 12:30")
        #             await bot.send_message(chat_id=message.chat.id, text="5.ОМЗ - 201 || 12:50 - 13:40")
        #         case 'Friday':
        #             await bot.send_message(chat_id=message.chat.id, text="1.ФК - сп.з. || 8:30 - 9:20")
        #             await bot.send_message(chat_id=message.chat.id, text="2.ФіА - 408 || 9:30 - 10:20")
        #             await bot.send_message(chat_id=message.chat.id, text="3.ЗУ - 204 || 10:40 - 11:30")
        #         # case 'Saturday':
        #         #     await message.answer(text="Культ. - 107 || 8:30 - 9:50")
        #         #     await bot.send_message(chat_id=message.chat.id, text="ФК - сп.з || 10:00 - 11:20")
        #         #     await bot.send_message(chat_id=message.chat.id, text="Вс.Історія - 301 || 12:00 - 13:20")
        #         #     await bot.send_message(chat_id=message.chat.id, text="БЕ - 210 || 13:20 - 14:50")
        #         case other:
        #             await bot.send_message(chat_id=message.chat.id, text="Немає пар по вихідним.Можна бити баклуші")
        if(day == 'Monday'):
            await bot.send_message(chat_id=message.chat.id, text="1.Гр.Осв. - 202 || 8:30 - 9:20")
            await bot.send_message(chat_id=message.chat.id, text="2.Матем. - 307 ||  9:30 - 10:20")
            await bot.send_message(chat_id=message.chat.id, text="3.Інф. - 311/304 || 10:40 - 11:30")
            await bot.send_message(chat_id=message.chat.id, text="4.ФК.(чисельник) - сп.з. || 11:40 - 12:30")
            await bot.send_message(chat_id=message.chat.id, text="4.Геогр.(знаменник) - 405 || 11:40 - 12:30")
        elif(day == 'Tuesday'):
            await bot.send_message(chat_id=message.chat.id, text="1.Хімія(чисельник) - 302 || 8:30 - 9:20")
            await bot.send_message(chat_id=message.chat.id, text="1.БЖ(знаменник) - 409 ||  8:30 - 9:20")
            await bot.send_message(chat_id=message.chat.id, text="2.Укр.мова - 302 || 9:30 - 10:20")
            await bot.send_message(chat_id=message.chat.id, text="3.ФіА - 408 || 10:40 - 11:30")
            await bot.send_message(chat_id=message.chat.id, text="4.Укр.літ - 401 || 11:40 - 12:30")
        elif(day == 'Wednesday'):
            await bot.send_message(chat_id=message.chat.id, text="1.Заруб.літ - 203 || 8:30 - 9:20")
            await bot.send_message(chat_id=message.chat.id, text="2.Ін.м. - 107/16 || 9:30 - 10:20")
            await bot.send_message(chat_id=message.chat.id, text="3.БЕ - 406 || 10:40 - 11:30")
        elif(day == 'Thursday'):
            await message.answer(text="1.Соц(чисельник). - 203 || 8:30 - 9:20")
            await bot.send_message(chat_id=message.chat.id, text="1.Нічого(Знаменник)")
            await bot.send_message(chat_id=message.chat.id, text="2.Матем. - 307 || 9:30 - 10:20")
            await bot.send_message(chat_id=message.chat.id, text="3.К.Пр. - 304 || 10:40 - 11:30")
            await bot.send_message(chat_id=message.chat.id, text="4.Гр.Осв.(чисельник) - 202 || 11:40 - 12:30")
            await bot.send_message(chat_id=message.chat.id, text="4.Вс.Іст.(знаменник) - 301 || 11:40 - 12:30")
            await bot.send_message(chat_id=message.chat.id, text="5.ОМЗ - 201 || 12:50 - 13:40")
        elif(day == 'Friday'):
            await bot.send_message(chat_id=message.chat.id, text="1.ФК - сп.з. || 8:30 - 9:20")
            await bot.send_message(chat_id=message.chat.id, text="2.ФіА - 408 || 9:30 - 10:20")
            await bot.send_message(chat_id=message.chat.id, text="3.ЗУ - 204 || 10:40 - 11:30")
        else:
            await bot.send_message(chat_id=message.chat.id, text="Немає пар по вихідним.Можна бити баклуші")

@dp.message_handler(commands = ['nextpara'])
async def new_timer_message(message: types.Message):
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    now = datetime.now()
    day = week_days[now.weekday() + 1]
    # match day:
    #     case 'Monday':
    #         await bot.send_message(chat_id=message.chat.id, text="1.Гр.Осв. - 202 || 8:30 - 9:20")
    #         await bot.send_message(chat_id=message.chat.id, text="2.Матем. - 307 ||  9:30 - 10:20")
    #         await bot.send_message(chat_id=message.chat.id, text="3.Інф. - 311/304 || 10:40 - 11:30")
    #         await bot.send_message(chat_id=message.chat.id, text="4.ФК.(чисельник) - сп.з. || 11:40 - 12:30")
    #         await bot.send_message(chat_id=message.chat.id, text="4.Геогр.(знаменник) - 405 || 11:40 - 12:30")
    #     case 'Tuesday':
    #         await bot.send_message(chat_id=message.chat.id, text="1.Хімія(чисельник) - 302 || 8:30 - 9:20")
    #         await bot.send_message(chat_id=message.chat.id, text="1.БЖ(знаменник) - 409 ||  8:30 - 9:20")
    #         await bot.send_message(chat_id=message.chat.id, text="2.Укр.мова - 302 || 9:30 - 10:20")
    #         await bot.send_message(chat_id=message.chat.id, text="3.ФіА - 408 || 10:40 - 11:30")
    #         await bot.send_message(chat_id=message.chat.id, text="4.Укр.літ - 401 || 11:40 - 12:30")
    #     case 'Wednesday':
    #         await bot.send_message(chat_id=message.chat.id, text="1.Заруб.літ - 203 || 8:30 - 9:20")
    #         await bot.send_message(chat_id=message.chat.id, text="2.Ін.м. - 107/16 || 9:30 - 10:20")
    #         await bot.send_message(chat_id=message.chat.id, text="3.БЕ - 406 || 10:40 - 11:30")
    #     case 'Thursday':
    #         await message.answer(text="1.Соц(чисельник). - 203 || 8:30 - 9:20")
    #         await bot.send_message(chat_id=message.chat.id, text="1.Нічого(Знаменник)")
    #         await bot.send_message(chat_id=message.chat.id, text="2.Матем. - 307 || 9:30 - 10:20")
    #         await bot.send_message(chat_id=message.chat.id, text="3.К.Пр. - 304 || 10:40 - 11:30")
    #         await bot.send_message(chat_id=message.chat.id, text="4.Гр.Осв.(чисельник) - 202 || 11:40 - 12:30")
    #         await bot.send_message(chat_id=message.chat.id, text="4.Вс.Іст.(знаменник) - 301 || 11:40 - 12:30")
    #         await bot.send_message(chat_id=message.chat.id, text="5.ОМЗ - 201 || 12:50 - 13:40")
    #     case 'Friday':
    #         await bot.send_message(chat_id=message.chat.id, text="1.ФК - сп.з. || 8:30 - 9:20")
    #         await bot.send_message(chat_id=message.chat.id, text="2.ФіА - 408 || 9:30 - 10:20")
    #         await bot.send_message(chat_id=message.chat.id, text="3.ЗУ - 204 || 10:40 - 11:30")
    #     # case 'Saturday':
    #     #     await message.answer(text="Культ. - 107 || 8:30 - 9:50")
    #     #     await bot.send_message(chat_id=message.chat.id, text="ФК - сп.з || 10:00 - 11:20")
    #     #     await bot.send_message(chat_id=message.chat.id, text="Вс.Історія - 301 || 12:00 - 13:20")
    #     #     await bot.send_message(chat_id=message.chat.id, text="БЕ - 210 || 13:20 - 14:50")
    #     case other:
    #         await bot.send_message(chat_id=message.chat.id, text="Немає пар по вихідним.Можна бити баклуші")
    if (day == 'Monday'):
        await bot.send_message(chat_id=message.chat.id, text="1.Гр.Осв. - 202 || 8:30 - 9:20")
        await bot.send_message(chat_id=message.chat.id, text="2.Матем. - 307 ||  9:30 - 10:20")
        await bot.send_message(chat_id=message.chat.id, text="3.Інф. - 311/304 || 10:40 - 11:30")
        await bot.send_message(chat_id=message.chat.id, text="4.ФК.(чисельник) - сп.з. || 11:40 - 12:30")
        await bot.send_message(chat_id=message.chat.id, text="4.Геогр.(знаменник) - 405 || 11:40 - 12:30")
    elif (day == 'Tuesday'):
        await bot.send_message(chat_id=message.chat.id, text="1.Хімія(чисельник) - 302 || 8:30 - 9:20")
        await bot.send_message(chat_id=message.chat.id, text="1.БЖ(знаменник) - 409 ||  8:30 - 9:20")
        await bot.send_message(chat_id=message.chat.id, text="2.Укр.мова - 302 || 9:30 - 10:20")
        await bot.send_message(chat_id=message.chat.id, text="3.ФіА - 408 || 10:40 - 11:30")
        await bot.send_message(chat_id=message.chat.id, text="4.Укр.літ - 401 || 11:40 - 12:30")
    elif (day == 'Wednesday'):
        await bot.send_message(chat_id=message.chat.id, text="1.Заруб.літ - 203 || 8:30 - 9:20")
        await bot.send_message(chat_id=message.chat.id, text="2.Ін.м. - 107/16 || 9:30 - 10:20")
        await bot.send_message(chat_id=message.chat.id, text="3.БЕ - 406 || 10:40 - 11:30")
    elif (day == 'Thursday'):
        await message.answer(text="1.Соц(чисельник). - 203 || 8:30 - 9:20")
        await bot.send_message(chat_id=message.chat.id, text="1.Нічого(Знаменник)")
        await bot.send_message(chat_id=message.chat.id, text="2.Матем. - 307 || 9:30 - 10:20")
        await bot.send_message(chat_id=message.chat.id, text="3.К.Пр. - 304 || 10:40 - 11:30")
        await bot.send_message(chat_id=message.chat.id, text="4.Гр.Осв.(чисельник) - 202 || 11:40 - 12:30")
        await bot.send_message(chat_id=message.chat.id, text="4.Вс.Іст.(знаменник) - 301 || 11:40 - 12:30")
        await bot.send_message(chat_id=message.chat.id, text="5.ОМЗ - 201 || 12:50 - 13:40")
    elif (day == 'Friday'):
        await bot.send_message(chat_id=message.chat.id, text="1.ФК - сп.з. || 8:30 - 9:20")
        await bot.send_message(chat_id=message.chat.id, text="2.ФіА - 408 || 9:30 - 10:20")
        await bot.send_message(chat_id=message.chat.id, text="3.ЗУ - 204 || 10:40 - 11:30")
    else:
        await bot.send_message(chat_id=message.chat.id, text="Немає пар по вихідним.Можна бити баклуші")

@dp.message_handler(commands = ['aboba'])
async def new_timer_message(message: types.Message):
    await message.answer("ABOBA")

@dp.message_handler(commands = ['zamina'])
async def new_timer_message(message: types.Message):
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    now = datetime.now() + pd.DateOffset(days=1)
    day = week_days[now.weekday()]
    # match(day):
    #     case 'Sunday':
    #         await message.answer("Який коледж!? Атдіхай")
    #     case 'Saturday':
    #         await message.answer("Який коледж!? Атдіхай")
    #     case other:
    #         await message.answer("Сьогодні нема замін")
    if(day == 'Sunday' or day == 'Saturday'):
        await bot.send_message(chat_id=message.chat.id, text="Вихідний день")
    else:
        await bot.send_message(chat_id=message.chat.id, text="Сьогодні немає замін")

@dp.message_handler(commands = ['help'])
async def new_timer_message(message: types.Message):
    await message.answer("/para подивитися пари на сьогодні")
    await message.answer("/aboba використовуйте на свій страх і риск")
    await message.answer("/nextpara подивитися пари на завтра")
    await message.answer("/zamina Подивитися заміни на сьогодні")
    await message.answer("/allpara Розклад")

@dp.message_handler(commands = ['roflanebalo'])
async def new_timer_message(message: types.Message):
    await message.answer_photo('https://static-cdn.jtvnw.net/jtv_user_pictures/adeec5c1-d6df-4aff-a0a3-ff8a9a56892a-profile_image-300x300.jpg')

@dp.message_handler(commands=['del'])
async def delete_message(message: types.Message):
    if(message.from_user.id == 1263195198 or message.from_user.id == 1100373871):
        try:
            i = 0
            r = message["message_id"]
            while(i < 50):
                i = i + 1
                print(i)
                r = r - i
                print(r)
                await bot.delete_message(chat_id=message.chat.id, message_id = r)

        except(MessageCantBeDeleted, MessageToDeleteNotFound):
            print("Lox")
    else:
        await message.answer("У вас немає прав на цю команду, спишіться з Старостою, якщо це не так")

# @dp.message_handler(commands=['allpara'])
# async def allPara(message: types.Message):
#     await bot.forward_message(chat_id= -990519529, from_chat_id=-1867635041, message_id=110)


# @dp.message_handler(commands=['online'])
# async def gay(message: types.Message):
#     if (message.from_user.id == 1263195198 or message.from_user.id == 1100373871):
#         today = pd.datetime.now()
#         tomorrow = today + timedelta(1)
#         await bot.send_message(chat_id=-1001867635041, text="Хто " + tomorrow.strftime('%d-%m-%Y') + " навчається онлайн ставте + у коментарі")
#     else:
#         await bot.send_message(chat_id=message.chat.id,text="У вас немає прав на цю команду, спишіться з Старостою, якщо це не так")

# chat_id=-1001867635041






# @dp.message_handler()
# async def getUserData(message: types.Message, i = maini):
#     users = {}
#     isTrue = True
#     while(i < 50):
#         users[i] = message.from_user.username
#         i+=1
#         await bot.send_message(chat_id=message.chat.id, text="Hi")
#     return users, i
















if __name__ == '__main__':
    executor.start_polling(dp)

# while(True):
#     x = datetime.datetime.now()
#     if(x.hour == 14):
#         print("Work")



