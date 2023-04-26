from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import status
class BotUserViewSet(ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['name']
class BotUserInfo(APIView):
    def post(self,request):
        data = request.data 
        user = BotUser.objects.get(telegram_id=data['telegram_id'])
        serializer = BotUserSerializer(instance=user,partial=True)
        return Response(serializer.data)
class BotUserCount(APIView):
    def get(self,request):
        from datetime import datetime,timedelta,date
        today = date.today()
        nextday = today+ timedelta(days=1)
        oneweek = today - timedelta(days=7)
        oneday = today + timedelta(days=1)
        onemonth = today - timedelta(days=30)
        onedayfilter = BotUser.objects.filter(added__range=[today,oneday]).count()
        oneweekfilter = BotUser.objects.filter(added__range=[oneweek,nextday]).count()
        onemonthfilter = BotUser.objects.filter(added__range=[onemonth,nextday]).count()
        allfilter = BotUser.objects.all().count()
        # today_time=datetime.now().strftime("%Y-%m-%d")
        # month_time = datetime.now() - timedelta(days=31)
        # month_time = month_time.strftime("%Y-%m-%d")
        # all = BotUser.objects.all().count()
        # today=BotUser.objects.filter(added=today_time).count()
        # month = BotUser.objects.filter(added__range=[month_time,today_time]).count()
        text =  f"✅ Bugun qo'shilganlar: {onedayfilter}/n" \
                f"✅ Shu oy qo'shilganlar: {onemonthfilter}/n" \
                f"✅ Umumiy obunachilar: {allfilter}"
        return Response(data={'info':text},status=status.HTTP_200_OK)