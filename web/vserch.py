def search4vowels(phrase:str) -> set:
    """Возвращает гласные, найденые в указаной фразе."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Возвращает найденые указаные буквы во фразе"""
    return set(letters).intersection(set(phrase))
