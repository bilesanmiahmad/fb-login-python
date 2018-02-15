import requests


def get_access_token(app_id, app_secret, redirect_uri, code):
    """
    This method gets the access token that helps you get
    user details from facebook. The code argument is
    retrieved from the url after the user has accepted
    the permissions of your app from facebook
    :param app_id:
    :param app_secret:
    :param redirect_uri:
    :param code:
    :return file.json:
    """
    payload = {'client_id': app_id, 'redirect_uri': redirect_uri, 'client_secret': app_secret, 'code': code}
    access_data = requests.post('https://graph.facebook.com/v2.10/oauth/access_token?', params=payload)
    return access_data.json()


def get_user_data(access_code):
    """
    This method is used to retrieve user data from facebook.
    The data retrieved depends on the permissions granted by
    the user.
    :param access_code:
    :return file.json:
    """
    fields = 'id,first_name,gender,email,picture,age_range,last_name,birthday,favorite_athletes,favorite_teams,location,relationship_status,languages,link,cover,friends'
    payload = {'access_token': access_code, 'fields': fields}
    user_data = requests.get('https://graph.facebook.com/v2.7/me?', params=payload)
    return user_data.json()
