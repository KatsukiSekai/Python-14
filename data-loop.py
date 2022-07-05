student=[
{"name": "Joseph","score":85},
{"name": "James","score":70},
{"name": "Mary","score":90},
{"name": "Tony","score":65},
{"name": "Tuu","score":49},
{"name": "Pom","score":51},
]
for s in student:
    if s["score"] >= 80:
        print(s["name"],s["score"],"Grade 4")
    elif s["score"] >= 70:
        print(s["name"],s["score"],"Grade 3")
    elif s["score"] >= 60:
        print(s["name"],s["score"],"Grade 2")
    elif s["score"] >= 50:
        print(s["name"],s["score"],"Grade 1")
    else :
        print(s["name"],s["score"],"Grade 0")
#นายชนะชัย สังข์ศิริ 6/14 8