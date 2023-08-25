class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_LENGTH = 5
email = input()
while email != 'End':

    if email.count('@') != 1:
        raise MustContainAtSymbolError("Email must contain one @")

    username, domain = email.split('@')

    if len(username) < MIN_LENGTH:
        raise NameTooShortError('Name must be more than 4 characters')

    try:
        domain_name, domain_extension = domain.split('.')
        if domain_extension not in ['com', 'bg', 'org', 'net']:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    except ValueError:
        raise InvalidDomainError("Domain must contain dot")

    print('Email is valid')
    email = input()
