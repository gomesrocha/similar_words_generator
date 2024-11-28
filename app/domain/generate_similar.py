import random


CHARACTER_MAP = {
    "a": ["@", "4", "á", "â"],
    "c": ["ç", "¢", "©"],
    "e": ["3", "€", "ê"],
    "i": ["1", "!", "|"],
    "o": ["0", "°", "ö"],
    "s": ["$", "5", "§"],
    "u": ["ú", "ü", "û"],
    "h": ["#", "ĥ"],
    "w": ["vv", "ẃ"],
}

def generate_variations(word: str, max_variations: int) -> list:
    variations = set()

    # Substituir caracteres por equivalentes no CHARACTER_MAP
    for _ in range(max_variations * 2):  # Gerar mais variações para filtrar
        variation = list(word)
        for idx, char in enumerate(variation):
            if char.lower() in CHARACTER_MAP:
                # Substitui com chance aleatória
                if random.random() > 0.5:
                    variation[idx] = random.choice(CHARACTER_MAP[char.lower()])
        variations.add("".join(variation))

    # Limitar o número de variações e evitar duplicatas
    return list(variations)[:max_variations]
