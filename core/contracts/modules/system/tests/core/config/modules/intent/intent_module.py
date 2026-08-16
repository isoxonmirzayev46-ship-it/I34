from core.contracts.module import I34Module


class IntentModule(I34Module):

    def handle(self, request):
        text = request.get("text", "").strip().lower()

        if not text:
            return {
                "success": False,
                "intent": "unknown",
                "confidence": 0.0
            }

        if "salom" in text:
            return {
                "success": True,
                "intent": "greeting",
                "confidence": 1.0
            }

        if "yordam" in text:
            return {
                "success": True,
                "intent": "help",
                "confidence": 1.0
            }

        return {
            "success": True,
            "intent": "unknown",
            "confidence": 0.0
        }
