from tkinter import *
import os

news = os.listdir('./news')
photos = os.listdir('./img')

root = Tk()
root.title("Inshorts Newspaper")
root.geometry('1366x768')

for text_file, img in zip(news, photos):
    news_card = Frame(root, borderwidth = 3, width = 700)

    photo = PhotoImage(file = os.path.join('./img', img))
    label = Label(news_card, image=photo)
    label.image = photo  # keep a reference!
    label.pack(side = LEFT)

    with open(os.path.join('./news', text_file), 'r') as article:
        news_content = article.read()
        news_block = Text(news_card, height = 5, width = 600, bg = 'lightgrey', font = (20))
        news_block.insert(END, news_content)
        news_block.config(state='disabled')
        # print(article.read())
        # print('-----------------------------------------')
        news_block.pack(side = RIGHT)

    news_card.pack(side = TOP)


root.mainloop()
