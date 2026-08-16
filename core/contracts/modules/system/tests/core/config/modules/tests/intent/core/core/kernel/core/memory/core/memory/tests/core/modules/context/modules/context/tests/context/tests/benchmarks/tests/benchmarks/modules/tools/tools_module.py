from core.contracts.module import I34Module


class ToolsModule(I34Module):

    def handle(self, request):
        action = request.get("action")

        if action == "list":
            return {
                "success": True,
                "tools": []
            }

        return {
            "success": False,
            "error": "Unknown tool action"
        }
