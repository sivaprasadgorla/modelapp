from django.contrib import admin
from django.urls import path
from modelapp.views import HomeView,InsertInput,InserView,DisplayView,DeleteInputView,DeleteView,UpdateInputView,UpdateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('modelapp/',HomeView.as_view()),
    path('modelapp/insertinput/',InsertInput.as_view()),
    path('modelapp/insertinput/insert/',InserView.as_view()),
    path('modelapp/display/',DisplayView.as_view()),
    path('modelapp/deleteinput/',DeleteInputView.as_view()),
    path('modelapp/deleteinput/delete/',DeleteView.as_view()),
    path('modelapp/updateinput/',UpdateInputView.as_view()),
    path('modelapp/updateinput/update/',UpdateView.as_view()),
]
