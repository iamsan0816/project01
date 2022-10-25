
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
        btn = tk.Button(mainCanvas, text="click",
                        image=self.tkbtnbgImage, compound=tk.LEFT,).pack()


def main():
    window = Window()
    window.title("Frame框架")
    window.geometry("3191x2000")
    window.mainloop()


if __name__ == "__main__":
    main()
