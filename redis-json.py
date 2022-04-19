import json, redis

redis_cli = redis.Redis(host="192.168.1.234", port=6379, decode_responses=True, encoding="utf-8")

product = {"pid": 123, "stock": False}

redis_cli.set("Stock", json.dumps(product))

response = redis_cli.get("Stock")

print(response)