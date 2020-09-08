from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from shushan1.models import Barile, Batterie,Rabbocco
from datetime import datetime


# Create your views here.
def index(request):
    data = models.Batterie.objects.all()
    return render(request, 'index.html', {'d': data})


def getbarile(request, nome):
    f = models.Batterie.objects.get(nomebatterie=str(nome))
    d = models.Barile.objects.filter(bat=f)

    return render(request, 'page.html', {'d': d})


def get(request, nome):
    a = models.Barile.objects.get(nomeb=nome)
    return render(request, 'page1.html', {'a': a})


def get2(request, nome):
    old = models.Barile.objects.get(nomeb=nome)
    ss = models.Batterie.objects.get(nomebatterie=str(old.bat.nomebatterie))

    new = models.Barile(nomeb=nome, capacita=int(request.POST['capacita']) + int(old.capacita),
                        tipolegno=request.POST['tipo'], bat=ss)
    new.save()
    info = models.Info(date=datetime.now(), operation='aggiunto', acapacita=int(request.POST['capacita']),
                       tipoaggiunto=str(request.POST['check']), nomebarile=nome)
    info.save()

    return HttpResponseRedirect('/page/' + old.bat.nomebatterie)


def prel(request, nome):
    b = models.Barile.objects.get(nomeb=nome)
    return render(request, 'page2.html', {'b': b})


def prelback(request, nome):
    old = models.Barile.objects.get(nomeb=nome)
    ss = models.Batterie.objects.get(nomebatterie=str(old.bat.nomebatterie))

    new = models.Barile(nomeb=nome, capacitamax=request.POST['capacitamax'], precedente=request.POST['precedente'],
                        prossimo=request.POST['prossimo'], capacita=int(old.capacita) - int(request.POST['capacita']),
                        tipolegno=request.POST['tipo'], bat=ss)
    new.save()
    info = models.Info(date=datetime.now(), operation='prelevio', acapacita=int(request.POST['capacita']),
                       tipoaggiunto='prelevio', nomebarile=nome)
    info.save()

    return HttpResponseRedirect('/page/' + old.bat.nomebatterie)


def rabbocco(request, nome):
    f = Batterie.objects.get(nomebatterie=nome)
    m = Barile.objects.filter(bat=f)
    t = m[::-1]
    print(t)
    r = []
    if(t[0].capacita==t[0].capacitamax):
        return HttpResponse("non puoi fare il rabbocco")
    else:
        for i in range(len(t)):
            s=i
            while (t[i].capacita < t[i].capacitamax and s < len(t) - 1):
                d = t[i].capacitamax - t[i].capacita
                if (t[s + 1].capacita >= d):
                    r.append(d)
                    print("e venuta a " + str(t[i].nomeb) + " " + str(d) + " litri" + " venuta da " + str(t[s + 1].nomeb))
                    f = models.Rabbocco(barileorigine=str(t[s + 1].nomeb), bariledestinazione=str(t[i].nomeb),
                                    quantita=int(d))
                    f.save()
                if (t[s + 1].capacita < d and s <= (len(t) - 2)):
                    t[i].capacita = t[i].capacita + t[s + 1].capacita
                    r.append(t[s + 1].capacita)
                    print("e venuta a " + str(i) + " " + str(t[s + 1].capacita) + " litri" + " venuta da " + str(s + 1))
                    f = models.Rabbocco(barileorigine=str(t[s+1].nomeb), bariledestinazione=str(t[i].nomeb),
                                    quantita=int(t[s + 1].capacita))
                    f.save()
                    t[s + 1].capacita = 0
                    s+=1
                    if (s == 3):
                        break
                else:
                    t[s + 1].capacita = t[s + 1].capacita - d
                    t[i].capacita = t[i].capacita + d
                    s += 1

    if (m[0].capacita == t[0].capacitamax):
        return HttpResponse(str(t[0].capacita)+str(t[0].capacitamax)+str(t[1].capacita)+str(t[1].capacitamax)+str(t[2].capacita)+str(t[2].capacitamax)+str(t[3].capacita)+str(t[3].capacitamax))
    else:
        for i in range(len(t)):
            ne = models.Barile(nomeb=str(t[i].nomeb), capacitamax=int(t[i].capacitamax), precedente=str(t[i].precedente),prossimo=str(t[i].prossimo),capacita=int(t[i].capacita),tipolegno=str(t[i].tipolegno), bat=t[i].bat)
            ne.save()
        return  HttpResponse('done')



