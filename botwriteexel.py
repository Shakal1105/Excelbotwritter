import pandas
from telebot import TeleBot

class QQ():
    def __init__(self):
        self.name = []
        self.num = []
        self.price = []

        self.app()

    def app(self):

        bot = TeleBot("5274458764:AAErPIzV3Ual3dunjQCR5of4LRGAOG9ZTY8")
        print("work")
        @bot.message_handler(commands=["star"])
        def dfdf(m):
            self.exelbase = pandas.DataFrame({"НАзва": self.name, "Количество": self.num, "Цена": self.price})
            self.exelbase.to_excel('./123.xlsx', index=False)
            bot.send_message(m.chat.id, "zapisano y file")

        @bot.message_handler(content_types=["text"])
        def exel(m):
            text = m.text
            arr = text.split('\n')
            for i in arr:
                arr = i.split(' ')
                self.k = len(arr)
                self.name.append(arr[0])
                self.num.append(arr[self.k-2])
                self.price.append(arr[self.k-1])
            print(arr)
            bot.delete_message(m.chat.id, m.id)


        bot.polling()

QQ()