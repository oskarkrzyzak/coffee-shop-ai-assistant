from main import get_response, parse_extraction, EXTRACTION_PROMPT, DELIMITER

TEST_CASES = [
    ("how much is a latte?", [{"items": ["Latte"]}]),
    ("what teas do you have?", [{"category": "Tea"}]),
    ("tell me about the kappuccino and the croissant", [{"items": ["Cappuccino", "Croissant"]}]),
    ("how much is a koffee lattee?", [{"items": ["Latte"]}]),
    ("is the FAT WHITEE vegan?", [{"items": ["Flat White"]}]),
    ("what do you have in cold drinks?", [{"category": "Cold Drinks"}]),
    ("I want a latte and some pastries", [{"items": ["Latte"]}, {"category": "Pastry"}]),
    ("write me a poem", []),
    ("do you have burgers?", []),
    ("what's the cheapest drink?", []),
]

score = 0
for question, expected in TEST_CASES:
    messages = [
        {"role": "system", "content": EXTRACTION_PROMPT},
        {"role": "user", "content": f"{DELIMITER}{question}{DELIMITER}"},
    ]
    result = parse_extraction(get_response(messages))
    ok = result == expected
    print(f"Test {'passed' if ok else 'failed'}")
    print(f"Q:        {question}")
    print(f"expected: {expected}")
    print(f"got:      {result}")
    print()
    if ok:
        score += 1

print(f"Score: {score}/{len(TEST_CASES)}")