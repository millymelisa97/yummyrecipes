class User:
    all_users = dict()

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        """ Registers a user """
        if str(self.username) not in User.all_users:
            User.all_users[str(self.username)] = self.get_details()
            return self.get_details()
        return False

    def get_details(self):
        return {
            "username": self.username,
            "password": self.password
        }
