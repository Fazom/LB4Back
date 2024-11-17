# main.py

from functions import *

def main():
    try:
        print(divide(10, 2))
        print(find_in_list([1, 2, 3], 1))

        print(safe_divide(10, 0))

        print(safe_file_read("nonexistent_file.txt"))

        string_operations("123", 10)
        list_operations([1, 2, 3], 5, 10)

        generate_exception("value")

        check_value(-1)

        lst = [1, 2, 3]
        print(add_to_list(lst, 4))
        print("Четное число:", is_even(4))
        print("Максимум:", find_max_in_strings(["1.1","2.2", "3.3"]))

    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
