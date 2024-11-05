from django.contrib.auth import login
from rest_framework import generics, permissions, status
from .models import CustomUser, Debt
from .serializers import UserSerializer, DebtSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)


class DebtListView(generics.ListAPIView):
    serializer_class = DebtSerializer

    def get_queryset(self):
        user = self.request.user
        return Debt.objects.filter(borrower=user)


# def all_debts(request):
#     data = Debt.objects.all()
#     serial = DebtSerializer
#     return Response(data=serial, status=status.HTTP_200_OK)


class CreateDebtView(generics.CreateAPIView):
    model = Debt
    serializer_class = DebtSerializer

    # def perform_create(self, serializer):
    #     serializer.save(Debt.borrower)


@api_view(['POST'])
def close_debt(request):
    debt_id = request.data.get('debt_id')
    try:
        debt = Debt.objects.get(id=debt_id, borrower=request.user)
        debt.is_closed = True
        debt.save()
        return Response({'message': 'Debt closed successfully'})
    except Debt.DoesNotExist:
        return Response({'error': 'Debt not found'}, status=404)


class AllDebtsView(generics.ListAPIView):
    serializer_class = DebtSerializer

    def get_queryset(self):
        return Debt.objects.all()
