# docs string 関数の説明を残す場合は"""でくくる"""
def example_func(param1, param2):
    """
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
    Returns:
        bool: The return value. True for success, False otherwise
    """
    print(param1)
    print(param2)
    return True

print(example_func.__doc__)
print(help(example_func))
