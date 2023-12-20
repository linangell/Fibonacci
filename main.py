# import fibonacci
# import factorial
#
# print("Which task would you like to perform:")
#
# k = int(input("Enter the integer you'd like to find its factorial: "))
#     result = factorial.factorial(k)
#     print("The factorial of", k, "is", result)
#
# n = int(input("Enter the position in the Fibonacci sequence: "))
#     result = fibonacci.fibonacci(n)
#     print("The Fibonacci sequence up to position", n,  "is:" ,sequence)


import tkinter as tk
import fibonacci
import factorial

def calculate_factorial():
    k = int(entry.get())
    result = factorial.factorial(k)
    result_label.config(text=result)


def calculate_fibonacci():
    n = int(entry.get())
    result = fibonacci.fibonacci(n)
    result_label.config(text=result)

window = tk.Tk()
window.title("ff")

label = tk.Label(window, text="Which task would you like to perform:")
label.pack()

factorial_button = tk.Button(window, text="Find the factorial", command=calculate_factorial)
factorial_button.pack()

fibonacci_button = tk.Button(window, text="Find the Fibonacci value", command= calculate_fibonacci)
fibonacci_button.pack()

entry = tk.Entry(window)
entry.pack()

result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()
