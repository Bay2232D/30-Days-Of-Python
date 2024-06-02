class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

class UserReport:
    @staticmethod
    def print_user_report(users):
        for user in users:
            print(f'User: {user.name}, Email: {user.email}')

# Creating User objects
user1 = User('Alice', 'alice@example.com')
user2 = User('Bob', 'bob@example.com')

# Creating UserManager object and adding Users
user_manager = UserManager()
user_manager.add_user(user1)
user_manager.add_user(user2)

# Creating UserReport object and printing the report
user_report = UserReport()
user_report.print_user_report(user_manager.users)
