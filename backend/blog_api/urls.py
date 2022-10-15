# from django.urls import path
# from .views import PostList, PostDetail
from .views import PostList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('', PostList, basename='post')

urlpatterns = router.urls





# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
#     path('', PostList.as_view(), name='listcreate'),
# ]