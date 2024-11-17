
# Шаг 1: Две функции без обработчиков исключений
def divide(a, b):
    if b == 0:
        raise ValueError("Делить на ноль не надо")
    return a / b

def find_in_list(lst, index):
    if index < 0 or index >= len(lst):
        raise IndexError("Индекс за пределами списка")
    return lst[index]

# Шаг 2: Функция с обработчиком Exception (без finally)
def safe_divide(a, b):
    try:
        return a / b
    except Exception as e:
        print(f"Ошибка: {e}")

# Шаг 3: Функция с обработчиком Exception и блоком finally
def safe_file_read(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    finally:
        print("Операция чтения завершена")

# Шаг 4: Функции с обработчиками разных типов исключений
def string_operations(s, index):
    try:
        num = int(s)
        return s[index]
    except ValueError:
        print("Невозможно преобразовать строку в число")
    except IndexError:
        print("Индекс за пределами строки")
    finally:
        print("Операция завершена")

def list_operations(lst, index, value):
    try:
        lst[index] = value
        return lst
    except IndexError:
        print("Индекс за пределами списка")
    except TypeError:
        print("Неправильный тип данных")
    finally:
        print("Операция со списком завершена")

# Шаг 5: Генерация и обработка исключений внутри функции
def generate_exception(condition):
    try:
        if condition == "value":
            raise ValueError("Условие value вызвало исключение")
        elif condition == "type":
            raise TypeError("Условие type вызвало исключение")
        else:
            raise Exception("Неизвестное исключение")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        print("Исключение обработано")

# Шаг 6: Пользовательские исключения
class CustomError(Exception):
    """Общее пользовательское исключение"""
    pass

class NegativeValueError(CustomError):
    """Исключение для отрицательных значений"""
    pass

class EmptyListError(CustomError):
    """Исключение для пустых списков"""
    pass

# Шаг 7: Использование пользовательского исключения
def check_value(value):
    try:
        if value < 0:
            raise NegativeValueError("Значение не может быть отрицательным")
        elif value == 0:
            raise CustomError("Значение не может быть нулём")
    except CustomError as ce:
        print(f"CustomError: {ce}")
    finally:
        print("Проверка значения завершена")

# Шаг 8: Дополнительные функции для демонстрации
def add_to_list(lst, value):
    if not isinstance(lst, list):
        raise TypeError("lst должен быть списком")
    lst.append(value)
    return lst

def is_even(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Параметр должен быть числом.")
    if number < 0:
        raise ValueError("Число должно быть неотрицательным.")

    return number % 2 == 0

def find_max_in_strings(string_numbers):
    try:
        numbers = [float(num) for num in string_numbers]
    except ValueError as e:
        raise ValueError(f"Список содержит некорректные строки: {e}")

    return max(numbers)
