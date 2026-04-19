# 📖 Kuantum-Geçidi Kullanım Rehberi

Bu rehber, projenin kurulumu, yapısı ve kullanımı hakkında detaylı bilgi sağlamaktadır.

## 🚀 Hızlı Başlangıç

### 1. Gereksinimler
Proje Python 3.9+ ve Qiskit 1.0+ ekosistemini kullanmaktadır. Gerekli kütüphaneleri şu komutla kurabilirsiniz:

```bash
pip install -r requirements.txt
```

### 2. İlk Testin Çalıştırılması
Terminal üzerinden kuantum ışınlanma protokolünün doğruluğunu test etmek için:

```bash
python kaynak/isinlanma_test.py
```

Bu komut şunları yapar:
*   Rastgele veya belirlenmiş bir kuantum durumu hazırlar.
*   Işınlanma devresini kurar ve simüle eder.
*   **Fidelity (Sadakat)** hesaplayarak veri iletim başarısını raporlar.
*   Görsel çıktıları `gorseller/` klasörüne kaydeder.

---

## 🏗 Proje Yapısı

### `kaynak/` (Kaynak Kod)
*   **`devre_tasarimci.py`**: Kuantum devrelerinin atomik parçalarını (dolanıklık, hazırlık, düzeltme) oluşturur.
*   **`analiz_araclari.py`**: Bloch küresi karşılaştırması ve sadakat hesaplama gibi analiz araçlarını içerir.
*   **`isinlanma_test.py`**: Tüm süreci başlatan ve doğrulayan ana script.

### `dersler/` (Eğitim Materyalleri)
01'den 03'e kadar olan Jupyter Notebook dosyaları, kuantum mekaniği bilmeyen birinin temelden başlayarak ışınlanma protokolünü anlamasını sağlamak için tasarlanmıştır.

---

## 📊 Sonuçları Anlamak

Çalıştırma sonrası `gorseller/` klasöründe şu dosyaları göreceksiniz:
1.  **`isinlanma_devresi.png`**: Protokolün Qiskit üzerindeki devre şeması.
2.  **`bloch_karsilastirma.png`**: Alice'in gönderdiği durum ile Bob'un aldığı durumun Bloch küresi üzerindeki yan yana görseli.

---

## 🛠 Sorun Giderme

*   **Çizim Hatası:** Eğer `matplotlib` veya `pylatexenc` yüklü değilse devre şemaları görsel yerine metin (ASCII) olarak kaydedilir.
*   **Sürüm Uyumluluğu:** `qiskit>=1.0.0` kullandığınızdan emin olun.

---

### 👨‍💻 Geliştirici Hakkında

Bu proje **Bahattin Yunus Çetin** (IT Architect) tarafından kuantum hesaplama pratiklerini akademik ve endüstriyel standartlarda sunmak amacıyla geliştirilmiştir.

*   **GitHub:** [github.com/arch-yunus](https://github.com/arch-yunus)
*   **LinkedIn:** [linkedin.com/in/bahattinyunus](https://www.linkedin.com/in/bahattinyunus/)
