from django.db import models
from django.contrib.auth.models import User

class Zapis(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО клиента")
    email = models.EmailField(verbose_name="Email клиента")
    phone = models.CharField(max_length=20, verbose_name="Телефон клиента")
    excurse = models.CharField(max_length=200, verbose_name="Экскурсия")
    date = models.DateField(verbose_name="Дата экскурсии")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заявки")

    def __str__(self):
        return f"{self.name} - {self.excurse} ({self.date})"

    class Meta:
        verbose_name = "Запись на экскурсию"
        verbose_name_plural = "Записи на экскурсии"

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    value = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    pass  
