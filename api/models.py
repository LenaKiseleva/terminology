from django.db import models


class Manual(models.Model):
    name = models.CharField(
        verbose_name='Наименование справочника',
        max_length=200,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Короткое наименование',
        max_length=50,
        unique=True,
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=200,
        null=True,
    )
    version = models.CharField(
        verbose_name='Версия',
        max_length=200,
        unique=True,
    )
    commencement_date = models.DateField(
        verbose_name='Дата начала действия справочника этой версии',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'

    def __str__(self):
        return f'Справочник {self.name}. Версия {self.version}'


class UnitManual(models.Model):
    manual = models.ForeignKey(
        Manual,
        on_delete=models.CASCADE,
        related_name='units',
    )
    code_unit = models.CharField(
        verbose_name='Код элемента',
        max_length=200,
    )
    value_unit = models.CharField(
        verbose_name='Значение элемента',
        max_length=200,
    )