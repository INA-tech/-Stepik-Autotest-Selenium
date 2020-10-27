def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке

    index = full_string.find(substring)
    if index == -1:
        print(f"expected '{substring}' to be substring of '{full_string}'")
