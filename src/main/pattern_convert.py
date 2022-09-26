"""    
• N – цифра от 0 до 9;
• A – прописная буква латинского алфавита;
• a – строчная буква латинского алфавита;
• X – прописная буква латинского алфавита либо цифра от 0 до 9;
• Z –символ из списка: “-“, “_”, “@”.    
"""


import re
from typing import List

from django.core.exceptions import ValidationError

mapping = {
    "N": "[0-9]",
    "A": "[A-Z]",
    "a": "[a-z]",
    "X": "[A-Z-0-9]",
    "Z": "[_-@]"
}


def convert(s: str) -> re.Pattern:
    """конвертирование строк в паттерн

    Args:
        s (str): EqptType.mask

    Raises:
        ValidationError: если символ не входит в mapping.values

    Returns:
        Pattern: паттерн регулярки
    """
    try:
        arr: List[str] = [mapping[i] for i in s]
    except KeyError as e:
        raise ValidationError(f"Неправильная маска EqptType: {e}")
        
    return re.compile(f"^{''.join(arr)}$")
            

