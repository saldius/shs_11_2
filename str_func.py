def string_upper(s):
    """возвращает строку со всеми заглавными буквами"""
    return s.upper()

def string_title(s):
    """возвращает строку с заглавными первыми буквами в каждом слове"""
    return s.title()


if __name__ == '__main__':
    print(string_upper("я играю на гармошке у прохожих "))
    print(string_title("я играю на гармошке у прохожих "))