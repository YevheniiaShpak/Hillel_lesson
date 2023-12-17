import json

a = {
    232345: ("Fred", 22),
    789787: ("Ron", 17),
    500000: ("Harry", 16),
    987897: ("Djinni", 15),
    777555: ("Men", 27),
    232323: ("Toppi", 25)
}

with open("dz18.json", "w") as f:
    json.dump(a, f)

