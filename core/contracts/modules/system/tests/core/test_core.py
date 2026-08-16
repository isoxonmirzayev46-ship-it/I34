from core.kernel.i34_core import I34Core
from modules.system.system_module import SystemModule


def test_system_module():
    core = I34Core()
    core.register_module("system", SystemModule())

    result = core.call_module(
        "system",
        {"action": "status"}
    )

    assert result["success"] is True
    assert result["module"] == "system"
