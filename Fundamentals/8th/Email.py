class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails = []

data = input()
while 'Stop' not in data:
    sender, receiver, content = data.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    data = input()

send_emails = [int(el) for el in input().split(', ')]
for index, element in enumerate(emails):
    if index in send_emails:
        emails[index].send()
    print(emails[index].get_info())
# print(emails)
# print(email.get_info())


# Peter John Hi,John
# John Peter Hi,Peter!
# Katy Lilly Hello,Lilly
# Stop
# 0, 2
# Anna, Bella, Hi
# Sam, Dany, Okey
# Felix, Mery, Bye
# Stop
# 0