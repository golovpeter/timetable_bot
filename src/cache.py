import os

import redis


class UserCacheFactory:

    @staticmethod
    def getCache():
        if "HEROKU" in list(os.environ.keys()):
            return RedisCache()
        else:
            return DictCache()


class UserCache:

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def delete(self, key):
        pass

    def containsKey(self, key):
        pass


class RedisCache(UserCache):

    def __init__(self) -> None:
        self.user_cache = redis.from_url(os.environ.get("REDIS_URL"), decode_responses=True)

    def put(self, key, value):
        self.user_cache.set(key, value)

    def get(self, key):
        return self.user_cache.get(key)

    def delete(self, key):
        self.user_cache.delete(key)

    def containsKey(self, key):
        return self.user_cache.exists(key)


class DictCache(UserCache):

    def __init__(self) -> None:
        self.user_cache = {}

    def put(self, key, value):
        self.user_cache[key] = value

    def get(self, key):
        return self.user_cache[key]

    def delete(self, key):
        del self.user_cache[key]

    def containsKey(self, key):
        return key in self.user_cache
