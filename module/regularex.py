import re

def is_valid_email(addr):
    re.email = re.compile(r'^\w+\.?\w+\@\w+\.com$')
    if re.email.match(addr):
        return True
    else:
        return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):
    re.email = re.compile(r'^<?(\w+\s\w+)?>?\s?(\w+)@(\w+\.org|com)$')
    res = re.email.match(addr)
    if res:
        if res.group(1):
            return res.group(1)
        else:
            return res.group(2)
    else:
        return None
print(name_of_email('<Tom Paris> tom@voyager.org'))
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
print(name_of_email('tom@voyager.org'))
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
