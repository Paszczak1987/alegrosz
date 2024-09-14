# Alegrosz


## Algorytm tworzenia funkcjonalności w django

1. Czy potrzebne nowe django apps?
   - `django-admin startapp <name>`
   - rejestruję w settings.py -> INSTALLED_APPS

2. Czy potrzebne dane?
   - tworzę model w <appname>/models.py
   - `python manage.py makemigrations <appname>`
   - `python manage.py migrate <appname>`

3. Czy potrzebuję obsługę w CMS (Django Admin)
   - rejestruję modele w <app_name>/admin.py

4. Czy potrzebna jest logika? (View)
    - <app_name>/views.py
   
5. Czy potrzebny jest routing?