# import sys
# print(sys.version)
import time


class Messenger:
    db = []
    requested_count = 0

    def send_message(self, name, text):
        timestamp = time.asctime()
        self.db.append({
            'name': name,
            'text': text,
            'timestamp': timestamp
        })

    def get_messages(self):
        return self.db

    def get_new_messages(self):
        new_messages = self.db[self.requested_count:]
        self.requested_count += len(new_messages)
        return new_messages


messenger = Messenger()
messenger.send_message('Jack', '123')
messenger.send_message('Jack', '1234')
print(messenger.get_new_messages())

messenger.send_message('Black', 'Hell o!')
print(messenger.get_new_messages())

# def foo(bar):
#   bar = bar * 2
#   return bar

# result = foo(5)
# print(result)

# print("MELT NUBASOV UBIVAET")
