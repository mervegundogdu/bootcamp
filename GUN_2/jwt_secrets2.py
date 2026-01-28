import jwt
secret = "secret"
admin_token = jwt.encode({"username": "merve", "admin": True}, secret, algorithm="HS256")
print(admin_token)