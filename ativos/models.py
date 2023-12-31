from django.db import models

class Ativo(models.Model):
    date = models.CharField(
        verbose_name = "Data da cotação do ativo",
        max_length = 10,
    )

    open = models.CharField(
        verbose_name = "Preço de abertura",
        max_length = 10,
    )

    high = models.CharField(
        verbose_name = "Preço mais alto",
        max_length = 10,
    )

    low = models.CharField(
        verbose_name = "Preço mais baixo",
        max_length = 10,
    )

    close = models.CharField(
        verbose_name = "Preço de fechamento",
        max_length = 10,
    )

    adj_close = models.CharField(
        verbose_name = "Preço adjacente de fechamento",
        max_length = 10,
    )

    volume = models.CharField(
        verbose_name = "Volume",
        max_length = 20,
    )

    class Meta:
        verbose_name = "Ativo"
        verbose_name_plural = "Ativos"