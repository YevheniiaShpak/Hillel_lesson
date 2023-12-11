chess_players = {"Carlsen, Magnus": 1865,"Firouzja, Alireza": 2804,"Ding, Liren": 2799,"Caruana, Fabiano": 1792,"Nepomniachtchi, Ian": 2773}
new = {
    value: key
    for key, value
    in chess_players.items()
}
new1 = {i:j for i, j in new.items() if i > 2000}


new2 = {}
for i1, j1 in new1.items():
    words = j1.split(", ")
    new_value = f"{words[0]} {words[1][0]}."
    new2[i1] = new_value


print(new2)
