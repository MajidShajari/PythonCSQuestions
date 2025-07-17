import tkinter as tk
import math


def clear_message():
    message_label.config(text="", fg="black")


def show_result(msg):
    message_label.config(text=msg, fg="green")


def show_error(msg):
    message_label.config(text=msg, fg="red")


def get_two_numbers():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        return a, b
    except ValueError:
        show_error("ورودی‌ها باید عدد باشند.")
        return None, None


def get_one_number():
    try:
        n = float(entry1.get())
        return n
    except ValueError:
        show_error("ورودی باید عدد باشد.")
        return None


def get_one_integer():
    try:
        n = float(entry1.get())
        if not n.is_integer():
            show_error("ورودی باید عدد صحیح باشد.")
            return None
        return int(n)
    except ValueError:
        show_error("ورودی باید عدد باشد.")
        return None


def add():
    clear_message()
    a, b = get_two_numbers()
    if a is not None and b is not None:
        show_result(f"نتیجه جمع: {a + b}")


def subtract():
    clear_message()
    a, b = get_two_numbers()
    if a is not None and b is not None:
        show_result(f"نتیجه تفریق: {a - b}")


def multiply():
    clear_message()
    a, b = get_two_numbers()
    if a is not None and b is not None:
        show_result(f"نتیجه ضرب: {a * b}")


def divide():
    clear_message()
    a, b = get_two_numbers()
    if a is not None and b is not None:
        if b == 0:
            show_error("تقسیم بر صفر مجاز نیست.")
            return
        show_result(f"نتیجه تقسیم: {a / b}")


def power():
    clear_message()
    a, b = get_two_numbers()
    if a is not None and b is not None:
        show_result(f"نتیجه توان: {a ** b}")


def factorial():
    clear_message()
    n = get_one_integer()
    if n is not None:
        if n < 0:
            show_error("عدد باید غیر منفی باشد.")
            return
        show_result(f"نتیجه فاکتوریل {n}: {math.factorial(n)}")


def sqrt():
    clear_message()
    n = get_one_number()
    if n is not None:
        if n < 0:
            show_error("عدد منفی مجاز نیست.")
            return
        show_result(f"نتیجه جذر {n}: {math.sqrt(n)}")


root = tk.Tk()
root.title("ماشین حساب گرافیکی")

# ورودی‌ها
tk.Label(root, text="عدد اول:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry1 = tk.Entry(root, width=20)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="عدد دوم (در صورت نیاز):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry2 = tk.Entry(root, width=20)
entry2.grid(row=1, column=1, padx=5, pady=5)

# دکمه‌ها
btn_frame = tk.Frame(root)
btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

btn_add = tk.Button(btn_frame, text="جمع", width=12, command=add)
btn_add.grid(row=0, column=0, padx=3, pady=3)

btn_sub = tk.Button(btn_frame, text="تفریق", width=12, command=subtract)
btn_sub.grid(row=0, column=1, padx=3, pady=3)

btn_mul = tk.Button(btn_frame, text="ضرب", width=12, command=multiply)
btn_mul.grid(row=1, column=0, padx=3, pady=3)

btn_div = tk.Button(btn_frame, text="تقسیم", width=12, command=divide)
btn_div.grid(row=1, column=1, padx=3, pady=3)

btn_pow = tk.Button(btn_frame, text="توان", width=12, command=power)
btn_pow.grid(row=2, column=0, padx=3, pady=3)

btn_fact = tk.Button(btn_frame, text="فاکتوریل (فقط عدد اول)", width=20, command=factorial)
btn_fact.grid(row=2, column=1, padx=3, pady=3)

btn_sqrt = tk.Button(btn_frame, text="جذر (فقط عدد اول)", width=20, command=sqrt)
btn_sqrt.grid(row=3, column=0, padx=3, pady=3)

btn_exit = tk.Button(btn_frame, text="خروج", width=20, command=root.destroy)
btn_exit.grid(row=3, column=1, padx=3, pady=3)

# برچسب پیام خطا/نتیجه
message_label = tk.Label(root, text="", fg="black", font=("Arial", 12))
message_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
