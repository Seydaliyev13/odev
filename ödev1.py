def ciroHesapla(satisMiktar,birimSatisf):
    global inttoplamCiro
    toplamCiro=satisMiktar*birimSatisf
    return toplamCiro
def adamBasic(toplamCiro,adamSayisi):
    adamBasiCiro=toplamCiro/adamSayisi
    return adamBasiCiro
satisMiktar=int(input("Satış Miktarını giriniz:"))
birimSatisf=int(input("Birim Satış Fiyatını giriniz:"))
adamSayisi=int(input("Çalışan Sayısını giriniz:"))
ciro=ciroHesapla(satisMiktar,birimSatisf)
adamBasiCiro=adamBasic(ciro,adamSayisi)
print("ToplamCiro:",ciro)
print("Adam başına düşen Ciro:",adamBasiCiro)

