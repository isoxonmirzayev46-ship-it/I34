class I34Security:

    def validate_request(self, request):
        if not isinstance(request, dict):
            return {
                "allowed": False,
                "reason": "Request must be a dictionary"
            }

        if not request:
            return {
                "allowed": False,
                "reason": "Request is empty"
            }

        return {
            "allowed": True,
            "reason": "Request accepted"
        }
