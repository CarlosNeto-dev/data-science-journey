# Fazer um ranking dos alunos de acordo com a sua idade utilizando as funções "sorted()", "key()" e "lambda()"
students = [
    {"name": "Carlos", "age": 18, "score": 8.25},
    {"name": "Pedro", "age": 25, "score": 9.25},
    {"name": "Matheus", "age": 19, "score": 10}
]

age_organized = sorted(students, key=lambda student: student["age"], reverse=True)

print("+=" * 30)
print("RANKING OF STUDENTS HAVE MORE AGE ".center(60))
print("+=" * 30)
for c, s in enumerate(age_organized, start=1):
    print(f"{c} - {s}")
print("+=" * 30)