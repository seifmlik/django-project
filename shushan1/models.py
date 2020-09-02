
# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class Batterie(models.Model):
    nomebatterie=models.CharField(max_length=20)
    def __str__(self):
        return self.nomebatterie
    def __unicode__(self):
        return self.nomebatterie
class Barile(models.Model):
    nomeb=models.CharField(max_length=20,primary_key=True)
    capacitamax=models.IntegerField()
    precedente=models.CharField(max_length=20)
    prossimo=models.CharField(max_length=20)
    densita=models.IntegerField()
    capacita=models.IntegerField()
    tipolegno=models.CharField(max_length=20)
    bat=models.ForeignKey(Batterie,on_delete=models.CASCADE)
    def __str__(self):
        return self.nomeb

    def __unicode__(self):
        return self.capacita

class Info(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    operation=models.CharField(max_length=50)
    acapacita=models.IntegerField()
    tipoaggiunto=models.CharField(max_length=20)
    nomebarile=models.CharField(max_length=20)
    def __str__(self):
        return (str(self.date)+" "+str(self.operation)+" a "+str(self.nomebarile))


class Rabbocco(models.Model):
    barileorigine=models.CharField(max_length=50)
    bariledestinazione=models.CharField(max_length=50)
    quantita=models.IntegerField()
    def __str__(self):
        return (str(self.barileorigine) + "----->" + str(self.bariledestinazione) + " : " + str(self.quantita))





