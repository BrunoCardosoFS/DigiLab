class TempSettings:
    _temp_settings = {}

    @classmethod
    def set(self, key: str, value):
        self._temp_settings[key] = value

    @classmethod
    def get(self, key: str, default=False):
        return self._temp_settings.get(key, default)
