## EN
**simpletest** is a ``Python`` program for testing your functions and see if outcome matches\
Pretty easy to set up and run.\
You can do multiple tests with multiple outcomes.\
**NOTE:** ``tester.py`` is meant to be IMPORTED and used in other files in form of function

#### Requirements
To run this program you will only need ``colorama`` module\
To install it, run ``install_colorama.bat``

## RU
**simpletest** это ``Python`` программа для тестирования ваших функций и сравнения результата с ожиданием\
Очень легко установить и запустить.\
Вы можете делать несколько тестов с несколькими результатами\
**ЗАМЕЧАНИЕ:** ``tester.py`` должен быть ИМПОРТИРОВАН и использован в других файлхах в виде функции

#### Требования
Чтобы запустить эту программу, требуется лишь модуль ``colorama``\
Чтобы установить его, запустите ``install_colorama.bat``

## Example usage | Пример использования
```py
from tester import try_test

def multiply(*nums):
    x = 1

    for n in nums:
        x *= n

    return x

try_test(multiply,                # Tell function, what to do
        1.0,                      # Tell function, how long program can run
        ([1, 5], [6, 2, 6], [6]), # Arguments. In this case, we need to do 1x5, 6x2x6, and single number 6
        [5, 72, 6],               # Expectations. In here, we expect 1x5=5, 6x2x6=72 and 6=6
        "en")                     # Language ("ru" or "en", defaults to "en")

# Output should be
#
# Test result 1: Success
# Test result 2: Success
# Test result 3: Success
# Overall tests result: 3/3
```
