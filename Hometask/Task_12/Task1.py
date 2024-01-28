def is_admin(func):
    def wrapper(user_type: str):
        if user_type == 'admin':
            func(user_type)
        else:
            raise ValueError(f'Permission denied')
    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    print(f'User: {user_type}')
    # Some very dangerous operation


# show_customer_receipt(user_type='user')
# > ValueError: Permission denied
#
# show_customer_receipt(user_type='admin')
# > function pass as it should be
