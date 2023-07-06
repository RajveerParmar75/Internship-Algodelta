from pprint import pprint

import requests
from django.utils.functional import SimpleLazyObject, LazyObject
from django.http import HttpResponseRedirect, HttpResponse
from allauth.socialaccount.models import SocialToken
from django.contrib.auth.models import AnonymousUser
from django.utils.encoding import force_str

def google_login(request):
    return HttpResponseRedirect('/accounts/google/login/')

def google_callback(request):
    try:
        lazy_user = request.user

        # Evaluate the lazy_user to get the actual User object
        user = lazy_user._wrapped if hasattr(lazy_user, '_wrapped') else AnonymousUser()

        # Get the authorization code from the request
        code = request.GET.get('code')

        if code:
            # Exchange the authorization code for an access token
            token_url = 'https://oauth2.googleapis.com/token'
            client_id = 'YOUR_CLIENT_ID'
            client_secret = 'YOUR_CLIENT_SECRET'
            redirect_uri = 'YOUR_REDIRECT_URI'

            payload = {
                'code':code,
                'client_id': '327173967023-b811bmm9obv8bida2qrfkoi35kin6la5.apps.googleusercontent.com',
                'client_secret': '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',
                'redirect_uri': 'http://127.0.0.1:8000/google/callback/',
                'grant_type': 'authorization_code'
            }

            response = requests.post(token_url, data=payload)
            if response.status_code == 200:
                token_data = response.json()
                access_token = token_data['access_token']

                # Save or use the access token as needed
                # For example, you can update the SocialToken for the user
                social_auth = SocialToken.objects.get(user=user, provider='google')
                social_auth.extra_data['access_token'] = access_token
                social_auth.save()

                # Print or return the access token value
                access_token_value = access_token
                print(access_token_value)
                # You can also return the access token value as a response if needed
                return HttpResponse(f'Access Token: {access_token_value}')

        return HttpResponse('Callback completed successfully')

    except Exception as e:
        print(e)
        return HttpResponse('Callback completed with an error')
    # ...