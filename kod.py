meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap/ Aymnızamada league of legends adlı oyun :)",
            "ROFL":"bir şakaya karşılık cevap",
            "SHEESH":"onaylamamak",
            "CREEPY":"korkunç",
            "AGGRO": "agresifleşmek/sinielnmek"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
        print(meme_dict[word])
else:
        print ("böyle bir kelime yok yer yarıldı içine girdi sanki")
