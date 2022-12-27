from django.shortcuts import render
from . models import Lession,LessionScore
from . forms import LessionForm

def IndexView(request):
    lessions = Lession.objects.all()
    lessionscore = LessionScore()
    if request.method == 'POST':
        form = LessionForm(request.POST)
        if form.is_valid():
            form.save()        
    else:
        form = LessionForm()

    context={
        'lessions':lessions,
        'form':form,
        'chartdata':lessionscore.avrage()
    }

    return render(request,'dashboard/index.html',context)