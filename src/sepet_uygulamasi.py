from abc import ABC, abstractmethod

class Gozlemci(ABC):
    @abstractmethod
    def guncelle(self, urun_adi):
        pass

class BildirimSistemi(Gozlemci):
    def guncelle(self, urun_adi):
        print(f"BILDIRIM: Sepete yeni urun eklendi -> {urun_adi}")

class indirimstratejisi(ABC):
    @abstractmethod
    def hesapla(self, fiyat):
        pass

class yilbasiindirimi(indirimstratejisi):
    def hesapla(self, fiyat):
        return fiyat * 0.8

class ogrenciindirimi(indirimstratejisi):
    def hesapla(self, fiyat):
        return fiyat * 0.7

class kuponindirimi(indirimstratejisi):
    def hesapla(self, fiyat):
        return fiyat * 0.9

class EkIndirimDecorator(indirimstratejisi):
    def __init__(self, temel_indirim, ek_oran):
        self.temel_indirim = temel_indirim
        self.ek_oran = ek_oran

    def hesapla(self, fiyat):
        ara_sonuc = self.temel_indirim.hesapla(fiyat)
        return ara_sonuc * self.ek_oran

class urun:
    def __init__(self, fiyat, ad):
        self.ad = ad
        self.fiyat = fiyat
    def __repr__(self):
        return f"{self.ad}: {self.fiyat} TL"

class indirimfab:
    @staticmethod
    def indirimolustur(tip):
        if tip == "yilbasi": return yilbasiindirimi()
        elif tip == "ogrenci": return ogrenciindirimi()
        elif tip == "kupon": return kuponindirimi()
        return None

class urunlab:
    @staticmethod
    def urunolustur(ad, fiyat):
        return urun(fiyat, ad)

class sepet:
    def __init__(self):
        self.liste = []
        self._gozlemciler = []

    def gozlemci_ekle(self, gozlemci):
        self._gozlemciler.append(gozlemci)

    def haber_ver(self, urun_adi):
        for gozlemci in self._gozlemciler:
            gozlemci.guncelle(urun_adi)

    def urunekle(self, urun_nesnesi):
        self.liste.append(urun_nesnesi)
        self.haber_ver(urun_nesnesi.ad)

    def hesapla(self, strateji_veya_tip):
        toplam = sum(u.fiyat for u in self.liste)
        if isinstance(strateji_veya_tip, indirimstratejisi):
            return strateji_veya_tip.hesapla(toplam)
        strateji = indirimfab.indirimolustur(strateji_veya_tip)
        if strateji:
            return strateji.hesapla(toplam)
        return toplam

if __name__ == "__main__":
    sepetim = sepet()
    bildirim_merkezi = BildirimSistemi()
    sepetim.gozlemci_ekle(bildirim_merkezi)

    sepetim.urunekle(urunlab.urunolustur("Telefon", 1000))
    sepetim.urunekle(urunlab.urunolustur("Kılıf", 100))

    temel = ogrenciindirimi()
    kombo = EkIndirimDecorator(temel, 0.9)
    
    print(f"Toplam: {sepetim.hesapla(kombo)} TL")