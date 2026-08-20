def check_len(username, valid):
    if len(username) < 3 or len(username) > 20:
        valid = False
        print("Reason: Username must be between 3 and 20 characters.")
        return valid
    else:
        return valid


def check_char(username, allowed_chars, valid):
    keys = ""

    for key in username:
        if key not in allowed_chars:
            valid = False
            keys += f"{key},"

    if not valid:
        print(f"Reason: Invalid character: {keys}")
        return valid
    else:
        return valid


def check_username(username):
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

    valid = True

    check_leny = check_len(username, valid)
    check_chary = check_char(username, allowed_chars, valid)

    if (not check_chary) or (not check_leny):
        return "Invalid"
    else:
        return "Valid"