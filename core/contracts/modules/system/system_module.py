from core.contracts.module import I34Module


class SystemModule(I34Module):

    def handle(self, request):
        return {
            "success": True,
            "module": "system",
            "request": request
        }
