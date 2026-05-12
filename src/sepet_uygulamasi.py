class Urun:
    def __init__(self,ad,fiyat):
        self.ad=ad
        self.fiyat=fiyat
class sepet:
    def __init__(self,):
        self.liste=[]
    def urun_ekle(self,urun):
        self.liste.append(urun)

    def hesaplama(self,indirim_tipi):
        toplam=sum(u.fiyat for u in self.liste)
        if indirim_tipi=="YILBASI":
            return toplam*0.8
        elif indirim_tipi=="OGRENCI":
            return toplam*0.7
        elif indirim_tipi=="KUPON10":
            return toplam*0.9
        else:
            return toplam   
        
sepet1=sepet()
urun1=Urun("kitap",100)
urun2=Urun("Klavye",250)
sepet1.urun_ekle(urun1)
sepet1.urun_ekle(urun2)
tutar=sepet1.hesaplama("OGRENCI")
print(f"Odenecek toplam tutar: {tutar}")