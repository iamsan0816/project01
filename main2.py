
from email.mime import image
import tkinter as tk
from PIL import Image, ImageTk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        bgImage = Image.open('bg.jpg')
        self.tkImage = ImageTk.PhotoImage(bgImage)
        mainCanvas = tk.Canvas(self)
        mainCanvas.create_image(0, 0, anchor=tk.NW, image=self.tkImage)
        #tk.Button(mainCanvas, text="click").pack()
        mainCanvas.pack(fill=tk.BOTH, expand=True)

        btnbgimage = Image.open('button.jpg').resize(
            (200, 200), Image.ANTIALIAS)  # resize設定大小
        self.tkbtnbgImage = ImageTk.PhotoImage(btnbgimage)
        btn = tk.Button(mainCanvas, text="",
                        image=self.tkbtnbgImage, compound=tk.LEFT,).pack()


def main():
    window = Window()
    window.title("Frame框架")
    window.resizable(0, 0)  # 不給改視窗尺寸
    window.geometry("640x480+300+200")  # 視窗的尺寸加上視窗開啟的距離
    window.mainloop()


if __name__ == "__main__":
    main()
