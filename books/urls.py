from django.urls import path
from .views import BookListApiView,BookDetailApiView,\
    BookDeleteApiView,BookUpdateApiView, BookCreateApiView,BookCreateListApiView, BookUpdateDeleteApiView, BookViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')







urlpatterns = [
    path('books/', BookListApiView.as_view() , name='book_api'),
    path('book/', BookCreateListApiView.as_view()),
    path('bookupdatedelete/<int:pk>', BookUpdateDeleteApiView.as_view()),
    path('books/create', BookCreateApiView.as_view()),
    path('books/<int:pk>/', BookDetailApiView.as_view()),
    path('books/<int:pk>/delete', BookDeleteApiView.as_view()),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
]

urlpatterns = urlpatterns + router.urls