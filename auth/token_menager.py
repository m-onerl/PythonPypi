class TokenManager:
    def __init__(self, initial_token):
        self.token = initial_token

    def get_token(self):
        return self.token

    def set_token(self, new_token):
        self.token = new_token
