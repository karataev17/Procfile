from bot import bot, dp
from aiogram.types import Message
from config import admin_id
from aiogram.dispatcher.filters import Command, Text
from keyboards.default import menu
from states.test1 import Test1
from states.Test4 import Test4
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.test import Test
from states.test2 import Test2
from states.test3 import Test3
from bot import bot

async def send_to_message(dp):
    await bot.send_message(chat_id=admin_id, text="Ехала", )


@dp.message_handler(Command("start"))
async def echo(message: Message):
    text = f"Привет,{message.from_user.first_name}\nРад с тобой познакомиться!\n Нажми на /menu чтобы выбрать нужную категорию(или воспользуйтесь командами)"
    await message.answer(text=text)




@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer(f" {message.from_user.first_name} ,выбери ?", reply_markup=menu)


@dp.message_handler(Text(equals=["Сколько мне надо набрать на сессии?","Лек/практика/сро", "Практика/Сро","Лек/Сро/Лабка","Лек/практика/сро/лабка"]))
async def get_food(message: Message):
    if(message.text=="Лек/практика/сро"):
        await message.answer(f"Вы выбрали Лек/Прак/Сро!Нажмите на /LekPrakSro",
                                reply_markup=ReplyKeyboardRemove())
    elif(message.text=="Сколько мне надо набрать на сессии?"):
        await message.answer(f"Нажмите на /Itog",
                                reply_markup=ReplyKeyboardRemove())
    elif(message.text=="Практика/Сро"):
        await message.answer(f"Вы выбрали Прак/Сро!Нажмите на /PrakSro",
                                reply_markup=ReplyKeyboardRemove())
    elif(message.text=="Лек/Сро/Лабка"):
        await message.answer(f"Вы выбрали Лек/Сро/Лабка!Нажмите на /LekSroLab",
                                reply_markup=ReplyKeyboardRemove())
    elif(message.text=="Лек/практика/сро/лабка"):
        await message.answer(f"Вы выбрали Лек/Практика/Сро/Лабка!Нажмите на /LekPrakSroLab",
                                reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Command("Itog"),state=None)
async def osenka(message: types.Message):
    await message.answer("Введите рейтинг допуска")

    await Test3.Q1.set()
@dp.message_handler(state=Test3.Q1)
async def answer_q10(message: types.Message, state: FSMContext):
    answer = message.text
    Itog=int(answer)
    Step=abs((Itog*0.6-70)/0.4)
    Peterka=abs((Itog*0.6-90)/0.4)
    await message.answer(f"У вас {int(message.text)} баллов \n"
                         f"Чтобы остаться на степендии,вам надо набрать-{int(Step)} балов \n"
                         f"Чтобы получить 5ку вам надо-{int(Peterka)} балов")
    await state.reset_state()
    await state.finish()


