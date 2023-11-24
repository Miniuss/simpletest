from colorama import Fore
from time import time as ctime

langs = {
    "ru": {
        "testres": "Результат теста",
        "timeout": "Время ожидания истекло",
        "wrong": "Неверный ответ",
        "elapsed": "Пройденное время",
        "result": "Результат тестов",
        "good": "Успех"
    },
    "en": {
        "testres": "Test result",
        "timeout": "Timeout",
        "wrong": "Wrong answer",
        "elapsed": "Elapsed time",
        "result": "Overall tests result",
        "good": "Success"
    }
}

def try_test(func, timeout: float, args: tuple, expects: list, lang: str = "en"):
    """
    # Arguments\n
    ## EN\n
    ``func`` - Function that you want to test\n
    ``timeout`` - Amount of seconds until program will time out\n
    ``args`` - Tuple with LISTS of arguments (ex. ``([4, 2], [5, 1], [6, 2])``)\n
    ``expects`` - Expected values (list) (must match args)\n
    ``lang`` - Output language\n
    ## RU\n
    > RU\n
    ``func`` - Функция, которую нужно проверить\n
    ``timeout`` - Количество времени ожидания\n
    ``args`` - Кортеж (tuple) с листами аргументов (пр. ``([4, 2], [5, 1], [6, 2])``)\n
    ``expects`` - Ожидаемые значения (лист) (должен совпадать с args)\n
    ``lang`` - Язык вывода"""

    if not langs.get(lang):
        lang = "en"

    fails = 0
    ntests = len(expects)

    for i in range(ntests):
        cur_arg = args[i]
        cur_exp = expects[i]

        time = ctime()
        try:
            value = func(*cur_arg)
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Fore.RESET}\n")
            quit()

        elapsed = round(ctime() - time, 3)

        color = Fore.RED if value != cur_exp or elapsed > timeout else Fore.GREEN
        addon = langs[lang]["good"]

        if elapsed > timeout:
            addon = f"{langs[lang]['timeout']} ({elapsed}s/{timeout}s)"
            fails += 1
        elif value != cur_exp:
            addon = f"{langs[lang]['wrong']} ({Fore.GREEN}{cur_exp}{Fore.RED} | {Fore.LIGHTRED_EX}{value}{Fore.RED})"
            fails += 1

        print(f"{color}{langs[lang]['testres']} {i+1}: {addon}")

    print(f"{Fore.WHITE}{langs[lang]['result']}: {Fore.YELLOW}{ntests-fails}{Fore.WHITE}/{Fore.GREEN}{ntests}{Fore.RESET}\n")