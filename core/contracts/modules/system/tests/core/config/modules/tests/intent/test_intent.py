from modules.intent.intent_module import IntentModule


def test_greeting_intent():
    module = IntentModule()

    result = module.handle({
        "text": "Salom I34"
    })

    assert result["success"] is True
    assert result["intent"] == "greeting"


def test_help_intent():
    module = IntentModule()

    result = module.handle({
        "text": "Menga yordam kerak"
    })

    assert result["success"] is True
    assert result["intent"] == "help"
