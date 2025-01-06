class TempSettings:
    temp_settings = {}

    @classmethod
    def set(self, key: str, value):
        self.temp_settings[key] = value

    @classmethod
    def get(self, key: str, default=False):
        return self.temp_settings.get(key, default)
