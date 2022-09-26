import pytest
from django.core.exceptions import ValidationError

from main.models import EqptType, Eqpt

# серийный номер A3BFRGT0AS
# маска XXAAAAAXAA

@pytest.mark.django_db
@pytest.fixture(scope='session', name="eqpt_type")
def fixture_eqpt_type(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        EqptType.objects.create(
            name="TP-Link TL-WR74",
            mask="XXAAAAAXAA"
        )


@pytest.mark.django_db
def test_create_eqpt(eqpt_type):
    t = EqptType.objects.get(name="TP-Link TL-WR74")
    Eqpt.objects.create(
        eqpt_type=t,
        serial_number="A3BFRGT0AS",
        comment="test_comment"
    )
    with pytest.raises(ValidationError):
        e = Eqpt(
        eqpt_type=t,
        serial_number="a3BFRGT0AS",
        comment="test_comment"
    )
        e.full_clean()


