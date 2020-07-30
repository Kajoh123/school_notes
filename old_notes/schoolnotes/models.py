from django.db import models

class Subject(models.Model):
    name = models.CharField(verbose_name='Nazwa', max_length=120)
    teacher = models.CharField(verbose_name='Nauczyciel', max_length=120)

    def __str__(self):
        return f'{self.name}'

class Lesson(models.Model):
    topic = models.CharField(verbose_name='Temat', max_length=120)
    description = models.TextField(verbose_name='Opis', max_length=1000, blank=True, default='Brak opisu')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Przedmiot')
    date = models.DateField(verbose_name='Data')

    def __str__(self):
        return f'{self.subject.name} {self.date}'
