# Proje Tasarım Sorunları Analizi

## 1. Kendi Tespit Ettiğim Sorunlar (Manuel Analiz)
Aşağıdaki sorunlar kodu ilk incelediğimde gözüme çarpan temel tasarım eksiklikleridir:

* **Esneklik Eksikliği:** İndirim eklemek için sürekli `if-else` bloklarını değiştirmek gerekiyordu, bu da kodun bakımını zorlaştırıyordu.
* **Karmaşık Mantık Yapısı:** Hesaplama mantığı ile ürün yönetimi aynı sınıfın içindeydi, bu durum kodun okunabilirliğini düşürüyordu.
* **Kod Tekrarı:** Farklı indirim türleri için benzer hesaplama yapıları tekrar ediliyordu.
* **Genişletilebilirlik Sorunu:** Yeni bir özellik (örneğin bildirim sistemi) eklemek istediğimde ana sınıfın yapısını bozmam gerekiyordu.
* **Sıkı Bağlılık (Tight Coupling):** Ürünlerin indirim türlerine göbekten bağlı olması, sistemin modüler yapısını bozuyordu.

## 2. Yapay Zeka (AI) Tarafından Tespit Edilen Sorunlar
AI aracı (Gemini/ChatGPT) kodu analiz ettiğinde şu teknik eksiklikleri raporlamıştır:

* **Single Responsibility Principle (SRP) İhlali:** `sepet` sınıfının hem ürün listesini tutması hem de indirim hesaplaması yapmasının "Tek Sorumluluk İlkesine" aykırı olduğu belirtildi.
* **Open/Closed Principle İhlali:** Mevcut kodun yeni özelliklere kapalı, değişikliğe ise açık olduğu (yani her yeni özellikte eski kodun değiştirilmesi gerektiği) vurgulandı.
* **Strateji Eksikliği:** Algoritmaların (indirim türlerinin) nesneleşmediği, fonksiyon içine gömülü kaldığı tespiti yapıldı.
* **Bildirim Mekanizması Yoksunluğu:** Sepetteki değişikliklerin dış sistemlere (kullanıcıya/stok sistemine) haber verilmesi için bir arayüz eksikliği bildirildi.
* **Dinamik Yapılandırma Hatası:** Birden fazla indirimin (Örn: Öğrenci indirimi + Kupon) aynı anda uygulanamaması bir yapısal sorun olarak tanımlandı.

## 3. Karşılaştırma ve Analiz
Kendi gözlemlerim ile AI analizini kıyasladığımda şu sonuçlara ulaştım:

* **Benzerlikler:** Her iki analiz de kodun esnek olmadığını ve yeni özellik eklemenin zor olduğunu (if-else yapısı) ortak bir sorun olarak gördü.
* **Farklılıklar:** Ben daha çok "okunabilirlik" ve "zorluk" gibi pratik sonuçlara odaklanırken, AI analizi "SRP" ve "Open/Closed" gibi akademik prensipler üzerinden teknik bir yaklaşım sundu.
* **Kazanım:** AI analizi sayesinde, sorunun sadece "if-else kalabalığı" olmadığını, aslında temel SOLID prensiplerinin ihlal edildiğini fark ettim. Bu durum, çözüm için hangi tasarım örüntülerini (Strategy, Decorator, Observer) kullanmam gerektiğini netleştirdi.