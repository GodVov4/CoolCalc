import re

print("Я - крутий калькулятор")
print("Я швидко порахую все, що скажеш")
print("Якщо захочеш вийти, просто натисни ENTER\n")

previous = 0
run = True


def perform_math():
    global run
    global previous
    if previous == 0:
        equation = input("Що мені порахувати?\n")
    else:
        equation = input(str(previous))
    if equation == "":
        print("До зустрічі")
        run = False
    else:
        equation = re.sub("[a-zA-z,:()!?№;@#^&" "]", "", equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()
