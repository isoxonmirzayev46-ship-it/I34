from modules.tools.tools_module import ToolsModule


def test_list_tools():
    tools = ToolsModule()

    result = tools.handle({
        "action": "list"
    })

    assert result["success"] is True
    assert result["tools"] == []


def test_unknown_tool_action():
    tools = ToolsModule()

    result = tools.handle({
        "action": "unknown"
    })

    assert result["success"] is False
