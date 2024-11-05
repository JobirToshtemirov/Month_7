from django.urls import path
from .views import UserRegisterView, DebtListView, CreateDebtView, close_debt, AllDebtsView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('debts/', DebtListView.as_view(), name='debt-list'),
    # path('debts2/', all_debts, name='test'),
    path('debts/create/', CreateDebtView.as_view(), name='create-debt'),
    path('debts/close/', close_debt, name='close-debt'),
    path('debts/all/', AllDebtsView.as_view(), name='all-debts'),
]
