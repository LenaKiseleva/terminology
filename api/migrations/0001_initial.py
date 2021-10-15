# Generated by Django 2.2 on 2021-10-15 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Наименование справочника')),
                ('slug', models.SlugField(unique=True, verbose_name='Короткое наименование')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='Описание')),
                ('version', models.CharField(max_length=200, unique=True, verbose_name='Версия')),
                ('commencement_date', models.DateField(verbose_name='Дата начала действия справочника этой версии')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Справочник',
                'verbose_name_plural': 'Справочники',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='UnitManual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_unit', models.CharField(max_length=200, verbose_name='Код элемента')),
                ('value_unit', models.CharField(max_length=200, verbose_name='Значение элемента')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('manual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='api.Manual')),
            ],
            options={
                'verbose_name': 'Элемент справочника',
                'verbose_name_plural': 'Элементы справочника',
                'ordering': ('-pub_date',),
            },
        ),
    ]
