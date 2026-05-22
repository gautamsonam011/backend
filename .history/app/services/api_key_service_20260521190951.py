import secrets


class APIKeyService:

    @staticmethod
    def generate_api_key():

        return secrets.token_hex(32)