from django.http import JsonResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Contributor, SalavatCollection
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def send_salavat(request, name: str, number: str):
    if (q:=Contributor.objects.filter(name=name)).exists():
        contributor = q.first()
    else:
        contributor = Contributor.objects.create(name=name)

    SalavatCollection.objects.create(number=number, contributor=contributor)

    return JsonResponse({
        'ok': True
    })

@csrf_exempt
def home(request):
    return render(request, 'core/index.html')