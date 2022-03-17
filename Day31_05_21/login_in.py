def login_in(name, last, id):
    set1 = name[0:3]
    set2 = last[0:3]
    id_n = id[-3:]

    login_n = set1 + set2 + id_n
    return login_n

def valid_passw(passw):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    if len(passw) >= 7:
        correct_length = True
        for ch in passw:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False
    return is_valid


