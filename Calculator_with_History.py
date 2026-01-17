def show_history():
    with open('history.txt', 'r') as file:
        lines = file.readlines()
        if len(lines) == 0:
            print('No history found!')
        else:
            for line in reversed(lines):
                print(line.strip())

def clear_history():
    with open('history.txt', 'w') as file:
        print('History cleared!!')

def save_history(equation, result):
    with open('history.txt', 'a') as file:
        file.write(equation + "=" + str(result) + "\n")

def calculate(user):
    parts = user.split()
    if len(parts) != 3:
        print("Invalid input, Use format: number operator number (e.g, 8 + 2)")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print('Cannot divide by zero')
            return
        result = num1 / num2
    else:
        print('Invalid operator, Use only + - * /')
        return

    if int(result) == result:
        result = int(result)

    print("Result: ", result)

    save_history(user, result)

def main():
    print('-----SIMPLE CALCULATOR-----')

    while True:
        user = input('Enter calculation (+ - * /) or command (history, clear or exit) :- ')

        if user == 'exit':
            print('Goodbye')
            break
        elif user == 'history':
            show_history()
        elif user == 'clear':
            clear_history()
        else:
            calculate(user)

main()