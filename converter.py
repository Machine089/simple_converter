print("Temperature converter")


def celsius_k(t_int):
    res = t_int + 273.15
    return round(res, 3)


def celsius_f(t_int):
    res = (t_int * (9/5)) + 32
    return round(res, 3)


def kalvin_c(t_int):
    res = t_int - 273.15
    return round(res, 3)


def kalvin_f(t_int):
    res = (t_int - 273.15) * (9/5) + 32
    return round(res, 3)


def fahrenheit_c(t_int):
    res = (t_int - 32) * (5/9)
    return round(res, 3)


def fahrenheit_k(t_int):
    res = (t_int - 32) * (5/9) + 273.15
    return round(res, 3)


def converter():
    t = str(input('Enter temperature scale to be converted: ').upper())
    t_2 = str(input('Enter required scale: ').upper())
    t_int = float(input('Enter temperature: '))

    if t == 'C' and t_2 == 'K':
        return print(celsius_k(t_int))
    elif t == 'C' and t_2 == 'F':
        return print(celsius_f(t_int))

    if t == 'K' and t_2 == 'C':
        return print(kalvin_c(t_int))
    elif t == 'K' and t_2 == 'F':
        return print(kalvin_f(t_int))

    if t == 'F' and t_2 == 'C':
        return print(fahrenheit_c(t_int))
    elif t == 'F' and t_2 == 'K':
        return print(fahrenheit_k(t_int))


status = 1

while status:
    work = str(input("Do we convert? ").capitalize())
    if work == 'Yes':
        converter()
    elif work == 'No':
        status = 0
        print("Goodbye")
    else:
        print("Input error. Enter 'Yes' or 'NO'")
