import bcrypt


def psw_check(password_to_check, hashed_password):
    if bcrypt.checkpw(password_to_check, hashed_password):
        # password match
        return True
    else:
        # password doesn't match
        return False
