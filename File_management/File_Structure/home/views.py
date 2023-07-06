import jwt


# Create your views here.
def check_position(token):
    decoded_token = jwt.decode(token, 'django-insecure-8ukakv1a+p-u!)l11082m1f!%q3%hqneffuj7f^(=tr=5!s2@_',
                               algorithms=['HS256'])
    if decoded_token['type'] == 1:
        return 'user'
    elif decoded_token['type'] == 2:
        return 'org'
    elif decoded_token['type'] == 3:
        return 'admin'

