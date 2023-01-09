from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, AddMachineSerializer, SellSerializer, SellRangeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from .models import Machine, Sell, SellRange
from datetime import date, timedelta


# Create your views here.

class UserListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, formate=None):
        # from user model in built in model get the user last_name
        # for each User objects =>stores  info in user variable.and then access
        cnt = 0
        for user in User.objects.all():
            cnt = cnt + 1
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


# my own hand made custom function that creates user in the database.
class CreateUser(APIView):
    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def get(self, request):
    #     cnt = 0
    #     for user in User.objects.all():
    #         cnt = cnt + 1
    #     return Response(cnt)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


# Add machine views

class Add(APIView):
    def post(self, request):
        add = AddMachineSerializer(data=request.data)
        if add.is_valid():
            add.save()
            return Response(add.data, status=status.HTTP_201_CREATED)
        return JsonResponse(add.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        machine = Machine.objects.all()
        serializer = AddMachineSerializer(machine, many=True)
        return Response(serializer.data)


class MachineList(APIView):
    def get(self, request):
        machine_list = Machine.objects.all()
        serializer = AddMachineSerializer(machine_list, many=True)
        return Response(serializer.data)


class AddSell(APIView):
    def post(self, request):
        sell = SellSerializer(data=request.data)
        if sell.is_valid():
            sell.save()
            return Response(sell.data, status=status.HTTP_201_CREATED)
        return JsonResponse(sell.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, reqeust):
        all_sell = Sell.objects.all()
        serializer = SellSerializer(all_sell, many=True)
        return Response(serializer.data)

#        {
#         "start_date": "2023-01-01",
#         "end_date": "2023-01-06",
#         "machine": 2
#       }
#       post the above json =>total_sells within this day's


class Range(APIView):
    def post(self, request):
        ranges = SellRangeSerializer(data=request.data)
        if ranges.is_valid():
            ranges.save()
            total = 0
            cnt = 0
            sell_objects = Sell.objects.all()
            d = ranges.data["start_date"]
            y = int(d[0:4])
            m = int(d[5:7])
            d = int(d[8:10])
            e = ranges.data["end_date"]
            ye = int(e[0:4])
            me = int(e[5:7])
            de = int(e[8:10])

            start_date = date(y, m, d)
            end_date = date(ye, me, de)
            delta = end_date - start_date  # returns timedelta
            list_date = []
            for i in range(delta.days + 1):
                list_date.append(start_date + timedelta(days=i))

            for x in list_date:
                for y in sell_objects:
                    if y.machine.id == ranges.data["machine"]:
                        if y.date == x:
                            total += y.sell

            # for x in sell_objects:
            #     if x.machine.id == ranges.data["machine"]:
            #         total = total + x.sell

            return Response(total, status=status.HTTP_201_CREATED)
        return JsonResponse(ranges.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, reqeust):
    #     range = SellRange.objects.all()
    #     serializer = SellRangeSerializer(range, many=True)
    #     return Response(serializer.data)
