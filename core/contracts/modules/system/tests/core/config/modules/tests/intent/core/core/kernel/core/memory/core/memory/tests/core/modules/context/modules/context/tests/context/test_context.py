from modules.context.context_module import ContextModule


def test_context_set_and_get():
    context = ContextModule()

    context.handle({
        "action": "set",
        "key": "user_name",
        "value": "I34"
    })

    result = context.handle({
        "action": "get",
        "key": "user_name"
    })

    assert result["success"] is True
    assert result["value"] == "I34"


def test_context_clear():
    context = ContextModule()

    context.handle({
        "action": "set",
        "key": "test",
        "value": "123"
    })

    result = context.handle({
        "action": "clear"
    })

    assert result["success"] is True
    assert context.context == {}
