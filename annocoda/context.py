import requests_cache

class Context:
    def __init__(self, logger):
        self.session = requests_cache.CachedSession("image_cache")
        self.logger = logger
