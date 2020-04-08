import MeCab
wakati=MeCab.Tagger("-Owakati")
split_res=wakati.parse("トヨタ自動車が中国で 西山 光秋 の完成車工場の操業再開を当初予定の2").split()
print(split_res)
