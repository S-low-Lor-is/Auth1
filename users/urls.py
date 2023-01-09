from django.urls import path
from .views import UserListView, CreateUser, Add, MachineList, AddSell, Range, RegisterView
# have one url in auth1 urls section
urlpatterns = [
    path('', UserListView.as_view(), name='user-list-view'),
    path('create-user/', RegisterView.as_view()),
    path('add-machine/', Add.as_view()),
    path('machine-list/', MachineList.as_view()),
    path('add-sell/', AddSell.as_view()),
    path('range-sell/', Range.as_view())
]
