from abc import ABC, abstractmethod
class indirimstratejisi(ABC):
    @abstractmethod
    def hesapla(self,fiyat):
        pass
class yilbasiindirimi(indirimstratejisi):
    def hesapla(self, fiyat):
        return fiyat*0.8
class ogrenciindirimi(indirimstratejisi):
    def hesapla(self, fiyat):
        return fiyat*0.7
class kuponindirimi(indirimstratejisi):
    def hesapla(self, fiyat):
        return fiyat*0.9
class urun:
    def __init__(self, fiyat,ad):
        self.ad=ad
        self.fiyat=fiyat
    def __str__(self):
        return f"{self.ad}: {self.fiyat} TL"    
class indirimfab:
    @staticmethod
    def indirimolustur(tip):
        if tip=="yilbasi":
            return yilbasiindirimi()
        elif tip=="ogrenci":
            return ogrenciindirimi()
        elif tip=="kupon":
            return kuponindirimi()
        else:
            raise ValueError("Gecersiz indirim tipi")
class urunlab:
    @staticmethod
    def urunolustur(ad,fiyat):
        return urun(fiyat,ad)
class sepet:
    def __init__(self):
        self.liste=[]

    def urunekle(self,urun):
        self.liste.append(urun) 
    def hesapla(self,indirimtipi):
        toplam=sum(urun.fiyat for urun in self.liste)
        strateji= indirimfab.indirimolustur(indirimtipi)
        if strateji:
            return strateji.hesapla(toplam)     
        return toplam
    
if __name__=="__main__":   
    sepetim=sepet()
    sepetim.urunekle(urunlab.urunolustur("Kitap",100))
    sepetim.urunekle(urunlab.urunolustur("Kalem",20))
    sepetim.urunekle(urunlab.urunolustur("Defter",50))
    print("Toplam fiyat:",sepetim.hesapla("yilbasi"))
    print("Toplam fiyat:",sepetim.hesapla("ogrenci"))
    print("Toplam fiyat:",sepetim.hesapla("kupon"))
    
