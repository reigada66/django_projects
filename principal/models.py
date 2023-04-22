from django.db import models
#from moneyfield import MoneyField

class Servico(models.Model):
#    Preco= MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    Duracao=models.PositiveSmallIntegerField()
    Desc_Serv=models.CharField(max_length=50)
#    imagem = models.ImageField(upload_to='img_serv')

