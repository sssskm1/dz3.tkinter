import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class BookApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Профиль пользователя')
        self.root.geometry('500x400')
        self.root.resizable(False, False)
        self.initUI()

    def initUI(self):
        # Основной фрейм
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))


        image_frame = ttk.Frame(main_frame)
        image_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N)

        try:
            image = Image.open('assets/photo.jpg')
            image = image.resize((200, 200), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            image_label = ttk.Label(image_frame, image=self.photo)
        except FileNotFoundError:
            image_label = ttk.Label(image_frame, text='Изображение не найдено')

        image_label.grid(row=0, column=0)


        info_frame = ttk.Frame(main_frame)
        info_frame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.N)


        title_label = ttk.Label(info_frame, text='Информация',
                                font=('Arial', 12, 'bold'))
        title_label.grid(row=0, column=0, sticky=tk.W, pady=5)


        author_label = ttk.Label(info_frame, text='Биография: Калганова Софья, 19 лет.',
                                 font=('Arial', 10))
        author_label.grid(row=1, column=0, sticky=tk.W, pady=5)


        year_label = ttk.Label(info_frame, text='Обучение: МАИ , 2 курс ,\n 317 кафедра "Инноватика"',
                               font=('Arial', 8))
        year_label.grid(row=2, column=0, sticky=tk.W, pady=5)


        description_label = ttk.Label(info_frame,
                                      text='Опыт работы: отсутствует ',
                                      font=('Arial', 10))
        description_label.grid(row=3, column=0, sticky=tk.W, pady=10)

        # Кнопка
        self.read_button = ttk.Button(info_frame, text='я ознакомился',
                                      command=self.on_read_clicked)
        self.read_button.grid(row=4, column=0, sticky=tk.W, pady=10)

    def on_read_clicked(self):
        print("Пользователь ознакомлен")


if __name__ == '__main__':
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()