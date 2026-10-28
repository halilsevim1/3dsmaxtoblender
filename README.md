# 3ds Max → Blender Aktarım Sistemi

**3ds Max + V-Ray** sahnelerini **Blender + Cycles** ortamına, V-Ray materyalleriyle birlikte doğrudan aktaran iki parçalı bir geçiş sistemidir.

> *English summary:* A two-part pipeline that exports a complete 3ds Max (V-Ray) scene with a MAXScript and imports it into Blender (Cycles) through an add-on (**File > Import > Max Scene (JSON)**). See below for installation and usage.

---

## Nasıl Çalışır?

```
┌────────────────────┐     JSON + FBX      ┌──────────────────────┐
│  3ds Max + V-Ray   │ ─────────────────▶  │  Blender + Cycles    │
│  max2b_v1_2.mse    │   (dışa aktarım)    │  Blender eklentisi   │
└────────────────────┘                     └──────────────────────┘
```

1. **3ds Max tarafı:** MAXScript, sahneyi seçtiğiniz klasöre dışa aktarır (JSON + FBX). Hangi öğelerin aktarılacağını ve hedef klasörü siz seçersiniz.
2. **Blender tarafı:** Eklenti, *Import* menüsüne **Max Scene (JSON)** seçeneğini ekler. Bu seçenekle sahne, Cycles ile çalışacak şekilde Blender'a eksiksiz aktarılır.

## Özellikler

- V-Ray materyalleri dahil tüm sahnenin aktarımı
- Aktarılacak öğeleri ve hedef konumu seçebilme
- Blender'da tek adımla (File > Import) içe aktarma
- Cycles ile doğrudan render almaya hazır sonuç
- Blender 3.0 ve üzeri desteği

## Depo İçeriği

| Yol | Açıklama |
|---|---|
| [`3dsmax/max2b_v1_2.mse`](3dsmax/max2b_v1_2.mse) | 3ds Max için şifrelenmiş MAXScript (dışa aktarıcı) |
| [`blender/max2blender_v1_2.zip`](blender/max2blender_v1_2.zip) | Blender eklentisi (paket) – **Blender 4.x / 5.x (Python 3.11 / 3.12) için önerilen** |
| [`blender/max2b_blender_v1_2.py`](blender/max2b_blender_v1_2.py) | Tek dosyalık eklenti – Python 3.10 tabanlı Blender 3.x sürümleri için |

## Kurulum

### 1) 3ds Max

1. [`max2b_v1_2.mse`](3dsmax/max2b_v1_2.mse) dosyasını indirin.
2. 3ds Max'te **Scripting > Run Script...** menüsünden dosyayı seçin (ya da dosyayı görünüm alanına sürükleyip bırakın).
3. Açılan arayüzden aktarılacak öğeleri ve hedef klasörü seçin.

### 2) Blender

1. Sürümünüze uygun dosyayı indirin (yukarıdaki tabloya bakın).
2. **Edit > Preferences > Add-ons > Install...** (Blender 4.2+ için: *Install from Disk...*) ile dosyayı seçin.
3. **Max to Blender Scene Importer** eklentisini işaretleyerek etkinleştirin.

> `.zip` dosyasını **açmadan**, olduğu gibi seçin.

## Kullanım

1. 3ds Max'te sahneyi açın, `.mse` betiğini çalıştırın, ayarları yapıp **dışa aktarın**.
2. Blender'da **File > Import > Max Scene (JSON)** seçeneğini kullanın.
3. Dışa aktarım klasöründeki `.json` dosyasını seçin. FBX dosyaları ve dokular aynı klasörde bulunmalıdır.
4. Render motorunu **Cycles** olarak ayarlayıp render alın.

## Sistem Gereksinimleri

| Bileşen | Gereksinim |
|---|---|
| 3ds Max | MAXScript çalıştırabilen sürüm + V-Ray |
| Blender | 3.0 veya üzeri |
| Python (zip paketi) | 3.11 veya 3.12 (Blender'ın kendi Python'u) |
| Render motoru | Cycles |

## Sorun Giderme

- **Eklenti menüde görünmüyor:** Eklentinin Preferences > Add-ons içinde etkin olduğundan emin olun.
- **Eklenti yüklenmiyor:** Blender'ın Python sürümüne uygun dosyayı kullanın (zip: 3.11/3.12, `.py`: 3.10).
- **Dokular eksik:** Dışa aktarılan klasörün taşınmadan, tüm dosyalarıyla birlikte kullanıldığından emin olun.

## Notlar

Betik ve eklenti kaynak kodları korumalı (şifreli) olarak dağıtılır; dosyaların değiştirilmesi çalışmayı bozar.

## Sürüm

**v1.2** – Halil Sevim

## Lisans / Telif

© Halil Sevim – Tüm hakları saklıdır. İzinsiz yeniden dağıtım ve değiştirme yapılamaz.
