from django.urls import path
from .Teacher.views import TeacherView
from .Student.views import StudentView
from .HOD.views import HodView
from .Register.views import RegisterView
from .Time_Table.views import Time_Table_Views
from .Teacher.subject.views import SubjectView
from .Grade.views import GradeView
from .Grade.expence import get_expence
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .Token.views import MyTokenObtainPairView
urlpatterns = [
    path('teacher',TeacherView().as_view(),name='TEACHER DETAIL'),
    path('student', StudentView().as_view(), name='STUDENT DETAIL'),
    path('hod', HodView().as_view(), name='HOD DETAIL'),
    path('register',RegisterView().as_view(),name='REGISTER USER'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('timetable', Time_Table_Views().as_view(), name='TIME TABLE'),
    path('Subject', SubjectView().as_view(), name='SUBJECT'),
    path('grade', GradeView().as_view(), name='GRADE'),
    path('expense', get_expence, name='expense'),
]
