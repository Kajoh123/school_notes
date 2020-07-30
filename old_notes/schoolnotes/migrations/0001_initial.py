# Generated by Django 3.0.8 on 2020-07-26 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nazwa')),
                ('teacher', models.CharField(max_length=120, verbose_name='Nauczyciel')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=120, verbose_name='Temat')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Opis')),
                ('date', models.DateField(verbose_name='Data')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolnotes.Subject', verbose_name='Przedmiot')),
            ],
        ),
    ]