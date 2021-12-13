# 1. To create a function that would check whether the submitted personal identification code of a Lithuanian citizen
# is valid.
# 2. Make the program generate the correct personal code (using the previously created function) according to the
# entered one
# gender, date of birth and serial number)

def return_personal_control_nr(personal_nr):
    code = str(personal_nr)
    a = int(code[0])
    b = int(code[1])
    c = int(code[2])
    d = int(code[3])
    e = int(code[4])
    f = int(code[5])
    g = int(code[6])
    h = int(code[7])
    i = int(code[8])
    j = int(code[9])
    s = a * 1 + b * 2 + c * 3 + d * 4 + e * 5 + f * 6 + g * 7 + h * 8 + i * 9 + j * 1
    if s % 11 != 10:
        control = s % 11
    else:
        s = a * 3 + b * 4 + c * 5 + d * 6 + e * 7 + f * 8 + g * 9 + h * 1 + i * 2 + j * 3
        if s % 11 != 10:
            control = s % 11
        else:
            control = 0
    return control


def personal_code_validation(personal_nr):
    last_nr = int(str(personal_nr)[-1])
    return last_nr == return_personal_control_nr(personal_nr)


def personal_nr_generation(gender, date_of_birth, serial_nr):
    data_split = date_of_birth.split("-")
    years = int(data_split[0][:2])

    if gender == "man":
        first_nr = str((int(years) - 18) * 2 + 1)
    else:
        first_nr = str((int(years) - 18) * 2 + 2)

    years = data_split[0][2:]
    month = data_split[1]
    day = data_split[2]

    without_last_nr = first_nr + years + month + day + serial_nr
    pers_code = int(without_last_nr + str(return_personal_control_nr(without_last_nr)))
    return pers_code


print(personal_code_validation(45102129986))
print(personal_code_validation(61907108400))
print(personal_nr_generation("man", "1999-09-16", "512"))
