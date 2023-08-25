from abc import ABC, abstractmethod


class IContent(ABC):
    @abstractmethod
    def format(self):
        pass


class SenderReceiver:
    @staticmethod
    def format_sender_and_receiver(name):
        return ''.join(["I'm ", name.name])


class ISender(SenderReceiver):
    def __init__(self, sender_name):
        self.name = sender_name


class IReceiver(SenderReceiver):
    def __init__(self, receiver_name):
        self.name = receiver_name


class MyContent(IContent):
    def __init__(self, my_content):
        self.content = my_content

    def format(self):
        return '\n'.join(['<myML>', self.content, '</myML>'])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, contents):
        pass


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.format_sender_and_receiver(sender)

    def set_receiver(self, receiver):
        self.__receiver = receiver.format_sender_and_receiver(receiver)

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):
        template = f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"

        return template


email = Email('IM')

sender = ISender('qmal')
email.set_sender(sender)

receiver = IReceiver('james')
email.set_receiver(receiver)

content = MyContent('Hello, there!')
email.set_content(content)

print(email)
