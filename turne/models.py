from django.db import models


class Cantor(models.Model):
    nome = models.CharField(max_length=25)
    estilo = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Pais(models.Model):
    Cont = (
        ('O', 'Oceania'),
        ('A', 'America'),
        ('E', 'Europa'),
        ('F', 'Africa'),
        ('S', 'Asia'),
        ('U', 'Unknow')
    )

    pais = models.CharField(max_length=20)
    data_criacao = models.DateField()
    continente = models.CharField(max_length=1, choices=Cont, blank=False, null=False, default='U')
    populacao = models.CharField(max_length=12)

    def __str__(self):
        return self.pais

class Turne(models.Model):
    MODELO = (
        ('A', 'Acustico'),
        ('B', 'Banda Completa'),
        ('S', 'Solo')
    )
    cantor = models.ForeignKey(Cantor, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=1, choices=MODELO, blank=False, null=False, default='S')