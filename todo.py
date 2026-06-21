# todo.py

tasks = [
    "Buy milk",
    "Read book"
]


for task in tasks:
    print(task)

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

print()
print(f"Total tasks: {len(tasks)}")