@dp.message_handler(Command("LekPrakSRO"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Вы начали работу с калькулятором.\n"
                         "Лекция. \n\n"
                         "Введите оценки по лекции через пробел(н.я - писать как 0) \n"
                         "Пример:100 100 100 0 100")

    # Вариант 1 - с помощью функции сет
    await Test.Q1.set()

    # Вариант 2 - с помощью first
    # await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # Ваирант 2 получения state
    #state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    #Вариант 1 сохранения переменных - записываем через key=var
    await state.update_data(answer1=answer)

    # Вариант 2 - передаем как словарь
    await state.update_data(
        {"answer1": answer}
    )

    await message.answer("Практика. \n\n"
                         "Введите оценки по практике через пробел(н.я - писать как 0)\n"
                         "Пример:100 100 100 0 100")


    await Test.next()
@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text

    # Ваирант 2 получения state
    #state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    #Вариант 1 сохранения переменных - записываем через key=var
    await state.update_data(answer2=answer)

    # Вариант 2 - передаем как словарь
    await state.update_data(
        {"answer2": answer}
    )

    await message.answer("СРО. \n\n"
                         "Введите оценки по СРО через пробел(н.я - писать как 0)\n"
                         "Пример:100 100 100 0 100")


    await Test.next()


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    # Достаем переменные
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = message.text

    message1 = answer1
    message2 = answer2
    message3=answer3
    a = len(message1)
    P = 0
    Itog=0
    d = ""
    kol=1
    i = 0
    while (i < a):
        if (message1[i] != " ") and i != a - 1:
            d += message1[i]


        elif i == a - 1:
            d += message1[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P=P/kol
    Itog+=P*0.2
    d = ""
    P=0
    kol = 1
    i=0
    a = len(message2)
    while (i < a):
        if (message2[i] != " ") and i != a - 1:
            d += message2[i]
        elif i == a - 1:
            d += message2[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P = P / kol
    Itog+= P * 0.5
    d = ""
    P=0
    kol = 1
    i=0
    a = len(message3)
    while (i < a):
        if (message3[i] != " ") and i != a - 1:
            d += message3[i]
        elif i == a - 1:
            d += message3[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P = P / kol
    Itog+= P * 0.3
    Sessia=abs((Itog*0.6-70)/0.4)

    await message.answer(f"Ваш средний текущий бал-{int(Itog)}\n"
                         f"Для того чтобы сохранить степендию вам надо набрать-{int(Sessia)}")

    # Вариант 1
    await state.finish()

    # Вариант завершения 2
    await state.reset_state()

    # Вариант завершения 3 - без стирания данных в data
    await state.reset_state(with_data=False)
@dp.message_handler(Command("PrakSro"), state=None)
async def enter_test1(message: types.Message):
    await message.answer("Практика. \n\n"
                         "Введите оценки по практике через пробел(н.я - писать как 0)\n"
                         "Пример:100 100 100 0 100")

    # Вариант 1 - с помощью функции сет
    await Test1.Q1.set()

    # Вариант 2 - с помощью first
    # await Test.first()


@dp.message_handler(state=Test1.Q1)
async def answer_q11(message: types.Message, state: FSMContext):
    answer = message.text

    # Ваирант 2 получения state
    #state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    #Вариант 1 сохранения переменных - записываем через key=var
    await state.update_data(answer1=answer)

    # Вариант 2 - передаем как словарь
    await state.update_data(
        {"answer1": answer}
    )

    await message.answer("СРО. \n\n"
                         "Введите оценки по СРО через пробел(н.я - писать как 0)\n"
                         "Пример:100 100 100 0 100")

    await Test1.next()



@dp.message_handler(state=Test1.Q2)
async def answer_q21(message: types.Message, state: FSMContext):
    # Достаем переменные
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    message1 = answer1
    message2 = answer2
    a = len(message1)
    P = 0
    Itog=0
    d = ""
    kol=1
    i = 0
    while (i < a):
        if (message1[i] != " ") and i != a - 1:
            d += message1[i]


        elif i == a - 1:
            d += message1[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P=P/kol
    Itog+=P*0.6
    d = ""
    P=0
    kol = 1
    i=0
    a = len(message2)
    while (i < a):
        if (message2[i] != " ") and i != a - 1:
            d += message2[i]
        elif i == a - 1:
            d += message2[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P = P / kol
    Itog+= P * 0.4
    Sessia=abs((Itog*0.6-70)/0.4)
    await message.answer(f"Ваш средний текущий бал-{int(Itog)}\n"
                         f"Для того чтобы сохранить степендию вам надо набрать-{int(Sessia)}")

    # Вариант 1
    await state.finish()

    # Вариант завершения 2
    await state.reset_state()

    # Вариант завершения 3 - без стирания данных в data
    await state.reset_state(with_data=False)
@dp.message_handler(Command("LekSroLab"), state=None)
async def enter_test2(message: types.Message):
    await message.answer("Вы начали работу с калькулятором.\n"
                         "Лекция. \n\n"
                         "Введите оценки по лекции через пробел(н.я - писать как 0) \n"
                         "Пример:100 100 100 0 100")

    # Вариант 1 - с помощью функции сет
    await Test4.Q1.set()

    # Вариант 2 - с помощью first
    # await Test.first()


@dp.message_handler(state=Test4.Q1)
async def answer_q12(message: types.Message, state: FSMContext):
    answer = message.text

    # Ваирант 2 получения state
    #state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    #Вариант 1 сохранения переменных - записываем через key=var
    await state.update_data(answer1=answer)

    # Вариант 2 - передаем как словарь
    await state.update_data(
        {"answer1": answer}
    )

    await message.answer("СРО. \n\n"
                         "Введите оценки по СРО через пробел(н.я - писать как 0)\n"
                         "Пример:100 100 100 0 100")


    await Test4.next()
@dp.message_handler(state=Test4.Q2)
async def answer_q22(message: types.Message, state: FSMContext):
    answer = message.text

    # Ваирант 2 получения state
    #state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    #Вариант 1 сохранения переменных - записываем через key=var
    await state.update_data(answer2=answer)

    # Вариант 2 - передаем как словарь
    await state.update_data(
        {"answer2": answer}
    )

    await message.answer("Лабораторная работа. \n\n"
                         "Введите оценки по лабке через пробел(н.я - писать как 0)\n"
                         "Пример:100 100 100 0 100")


    await Test4.next()


@dp.message_handler(state=Test4.Q3)
async def answer_q32(message: types.Message, state: FSMContext):
    # Достаем переменные
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = message.text

    message1 = answer1
    message2 = answer2
    message3=answer3
    a = len(message1)
    P = 0
    Itog=0
    d = ""
    kol=1
    i = 0
    while (i < a):
        if (message1[i] != " ") and i != a - 1:
            d += message1[i]


        elif i == a - 1:
            d += message1[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P=P/kol
    Itog+=P*0.2
    d = ""
    P=0
    kol = 1
    i=0
    a = len(message2)
    while (i < a):
        if (message2[i] != " ") and i != a - 1:
            d += message2[i]
        elif i == a - 1:
            d += message2[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P = P / kol
    Itog+= P * 0.5
    d = ""
    P=0
    kol = 1
    i=0
    a = len(message3)
    while (i < a):
        if (message3[i] != " ") and i != a - 1:
            d += message3[i]
        elif i == a - 1:
            d += message3[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P = P / kol
    Itog+= P * 0.3
    Sessia=abs((Itog*0.6-70)/0.4)

    await message.answer(f"Ваш средний текущий бал-{int(Itog)}\n"
                         f"Для того чтобы сохранить степендию вам надо набрать-{int(Sessia)}")

    # Вариант 1
    await state.finish()

    # Вариант завершения 2
    await state.reset_state()

    # Вариант завершения 3 - без стирания данных в data
    await state.reset_state(with_data=False)
@dp.message_handler(Command("LekPrakSroLab"), state=None)
async def enter_test4(message: types.Message):
    await message.answer("Вы начали работу с калькулятором.\n"
                         "Лекция. \n\n"
                         "Введите оценки по лекции через пробел(н.я - писать как 0) \n"
                         "Пример:100 100 100 0 100")

    # Вариант 1 - с помощью функции сет
    await Test2.Q1.set()

    # Вариант 2 - с помощью first
    # await Test.first()


@dp.message_handler(state=Test2.Q1)
async def answer_q14(message: types.Message, state: FSMContext):
    answer = message.text

    # Ваирант 2 получения state
    #state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    #Вариант 1 сохранения переменных - записываем через key=var
    await state.update_data(answer1=answer)

    # Вариант 2 - передаем как словарь
    await state.update_data(
        {"answer1": answer}
    )

    await message.answer("Практика. \n\n"
                         "Введите оценки по практике через пробел(н.я - писать как 0)\n"
                         "Пример:100 100 100 0 100")


    await Test2.next()
@dp.message_handler(state=Test2.Q2)
async def answer_q24(message: types.Message, state: FSMContext):
    answer = message.text

    # Ваирант 2 получения state
    #state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    #Вариант 1 сохранения переменных - записываем через key=var
    await state.update_data(answer2=answer)

    # Вариант 2 - передаем как словарь
    await state.update_data(
        {"answer2": answer}
    )

    await message.answer("СРО. \n\n"
                         "Введите оценки по СРО через пробел(н.я - писать как 0)\n"
                         "Пример:100 100 100 0 100")


    await Test2.next()


@dp.message_handler(state=Test2.Q3)
async def answer_q34(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)

    # Вариант 2 - передаем как словарь
    await state.update_data(
        {"answer3": answer}
    )

    await message.answer("Лабораторная работа. \n\n"
                         "Введите оценки по лабке через пробел(н.я - писать как 0)\n"
                         "Пример:100 100 100 0 100")


    await Test2.next()
@dp.message_handler(state=Test2.Q4)
async def answer_q44(message: types.Message, state: FSMContext):
    # Достаем переменные
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = data.get("answer3")
    answer4=message.text
    message1 = answer1
    message2 = answer2
    message3=answer3
    message4=answer4
    a = len(message1)
    P = 0
    Itog=0
    d = ""
    kol=1
    i = 0
    while (i < a):
        if (message1[i] != " ") and i != a - 1:
            d += message1[i]


        elif i == a - 1:
            d += message1[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P=P/kol
    Itog+=P*0.2
    d = ""
    P=0
    kol = 1
    i=0
    a = len(message2)
    while (i < a):
        if (message2[i] != " ") and i != a - 1:
            d += message2[i]
        elif i == a - 1:
            d += message2[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P = P / kol
    Itog+= P * 0.2
    d = ""
    P=0
    kol = 1
    i=0
    a = len(message3)
    while (i < a):
        if (message3[i] != " ") and i != a - 1:
            d += message3[i]
        elif i == a - 1:
            d += message3[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P = P / kol
    Itog+= P * 0.3
    d = ""
    P=0
    kol = 1
    i=0
    a = len(message4)
    while (i < a):
        if (message4[i] != " ") and i != a - 1:
            d += message4[i]
        elif i == a - 1:
            d += message4[i]
            P += int(d)
        else:
            P += int(d)
            kol += 1
            d = ""

        i += 1
    P = P / kol
    Itog+= P * 0.3
    Sessia=abs((Itog*0.6-70)/0.4)

    await message.answer(f"Ваш средний текущий бал-{int(Itog)}\n"
                         f"Для того чтобы сохранить степендию вам надо набрать-{int(Sessia)}")

    # Вариант 1
    await state.finish()

    # Вариант завершения 2
    await state.reset_state()

    # Вариант завершения 3 - без стирания данных в data
    await state.reset_state(with_data=False)
