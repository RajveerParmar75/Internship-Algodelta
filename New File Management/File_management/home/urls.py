
from django.urls import path
from .views import RegisterView
from .Token.views import MyTokenObtainPairView
from .views import UploadFile,OrganizationViews,AdminView
urlpatterns = [
    path('register', RegisterView().as_view(), name='REGISTER USER'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('upload',UploadFile().as_view(), name='upload for user by org'),
    path('org',OrganizationViews().as_view(), name='upload org'),
    path('view/admin',AdminView().as_view(), name='admin'),
]
