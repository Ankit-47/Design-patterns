class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class EmailNotifier(Observer):
    def update(self, message):
        print(f"📧 Email Notification: {message}")

class SMSNotifier(Observer):
    def update(self, message):
        print(f"📱 SMS Notification: {message}")

# Usage
subject = Subject()
email_observer = EmailNotifier()
sms_observer = SMSNotifier()

subject.attach(email_observer)
subject.attach(sms_observer)

subject.notify("New product launched!")