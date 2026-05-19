#00. パタトクカシーー,2つの文字列「パトカー」と「タクシー」の文字を先頭から交互に連結し、文字列「パタトクカシーー」を得よ。
kotoba1= "パトカー"
kotoba2 = "タクシー"

kekka0 = ""

for i in range(len(kotoba1)):
    kekka0 += kotoba1[i] + kotoba2[i]
print(kekka0)


