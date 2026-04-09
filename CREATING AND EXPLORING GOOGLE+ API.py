import random, string

files = [
    {
        "name": random.choice(["File", "Doc", "Report", "Data"]) + " " + str(random.randint(1, 100)),
        "id": ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    }
    for _ in range(10)
]

for i, f in enumerate(files, 1):
    print(f"{i}. {f['name']} ({f['id']})")
