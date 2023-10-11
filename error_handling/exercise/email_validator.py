class NameTooShortError(Exception):
    """ Raise this error when the name in the email is less than or equal to 4 chars"""


class MustContainAtSymbolError(Exception):
    """ Raise this error when there is no "@" symbol in the email """


class InvalidDomainError(Exception):
    """ Raise this error when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org) """


VALID_DOMAINS = ['com', 'bg', 'org', 'net']

while True:
    email = input()
    if email == 'End':
        break

    if '@' in email:
        name_email, domain = email.split('@')[0], email.split('@')[1]
        domain = domain.split('.')[1]
        if len(name_email) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        elif domain not in VALID_DOMAINS:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        else:
            print('Email is valid')
    elif '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")