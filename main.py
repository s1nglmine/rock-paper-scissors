import tkinter as tk
import random

choices = ['камень', 'бумага', 'ножницы']

def handle_choice(choice):
    computer_choice = random.choice(choices)

    if choice == computer_choice:
        result = f'Ничья! Я загадал {computer_choice}'
    elif (choice == 'камень' and computer_choice == 'ножницы') or \
         (choice == 'ножницы' and computer_choice == 'бумага') or \
         (choice == 'бумага' and computer_choice == 'камень'):
        result = f'Вы выиграли! Я загадал {computer_choice}'
    else:
        result = f'Вы проиграли! Я загадал {computer_choice}'

    result_label.config(text=result)

window = tk.Tk()
window.title('Камень Ножницы Бумага')
window.geometry('500x150')

rock_button = tk.Button(window, text='Камень', command=lambda: handle_choice('камень'))
paper_button = tk.Button(window, text='Бумага', command=lambda: handle_choice('бумага'))
scissors_button = tk.Button(window, text='Ножницы', command=lambda: handle_choice('ножницы'))
start_label = tk.Label(window, text='Давай сыграем в Камень Ножницы Бумага')
result_label = tk.Label(window, text='')

start_label.pack()
result_label.pack()
result_label.place(x=160, y=50)
rock_button.pack()
rock_button.place(x=100, y=100)
paper_button.pack()
paper_button.place(x=200, y=100)
scissors_button.pack()
scissors_button.place(x=300, y=100)

window.mainloop()