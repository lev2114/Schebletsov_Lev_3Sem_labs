def print_result(func):
    def wrapper(*args, **kwargs):

        print(func.__name__)

        result = func(*args, **kwargs)

        if isinstance(result, list):
            for i in result:
                print(i)
        elif isinstance(result, dict):
            for i in result:
                print(i, "=", result[i])
        else:
            print(result)

        return result
    return wrapper
