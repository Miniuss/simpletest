from colorama import Fore
from time import time as ctime

def try_test(func, timeout: float, args: tuple, expects: list):
    """
    # Arguments\n
    ``func`` - Function that you want to test\n
    ``timeout`` - Amount of seconds until program will time out\n
    ``args`` - Tuple with LISTS of arguments (ex. ``([4, 2], [5, 1], [6, 2])``)\n
    ``expects`` - Expected values (list) (must match args)
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
            print(f"{Fore.RED}Error: {e}{Fore.RESET}\n")
            quit()

        elapsed = round(ctime() - time, 3)

        color = Fore.RED if value != cur_exp or elapsed > timeout else Fore.GREEN
        addon = "Success!"

        if elapsed > timeout:
            addon = f"Timed out ({elapsed}s/{timeout}s)"
            fails += 1
        elif value != cur_exp:
            addon = f"Incorrect answer ({Fore.GREEN}{cur_exp}{Fore.RED} | {Fore.LIGHTRED_EX}{value}{Fore.RED})"
            fails += 1

        print(f"{color}Test {i+1} result: {addon}")

    print(f"{Fore.WHITE}Total: {Fore.YELLOW}{ntests-fails}{Fore.WHITE}/{Fore.GREEN}{ntests}{Fore.RESET}\n")