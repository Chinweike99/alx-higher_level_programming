def raise_exception_msg(message=""):
    class CustomNameException(Exception):
        pass

    try:
        raise CustomNameException(message)
    except CustomNameException as e:
        print(f"{e}")
