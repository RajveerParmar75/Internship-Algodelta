from django.urls import path,include
from .Register.views import RegisterView
from .Token.views import MyTokenObtainPairView
from .Org.docs.views import DocsViews
from .Admin.org.views import OrganizationView
from .Admin.login_track.views import MonitorView
from .Admin.space.views import SpaceView
from .User.views import UserDocsView
from .type_of_user.views import User_TypeViews
from .state.views import StateViews
from .city.views import CityViews
urlpatterns = [
    path('register',RegisterView().as_view(),name='REGISTER USER'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('docs', DocsViews.as_view(), name='UPLODE FILE'),
    path('registerOrganization', OrganizationView().as_view(), name='register org'),
    path('monitor', MonitorView().as_view(), name='site monitor for admin'),
    path('space', SpaceView().as_view(), name='allocate space for org'),
    path('download', UserDocsView().as_view(), name='download file'),
    path('type_of_user', User_TypeViews().as_view(), name='register the type of user'),
    path('city', CityViews().as_view(), name='city'),
    path('state', StateViews().as_view(), name='state'),
]