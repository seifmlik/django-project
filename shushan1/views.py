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

    for i in range(len(t)):
        print(t[i].capacita)
    return HttpResponse('lééé')


#
# def rabbocco(request, nome):
#     f = Batterie.objects.get(nomebatterie=nome)
#
#     m = Barile.objects.filter(bat=f)
#     t=m[::-1]
#     print(t)
#     r = []
#     for i in range(len(t)):
#         s = i
#         while (t[i].capacita < t[i].capacitamax and s < len(t) - 1):
#             d = t[i].capacitamax - t[i].capacita
#             r.append(d)
#             if (t[s + 1].capacita < d and s <= (len(t) - 2)):
#                 r.append(0)
#                 t[i].capacita = t[i].capacita + t[s + 1].capacita
#                 t[s + 1].capacita = 0
#                 s += 1
#
#                 if (s == len(t) - 1):
#                     break
#             else:
#                 t[s + 1].capacita = t[s + 1].capacita - d
#                 t[i].capacita = t[i].capacita + d
#                 s += 1
#     m = []
#
#     for i in r:
#         if (i != 0):
#             m.append(i)
#     h=0
#     for v in t[(len(m) - 1):]:
#         h=h+v.capacita
#     print(h)
#
#     k = m[:(len(m) - 1)] + [h]
#     print(k)
#
#     j = range(len(t) - 1)
#
#     for i in range(len(m) - 1):
#         print("e venuta a " + str(i) + " " + str(k[i]) + " litri" + " venuta da " + str(i + 1))
#         f = models.Rabbocco(barileorigine=str(t[i+1]), bariledestinazione=str(t[i]), quantita=int(k[i]))
#         print(str(t[i]),t[i].capacitamax,t[i].precedente,t[i].prossimo,t[i].capacita,t[i].tipolegno)
#         ne = models.Barile(nomeb=str(t[i]), capacitamax=int(t[i].capacitamax), precedente=str(t[i].precedente),
#                             prossimo=str(t[i].prossimo),
#                             capacita=int(t[i].capacita),
#                             tipolegno=str(t[i].tipolegno),bat=t[i].bat)
#         ne.save()
#
#         f.save()
#     # print("e venuta a " + str(i + 1) + " " + str(k[i + 1]) + " litri" + " venuta da " + str(j[(len(m)):]))
#     f = models.Rabbocco(barileorigine=str(j[(len(m)):]), bariledestinazione=str(t[i+1]), quantita=int(k[i+1]))
#     f.save()
    # for i in range(len(t)):
    #     try:
    #         ne = models.Barile(nomeb=str(t[i]), capacitamax=int(t[i].capacitamax), precedente=str(t[i].precedente),
    #                        prossimo=str(t[i].prossimo),
    #                        capacita=int(t[i].capacita),
    #                        tipolegno=str(t[i].tipolegno), bat=t[i].bat)
    #         ne.save()
    #     except:
    #         return HttpResponse('lééé')

















    #"-----------------------------------------------------------------------------------------------------------

    #
    # print(" --------------------------")
    #
    # v1 = (m[3].capacitamax - m[3].capacita)
    # if (m[2].capacita <= v1):
    #     print("barile twali feha" + str(m[2].capacita + m[3].capacita))
    #     v1 = m[3].capacitamax - (m[2].capacita + m[3].capacita)
    #     print(v1)
    # else:
    #     # 50-25=25 v1 e la differenza //ob
    #     print('hedhi el barile e sghira ken feha 25 walet  =' + str(v1 + m[3].capacita))  # 50
    #     br3 = (m[2].capacita - v1)  # 150-25=125 na9esna li hazineh
    #     print("li 9balha 9adech wala feha =" + str(br3))  # 125
    #     f=models.Rabbocco(barileorigine=str(m[2]),bariledestinazione=str(m[3]),quantita=v1)
    #     f.save()
    #
    #
    # # -------------------------------------------------------------------------
    # print(" --------------------------")
    # v2 = (m[2].capacitamax - br3)  # (200-125)
    # if (m[1].capacita <= v2):
    #     print("barile twali feha" + str(m[1].capacita + m[2].capacita))
    #     v1 = m[3].capacitamax - (m[1].capacita + m[2].capacita)
    #     print(v2)
    # else:
    #
    #     print('kif 3abina li 9bal lekhra =' + str(br3 + v2))  # 125+75=200
    #     br2 = (m[1].capacita - v2)
    #     print("ethenia walet =" + str(br2))
    #     g= models.Rabbocco(barileorigine=str(m[1]), bariledestinazione=str(m[2]), quantita=v2)
    #     g.save()
    #
    # # -------------------------------------------------------------------------------
    #
    # if (br2 == 0 and m[0].capacita <= m[1].capacitamax):
    #
    #     print("ethenia 3abineha belekhra =" + str(br2 + m[0].capacita))
    #     m[0].capacita = 0
    #     print("lekhra 9adech wala feha " + str(m[0].capacita - br2 + m[0].capacita))
    # else:
    #     print(" --------------------------")
    #
    #     print("li 9bal lekhra = " + str(br2 + (m[1].capacitamax - br2)))
    #     e = m[0].capacita - (m[1].capacitamax - br2)
    #     print("lekhra" + str(e))
    #     h = models.Rabbocco(barileorigine=str(m[0]), bariledestinazione=str(m[1]), quantita=(m[1].capacitamax - br2))
    #     h.save()

    # t = len(m)-2
    # for i in range (0,len(m)):
    #
    #     s=((m[len(m)-i-1].capacitamax)-m[len(m)-i-1].capacita)
    #     print(str(m[len(m)-i-1].capacitamax)+"-"+str(+m[len(m)-i-1].capacita)+"="+str(s))
    #     m[len(m) - i - 1].capacita=m[len(m)-i-1].capacitamax
    #
    #
    #
    #     if(t>=0):
    #         print("old cap pros" + str(m[t].capacita))
    #         print("new cap pros"+str(m[t].capacita-s))
    #         print(str(s)+"arriva da "+str(m[t])+"e va a"+str(m[len(m)-i-1]))
    #         t=t-1

    # print(m[len(m) - i - 2].capacita-s)
    # b= Barile.objects.get(nomeb=nome)
    # c=Barile.objects.get(nomeb='br2')
    #
    # # s=c.capacitamax-c.capacita
    # # b.capacita=b.capacita-s
    # # c.capacita=c.capacitamax
    # # print(str(s)+"venuta da "+str(c.nomeb))
    # # print(str(b.capacita)+" "+ str(c.capacita))
    # # b.save()
    # # c.save()
    # return HttpResponse('sallem')
