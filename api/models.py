from django.db import models


class Manual(models.Model):
    name = models.CharField(
        verbose_name='Наименование справочника',
        max_length=200,
        unique=False,
    )
    short_name = models.CharField(
        verbose_name='Короткое наименование',
        max_length=50,
        unique=False,
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=200,
        null=True,
        blank=True,
    )
    version = models.CharField(
        verbose_name='Версия',
        max_length=200,
        db_index=True,
    )
    commencement_date = models.DateField(
        verbose_name='Дата начала действия справочника',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'version'],
                name='unique_Version'
            )
        ]

    def __str__(self):
        return f'Справочник: {self.name}. Версия: {self.version}'


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
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочника'

    def __str__(self):
        return f'Справочник: {self.manual}. Значение: {self.value_unit}'
