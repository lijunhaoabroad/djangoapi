
from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet, ArticleGenericViewSet, ArticleModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('article-gv', ArticleGenericViewSet, basename='article-gv')
router.register('article-m', ArticleModelViewSet, basename='article-m')


urlpatterns = [

    # ViewSet ways of api
    path('viewset/', include(router.urls)),


    # traditional ways of api
    # path('article/', article_list),
    # path('article/<int:id>/', article_detail),


    # APIVIEW ways of api
    path('article/', ArticleAPIView.as_view()),
    path('article/<int:id>/', ArticleDetails.as_view()),

    # Generic ways of api
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),


]
