import re


def validate_password(password):
    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    if len(password) < 8:
        return False
    if not any(l.isupper() for l in password):
        return False
    if not any(l.isdigit() for l in password):
        return False
    if regex.search(password) is None:
        return False
    return True


ERROR_MESSAGE = 'Password must have minimum 8 characters, ' \
                'must contain at least one capitalized ' \
                'letter, at least one special character ' \
                'and at least one number!'
