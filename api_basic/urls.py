from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import article_list, article_detail, ArticleAPIView, ArticleDetail, GenericAPIView, DevicesAPIView,\
                    DevicesDetail, SellsAPIView
urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    path('detail/<int:pk>/', ArticleDetail.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),


    # coffee machine urls
    path('device/', DevicesAPIView.as_view()),
    path('device/detail/<int:pk>/', DevicesDetail.as_view()),
    path('sell/', SellsAPIView.as_view()),
]
