import re

class EmailAddressParser:

  def __init__(self, str):
    self.email_addresses = str

  def parse(self):
    print(self.email_addresses)
    split_pattern = re.compile(r"\s|,\s?")
    emails = sorted(split_pattern.split(self.email_addresses))
    print(emails)

    validate_pattern = re.compile(r'[\w.]*@\w*')
    valid_emails = [email for email in emails if validate_pattern.match(email)]
    print(valid_emails)
    return valid_emails