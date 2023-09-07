from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class Utils:

    @staticmethod
    def get_token_for_user(user):
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)
        return{
            'refresh': str(refresh),
            'access': str(access)
        }

