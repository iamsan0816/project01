import tkinter as tk

'''
def createWindow():
    window = tk.Tk()
    window.title("這是我的第一個視窗")
    btn = tk.Button(window, text='請按我', padx=20,
                    pady=20, font=('arial', 16))
    btn.pack(padx=50, pady=30)
    window.mainloop()



def main():
    createWindow()


if __name__ == "__main__":
    main()
'''


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("這是我的第一個觀窗")
        '''
        btn = tk.Button(self, text="請按我", padx=20, pady=20, font=('arial', 36))
        btn.pack(padx=100, pady=30)
        '''
        tk.Button(self, text="請按我", padx=20, pady=20, font=(
            'arial', 16), command=self.userClick).pack(padx=50, pady=30)

    def userClick(self):
        print("userClick")


def main():
    window = Window()
    window.mainloop()


if __name__ == "__main__":
    main()
