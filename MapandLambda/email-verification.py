You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The maximum length of the extension is 3

. 

import re
def fun(s):
    ##if re.findall(r'[\w\.-]+@\w+[.]+\w+',s):
    if re.match(r'^[-\w]+@[a-zA-Z\d]+\..{1,3}$',s):
        return True
    else:
        return False
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails