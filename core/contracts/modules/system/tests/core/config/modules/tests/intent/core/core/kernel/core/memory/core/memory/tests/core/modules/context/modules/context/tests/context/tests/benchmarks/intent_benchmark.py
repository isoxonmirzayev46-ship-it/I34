from modules.intent.intent_module import IntentModule


CASES = [
    {
        "text": "Salom",
        "expected": "greeting"
    },
    {
        "text": "Salom I34",
        "expected": "greeting"
    },
    {
        "text": "Menga yordam kerak",
        "expected": "help"
    },
    {
        "text": "Yordam ber",
        "expected": "help"
    },
    {
        "text": "Bugun ob-havo qanday?",
        "expected": "unknown"
    }
]


def run_benchmark():
    module = IntentModule()

    total = len(CASES)
    correct = 0

    for case in CASES:
        result = module.handle({
            "text": case["text"]
        })

        if result["intent"] == case["expected"]:
            correct += 1

    accuracy = correct / total

    return {
        "total": total,
        "correct": correct,
        "accuracy": accuracy
    }


if __name__ == "__main__":
    result = run_benchmark()
    print(result)
