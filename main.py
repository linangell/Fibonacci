import tkinter as tk
import fibonacci
import factorial

def calculate_factorial():
    k = int(entry.get())
    result = factorialfactorial(k)
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

# print ('Which task would you like to perform:')
# print('1: Find	the	factorial	')
# print('2: Find	the	fibonacci value	')
# m = input ("Enter the number of the task you'd like to perform : ")
# if m == '1':
#   v = input ("Enter the integer you'd like to find its factorial: ")
#
#   print('the factorial of' , v , 'is' , n )
# elif m == '2':
#   l = input ("Enter the sequences position of the fibonacci value: ")
#
#   print('the value pf posion' , v , 'in the fibonachi value' , k )


