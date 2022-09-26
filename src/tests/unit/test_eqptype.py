import pytest
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from main.models import EqptType

@pytest.mark.django_db
def test_create_eqpt_type():
    EqptType.objects.create(
        name="D-Link DIR-300",
        mask="NXXAAXZXaa"
    )


@pytest.mark.django_db
def test_duplicate_eqpt_type():
    with pytest.raises(IntegrityError):
        EqptType.objects.create(
        name="TP-Link TL-WR74",
        mask="XXAAAAAXAA"
        )

        EqptType.objects.create(
            name="TP-Link TL-WR74",
            mask="XXAAAAAXAA"
        )


@pytest.mark.django_db
def test_eqpt_type_error_mask():
    with pytest.raises(ValidationError):
        e = EqptType(
            name="TP-Link TL-WR74",
            mask="error"
        )
        e.full_clean()
    