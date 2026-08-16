from core.memory.memory import I34Memory


def test_memory_set_and_get():
    memory = I34Memory()

    memory.set("name", "I34")

    assert memory.get("name") == "I34"


def test_memory_default():
    memory = I34Memory()

    assert memory.get("unknown") is None


def test_memory_delete():
    memory = I34Memory()

    memory.set("name", "I34")
    memory.delete("name")

    assert memory.get("name") is None


def test_memory_clear():
    memory = I34Memory()

    memory.set("name", "I34")
    memory.set("version", "0.1.0")

    memory.clear()

    assert memory.get("name") is None
    assert memory.get("version") is None
