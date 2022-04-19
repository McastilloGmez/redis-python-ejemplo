import redis

redis_cli = redis.Redis(host="192.168.1.234", port=6379, decode_responses=True, encoding="utf-8")

def setToRedis(key, value):
    response = redis_cli.set(key, value)
    return response

def getToRedis(key):
    response = redis_cli.get(key)
    return response

def deleteRedisKey(key):
    response = redis_cli.delete(key)
    return response



