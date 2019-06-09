__author__ = "RituRaj"


from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def check_credentials(username, password):
    """Check Creadentials of the User

    :param username: username
    :param password: password entered at the time of registeration

    :return user_instance/None , boolean, True/False
            user_instance , True - > user exist and authenticated 
                            False - > user exist , but not authenticated
            user_instance , False -> User does not exist , not authennticated
    """
    try:
        u = User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        if user:
            return u, True
        else:
            return u, False

    except User.DoesNotExist:
        return None, False
