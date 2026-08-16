class I34Core:
    def __init__(self):
        self.modules = {}

    def register_module(self, name, module):
        self.modules[name] = module

    def call_module(self, name, request):
        if name not in self.modules:
            raise ValueError(f"Module not found: {name}")

        module = self.modules[name]

        if not hasattr(module, "handle"):
            raise TypeError(f"Invalid I34 module: {name}")

        return module.handle(request)
