# Funny Wars

Bu projede, Python ile geliştirilmiş bir oyun bulunmaktadır. FunnyWars bir 2D top-down multiplayer strateji oyunudur. Çıplak olan ana karakterimizle haritada reastgele çıkan meyveleri yiyip belli bir miktar koşarak bizim için savaşan boktan askerleri yönetip diğerleri ile savaştığımız, klozete gidenin kazandığı FunnyWars adından da anlaşılabileceği üzere eğlencesine yapılmış bir oyundur.

FunnyWars yakın arkadaşım olan Arda Akdoğan ile lise yıllarımızda birlikte komik bir strateji oyunu yapmak istememizle doğmuş bir oyundur.
Oyun maalesef akademik nedenlerden dolayı bir prototip olmaktan ileri gidemedi ve oyunu bitiremedik ancak planlama ve birlikte çalışma yeteneklerimiz geliştirdiğimiz eğlenceli bir proje oldu.

## Takım

Developer -> Umutcan Ekinci
2D Designer -> Arda Akdoğran

## Oyundan Görseller

![alt text](https://github.com/umutcanekinci/funny-wars/blob/main/images/sample.png?raw=true)

## Başlangıç

### Gereksinimler

Projeyi çalıştırmak için aşağıdaki yazılımlara ihtiyacınız olacaktır:

- Python 3.x
- Gerekli kütüphaneler (aşağıda listelenmiştir)
    - pygame=2.5.2

### Kurulum

*Kurulum yapmadan derlenmiş edilmiş çalıştırılabilir uygulama ile devam etmek istiyorsanız kurulum aşaması atlayıp __main__.exe dosyasını çalıştırabilirsiniz.


Gerekli kütüphaneleri yüklemek için aşağıdaki adımları izleyin:

1. Bu projeyi klonlayın:
    ```sh
    git clone https://github.com/umutcanekinci/funny-wars.git
    cd funny-wars
    ```

2. Sanal ortam oluşturun:
    ```sh
    python -m venv venv
    source venv/bin/activate # Windows kullanıyorsanız: venv\Scripts\activate
    ```

3. Gerekli paketleri yükleyin:
    ```sh
    pip install -r requirements.txt
    ```

### Çalıştırma

Oyunu çalıştırmak için şu komutu kullanın:
```sh
python __main__.py
```

### Kullanım

Oyunun amacı: Şehrini kur ve yönet, şehrin geliri ile daha fazla bina inşa et ve onları birleştirerek şehrini geliştir geliştir ve bu sayede daha fazla kazan.

#### Kontroller: 

##### Hareket etme tuşları:

W / Yukarı ok tuşu

A / Sol ok tuşu

S / Aşağı ok tuşu

D / Sağ ok tuşu

ESC Tuşu ile oyundan çıkabilirsiniz.

### Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen şu adımları izleyin:

1. Bu depoyu fork'layın (sağ üstteki Fork butonuna tıklayın).

2. Fork'ladığınız depoyu yerel makinenize klonlayın:
```sh
git clone https://github.com/umutcanekinci/funny-wars.git
cd funny-wars
```

3. Yeni bir dal oluşturun (örn: feature/yenilik):
```sh
git checkout -b feature/yenilik
```

4. Değişikliklerinizi yapın ve commit edin:
```sh
git commit -am 'Yeni özellik ekledim'
```

5. Değişikliklerinizi dalınıza iterek GitHub'a gönderin:
```sh
git push origin feature/yenilik
```

6. Pull request oluşturun.

### Lisans

Bu proje MIT Lisansı ile lisanslanmıştır - detaylar için LICENSE dosyasına bakabilirsiniz.

### İletişim

Sorularınız veya önerileriniz için umutcannekinci@gmail.com üzerinden iletişime geçebilirsiniz.
