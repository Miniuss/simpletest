from colorama import Fore
from time import time as ctime

def try_test(func, timeout: float, args: tuple, expects: list):
    """
    # Аргументы\n
    ``func`` - Функция, которую нужно проверить\n
    ``timeout`` - Количество времени ожидания\n
    ``args`` - Кортеж (tuple) с листами аргументов (пр. ``([4, 2], [5, 1], [6, 2])``)\n
    ``expects`` - Ожидаемые значения (лист) (должен совпадать с args)
    """

    fails = 0
    ntests = len(expects)

    for i in range(ntests):
        cur_arg = args[i]
        cur_exp = expects[i]

        time = ctime()
        
        try:
            value = func(*cur_arg)
        except Exception as e:
            print(f"{Fore.RED}Ошибка: {e}{Fore.RESET}\n")
            quit()

        elapsed = round(ctime() - time, 3)

        color = Fore.RED if value != cur_exp or elapsed > timeout else Fore.GREEN
        addon = "Успех!"

        if elapsed > timeout:
            addon = f"Время ожидания истекло ({elapsed}s/{timeout}s)"
            fails += 1
        elif value != cur_exp:
            addon = f"Неверный ответ ({Fore.GREEN}{cur_exp}{Fore.RED} | {Fore.LIGHTRED_EX}{value}{Fore.RED})"
            fails += 1

        print(f"{color}Результат теста {i+1}: {addon}")

    print(f"{Fore.WHITE}Результат тестов: {Fore.YELLOW}{ntests-fails}{Fore.WHITE}/{Fore.GREEN}{ntests}{Fore.RESET}\n")