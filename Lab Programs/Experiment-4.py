import re

# List of patterns, descriptions, and test strings
tests = [
    {
        "operator": "? (Zero or one)",
        "pattern": r"^colou?r$",
        "samples": ["color", "colour", "colouur"],
    },
    {
        "operator": "* (Zero or more)",
        "pattern": r"^ab*c$",
        "samples": ["ac", "abc", "abbbc", "adc"],
    },
    {
        "operator": "+ (One or more)",
        "pattern": r"^ab+c$",
        "samples": ["abc", "abbc", "ac"],
    },
    {
        "operator": "[] (Character set)",
        "pattern": r"^[aeiou]$",
        "samples": ["a", "e", "b"],
    },
    {
        "operator": "[^] (Negated character set)",
        "pattern": r"^[^0-9]$",
        "samples": ["a", "Z", "5"],
    },
    {
        "operator": "^ and $ (Start and End Anchors)",
        "pattern": r"^hello$",
        "samples": ["hello", "hello world", "say hello"],
    },
]

# Run tests and print YES or NO
for test in tests:
    print(f"Testing: {test['operator']} | Pattern: {test['pattern']}")
    for s in test["samples"]:
        result = "YES" if re.search(test["pattern"], s) else "NO"
        print(f"  String: '{s}' -> {result}")
    print("-" * 45)