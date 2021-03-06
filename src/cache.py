import os

import redis


class UserCacheFactory:

    __instance = None

    @staticmethod
    def getCache():
        if UserCacheFactory.__instance is not None:
            return UserCacheFactory.__instance

        if "HEROKU" in list(os.environ.keys()):
            UserCacheFactory.__instance = RedisCache()
        else:
            UserCacheFactory.__instance = DictCache()

        return UserCacheFactory.__instance


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
        self.user_cache.hmset(key, value)

    def get(self, key):
        return self.user_cache.hgetall(key)

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
