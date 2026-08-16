from core.contracts.module import I34Module


class ContextModule(I34Module):
    def __init__(self):
        self.context = {}

    def handle(self, request):
        action = request.get("action")

        if action == "set":
            key = request.get("key")
            value = request.get("value")

            if not key:
                return {
                    "success": False,
                    "error": "Context key is required"
                }

            self.context[key] = value

            return {
                "success": True,
                "action": "set",
                "key": key,
                "value": value
            }

        if action == "get":
            key = request.get("key")

            return {
                "success": True,
                "action": "get",
                "key": key,
                "value": self.context.get(key)
            }

        if action == "clear":
            self.context.clear()

            return {
                "success": True,
                "action": "clear"
            }

        return {
            "success": False,
            "error": "Unknown context action"
        }
