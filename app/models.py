class User:
    # variable to store all users registered
    all_users = dict()

    def __init__(self, username, password):
        """User initializer"""
        self.username = username
        self.password = password