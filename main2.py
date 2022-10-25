
from email.mime import image
from textwrap import fill
import tkinter as tk
from turtle import bgcolor
from PIL import Image, ImageTk
import tkinter.font as tkFont


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        bgImage = Image.open('bg.jpg')
        self.tkImage = ImageTk.PhotoImage(bgImage)
        mainCanvas = tk.Canvas(self)
        mainCanvas.create_image(0, 0, anchor=tk.NW, image=self.tkImage)
        #tk.Button(mainCanvas, text="click").pack()
        mainCanvas.pack(fill=tk.BOTH, expand=True)
        # end-------建立背景
        '''
        btnbgimage = Image.open('button.jpg').resize(
            (200, 200), Image.ANTIALIAS)  # resize設定大小
        self.tkbtnbgImage = ImageTk.PhotoImage(btnbgimage)
        btn = tk.Button(mainCanvas, text="",
                        image=self.tkbtnbgImage, compound=tk.LEFT,).pack()

        '''
        # -------建立lable------
        # tk.Label(mainCanvas, text='職能發展學院').pack() #pack無法靈活
        helv36 = tkFont.Font(family='Helvetica', size=24, weight='bold')
        tk.Label(mainCanvas, text="職能發展學院", font=helv36,
                 background='#f3790c', foreground="#ffffff").place(x=32, y=43)

        # -------end lable------


def main():
    window = Window()
    window.title("Frame框架")
    window.resizable(0, 0)  # 不給改視窗尺寸
    window.geometry("731x450+350+225")  # 視窗的尺寸加上視窗開啟的距離
    window.mainloop()


if __name__ == "__main__":
    main()
