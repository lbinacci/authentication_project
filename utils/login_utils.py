import bcrypt


def psw_check(password_to_check, hashed):
    if bcrypt.checkpw(password_to_check, hashed):\
        # password match
        return True
    else:
        # password doesn't match
        return False