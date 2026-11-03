from main import get_response, parse_extraction, EXTRACTION_PROMPT, DELIMITER

TEST_CASES = [
    ("how much is a latte?", "Latte"),
    ("what teas do you have?", "category Tea"),
    ("tell me about the cappuccino and the croissant", "Cappuccino, Croissant"),
    ("how much is a coffee latte?", "Latte"),
    ("is the FLAT WHITE vegan?", "Flat White"),
    ("what do you have in cold drinks?", "category Cold Drinks"),
    ("I want a latte and some pastries", "Latte + category Pastry"),
    ("write me a poem", "nothing ([])"),
    ("do you have burgers?", "nothing ([])"),
    ("what's the cheapest drink?", "nothing ([]), known limitation"),
]

for question, expected in TEST_CASES:
    messages = [
        {"role": "system", "content": EXTRACTION_PROMPT},
        {"role": "user", "content": f"{DELIMITER}{question}{DELIMITER}"},
    ]
    result = parse_extraction(get_response(messages))
    print(f"Q:        {question}")
    print(f"expected: {expected}")
    print(f"got:      {result}")
    print()