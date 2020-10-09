q = str(open("steam_description_data.csv"))
w = len(q)
print("символов : " + str(w))
w = len(q) - q.count(" ")
print("символов (без пробелов): " + str(w))
w = len(q) - q.count(".") - q.count("!") - q.count("?") - q.count(",") - q.count(";") - q.count("-") - q.count(":") - q.count("\"") - q.count("(") - q.count(")") - q.count("/")
print("символов (без знаков препинания): " + str(w))
w = q.count(" ") + 1
print("слов: " + str(w))
w = q.count(".") - q.count("...")*2 + q.count("!") + q.count("?") - q.count("?!") - q.count("!!!")*2
print("предложений: " + str(w))