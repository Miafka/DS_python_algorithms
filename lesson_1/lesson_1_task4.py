# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

UNICODE_a = ord('a')
UNICODE_z = ord('z')

start = (input("Введите символ от 'a' до 'z': ")).lower()
end = (input("Введите символ от 'a' до 'z': ")).lower()

unicode_start = ord(start)
unicode_end = ord(end)

if UNICODE_a <= unicode_start <= UNICODE_z and UNICODE_a <= unicode_end <= UNICODE_z:
    if unicode_start < unicode_end:
        poz_start = unicode_start - UNICODE_a + 1
        poz_end = unicode_end - UNICODE_a + 1
        print(f"Позиция '{start}' = {poz_start}, позиция '{end}' = {poz_end}, "
              f"букв между ними: {poz_end - poz_start - 1}")
    else:
        poz_start = unicode_start - UNICODE_a + 1
        poz_end = unicode_end - UNICODE_a + 1
        print(f"Позиция '{start}' = {poz_start}, позиция '{end}' = {poz_end}, "
              f"букв между ними: {poz_start - poz_end - 1}")

else:
    print("Неверный ввод, введите букву от 'a' до 'z'")
