from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Widoki naszej apki, renderujemy htmle zwracamy/wyświetlamy templatki
def contact(request):
    # request przekazuje obiekt z danymi żądania HTTP z przeglądarki
    return render(request, 'contact/contact.html')

def hello(request):
    return render(request, 'contact/hello.html')