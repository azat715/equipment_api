import pytest
import re
from django.core.exceptions import ValidationError

from main.pattern_convert import convert

# серийный номер A3BFRGT0AS
# маска XXAAAAAXAA

MASK = "XXAAAAAXAA"

def test_convert():
    assert str(convert(MASK)) == str(re.compile('^[A-Z-0-9][A-Z-0-9][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z-0-9][A-Z][A-Z]$'))


def test_convert():
    with pytest.raises(ValidationError):
        convert("XXAAAAAX?A")