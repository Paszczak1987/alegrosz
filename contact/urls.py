from django.urls import path
# Importujemy wszystko z views.py
from . import views

# Warto ustawić przestrzeń nazw żeby uniknąć konfliktów.
app_name = 'contact'



# Tutaj definiujemy URLe naszej apki.
urlpatterns = [
    # Lista URLi naszej apki django
    path('contact/', views.contact, name='contact'),
    path('contact/hello', views.hello, name='hello'),
]
