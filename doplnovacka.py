"""doplnovacka.py
Moje kamarádka učí soukromě němčinu. 
Potřebuje pro klienty připravit texty, které se časem naučí nazpaměň
(jedná se o právní předpisy).
Proto jim připravuje stále stejný text, ve kterém vynechá nejprve každé 5. slovo,
později každé 4. slovo atd., až se text naučí zpaměti.
Výstupem bude nový soubor. Pracujte se souborem lorem.py.
Vytvořte pro ni program, jehož vstupem bude textový soubor a informace,
kolikátý znak se má zaměnit.

Rozbor:
1)načíst soubor(open)
2)splitnout slova podle mezery do seznamu
3)procházet jednotlivá slova seznamu
4)když se jedná o x-té slovo:
5)procházet písmenka a:
6)písmenko nahradit pomlčkou
7)vynechat interpunkci
8)upravené slovo přidat do seznamu
jinak:
9)původní slovo přidat do seznamu
10)seznam spojit pomocí mezery do řetězce, řetězec uložit do nového souboru

"""

with open("song.txt") as f:
	text = f.read()
f.closed

#print(text)
text = text.replace("  ", " ")
text = text.replace("\n", "# ")

seznam = []
seznam = text.split(" ")

vysledek = []
interpunkce = ",.?!-;\""

for i in range(0, len(seznam)):
	slovo = seznam[i]
	slovoUpraveno = ""
	if ((i + 1) % 5 == 0): #vyberame kazde piate slovo, pricom index zacina na 0. indexe, preto navyšime i o +1
		for pismeno in slovo:
			if pismeno not in interpunkce:
				slovoUpraveno += "*"
			else:
				slovoUpraveno += pismeno
		vysledek.append(slovoUpraveno)
	else:
		vysledek.append(slovo)

s = " ".join(vysledek)
s = s.replace("#", "\n")
print(s)


