import re

from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from main.pattern_convert import convert

MASK_PATTERN = re.compile("^[NAaXZ]+$")
MASK_VALIDATOR = RegexValidator(re.compile(MASK_PATTERN))


class EqptType(models.Model):
    """Тип оборудования"""

    name = models.CharField(
        verbose_name="Наименование типа", max_length=252, unique=True
    )
    mask = models.CharField(
        verbose_name="Маска серийного номера",
        max_length=255,
        unique=True,
        validators=[MASK_VALIDATOR],
    )

    class Meta:
        verbose_name = "Тип оборудования"

    def __str__(self):
        return "{self.name}".format(self=self)


class Eqpt(models.Model):
    """Оборудование"""

    eqpt_type = models.ForeignKey(
        EqptType, related_name="eqpts", on_delete=models.PROTECT
    )
    serial_number = models.CharField(
        verbose_name="Серийный номер", max_length=255, unique=True
    )
    comment = models.TextField()
    deleted = models.BooleanField(default=False)

    def clean(self):
        """кастомная валидацаия serial_number"""
        pattern = convert(self.eqpt_type.mask)
        if not re.fullmatch(pattern, self.serial_number):
            raise ValidationError(f"Невалидный серийный номер: {self.serial_number}")

    class Meta:
        verbose_name = "Оборудование"

    def __str__(self):
        return "{self.serial_number}".format(self=self)
