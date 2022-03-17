def login_in(first, last, idnumber):
    #taking first 3 letter of the name
    set1 = first[0:3]
    set2 = last[0:3]
    set3 = idnumber[-3 :]
    login = set1 + set2 + set3
    return login

def valid_password(password):

   correct_length = False
   has_uppercase = False
   has_lowercase = False
   has_digit = False

   if len(password) >= 7:
       correct_length = True
       for ch in password:
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


