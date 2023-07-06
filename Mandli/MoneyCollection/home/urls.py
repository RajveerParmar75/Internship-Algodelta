from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView,MyTokenObtainPairView,AdminRegister,Saving_accountView,AgentRegister,Saving_TransectionView,Loan_TransectionView,Loan_accountView

urlpatterns = [
    path('register', RegisterView().as_view(), name='REGISTER USER'),
    path('api/token/', MyTokenObtainPairView().as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/admin', AdminRegister().as_view(), name='admin register'),
    path('register/agent', AgentRegister().as_view(), name='AGENT USER '),
    path('saving', Saving_accountView().as_view(), name='Saving register'),
    path('loan', Loan_accountView().as_view(), name='Loan register'),
    path('saving/transection',Saving_TransectionView().as_view(),name='add saving transection'),
    path('loan/transection', Loan_TransectionView().as_view(), name='add loan transection'),
]
