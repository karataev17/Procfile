@dp.message_handler()
async def echo(message: Message):
    message1 = message.text
    a = len(message1)
    P = 0
    d = ""
    i = 0
    while (i < a):
        if (message1[i] != " ") and i != a - 1:
            d += message1[i]
        elif i == a - 1:
            d += message1[i]
            P += int(d)
        else:
            P += int(d)
            d = ""

        i += 1
    text = str(P)
    await bot.send_message(chat_id=message.from_user.id, text=text)