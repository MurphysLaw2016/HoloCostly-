import lists as l
import os

camp_dict = {
    0: l.Lager,
    1: l.Tod,
    2: l.Land,
    3: l.Betriebszeit,
    4: l.Gaskammer,
    5: l.Das_verstecken_Juden
}

camp_names = {
    0: "Lager",
    1: "Tod",
    2: "Land",
    3: "Betriebszeit",
    4: "Gaskammer",
    5: "Das_verstecken_Juden"
}

file_list = []
for i in range(len(camp_dict)):
    try:
        with open(f"{camp_names[i]}.txt", "x") as f:
            title = camp_names[i]
            title.encode("UTF-8")
            f.write(f"{title}\n\n")
            file_list.append(camp_names[i])
            for index, item in enumerate(camp_dict[i]):
                item = item.encode("UTF-8")
                f.write(f"{index}: {item}\n")
    except FileExistsError:
        pass

name = input("what file are you looking for? There is Lager, Tod, Land, Betriebszeit, Gaskammer, "
             "and Das_verstecken_Juden. ")
with open(f"{name}.txt") as n:
    to_print = n.read()
    to_plaintext = to_print.encode('latin1').decode('unicode_escape').encode('latin1').decode('utf8')
    to_plaintext = to_plaintext.replace("b", "")
    to_plaintext = to_plaintext.replace("'", "")
    print(to_plaintext)

for i in range(len(camp_dict)):
    os.remove(f"{camp_names[i]}.txt")
