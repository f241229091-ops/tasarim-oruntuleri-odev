# Uygulanan Tasarım Örüntüleri

## Faz 1: Creational Patterns
- **Factory Method:** Ürün ve indirim nesnelerini oluşturmak için `urunlab` ve `indirimfab` sınıfları kullanıldı. Nesne yaratma mantığı istemci koddan ayrıldı.

## Faz 2: Structural Patterns
- **Decorator Pattern:** Mevcut indirim stratejilerini sarmalayarak (wrap) birden fazla indirimin aynı anda uygulanabilmesini sağlayan `EkIndirimDecorator` sınıfı eklendi.

## Faz 3: Behavioral Patterns
- **Observer Pattern:** Sepete bir ürün eklendiğinde `BildirimSistemi` sınıfına otomatik haber verilmesini sağlamak için kullanıldı. Bu sayede sepet ve bildirim mantığı birbirinden ayrıştırıldı.