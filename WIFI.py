import subprocess

profiles = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"],
    shell=True
).decode("utf-8", errors="ignore")

names = []

for line in profiles.splitlines():
    if "All User Profile" in line:
        name = line.split(":", 1)[1].strip()
        names.append(name)

print("Saved Wi-Fi Profiles:\n")

for i, name in enumerate(names, 1):
    print(f"[{i}] {name}")