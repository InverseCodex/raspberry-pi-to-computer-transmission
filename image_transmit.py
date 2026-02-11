import requests

BASE = "https://agrivision-website-v2.onrender.com"
USER_ID = "eb4f9e26-572c-433b-b32d-fc24e642e3ea"

# 1) Connect
r = requests.post(f"{BASE}/device/connect_user", json={"user_id": USER_ID}) #Flask route change later if final na
print("CONNECT:", r.status_code, r.text)

if r.status_code != 200:
    raise SystemExit("Connect failed; not uploading.") #Error Catching

data = r.json()
request_id = data["request_id"]
device_id = data["device_id"]

# 2) Upload
with open("photo.png", "rb") as f:
    files = {"image": ("photo.png", f, "image/png")}
    form = {"request_id": request_id, "device_id": device_id}
    r2 = requests.post(f"{BASE}/device/upload", data=form, files=files)

print("UPLOAD:", r2.status_code, r2.text)
