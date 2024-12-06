from importlib.resources import path

from members.models.teacher import views

urlpatterns = [
    path('teachers/', views.get_teachers, name='teachers'),


]