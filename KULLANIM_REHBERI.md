# 📖 Kuantum-Geçidi: Kullanım Rehberi

Bu rehber, projenin yerel makinenizde nasıl kurulacağını, çalıştırılacağını ve derslerin nasıl takip edileceğini adım adım açıklar.

## 🛠 1. Kurulum

Öncelikle sisteminizde Python 3.8+ yüklü olduğundan emin olun. Ardından gerekli kütüphaneleri kurun:

```bash
pip install qiskit qiskit-aer matplotlib pylatexenc
```

*Not: `pylatexenc`, devrelerin daha şık görünmesi için gereklidir.*

## 📚 2. Dersleri Takip Etme

Dersler Jupyter Notebook (`.ipynb`) formatındadır. Bunları çalıştırmak için VS Code, JupyterLab veya Google Colab kullanabilirsiniz.

1.  **[01_Qubit_Nedir.ipynb](dersler/01_Qubit_Nedir.ipynb):** Kuantum bitlerinin temelleri ve süperpozisyon.
2.  **[02_Dolaniklik_Olusturma.ipynb](dersler/02_Dolaniklik_Olusturma.ipynb):** Bell durumları ve qubitleri birbirine bağlama.
3.  **[03_Isinlanma_Protokolu.ipynb](dersler/03_Isinlanma_Protokolu.ipynb):** Alice'den Bob'a tam bir kuantum ışınlanma simülasyonu.

## 🚀 3. Test Senaryosunu Çalıştırma

Terminal üzerinden doğrudan bir simülasyon başlatmak için:

```bash
python kaynak/isinlanma_test.py
```

Bu komut:
*   Rastgele bir kuantum durumu oluşturur.
*   Işınlanma devresini kurar.
*   Terminal üzerinde devrenin metin tabanlı bir şemasını gösterir.

## 🔍 4. Proje Yapısı

*   `kaynak/`: Projenin ana kod tabanı (Sınıf yapıları ve testler).
*   `dersler/`: Eğitim amaçlı interaktif defterler.
*   `gorseller/`: Devre şemaları ve görsel analizler.

## 🧪 5. Kendi Deneylerinizi Yapın

`kaynak/devre_tasarimci.py` dosyasını inceleyerek kendi kuantum devrelerinizi oluşturabilir, `AnalizAraclari` sınıfı ile bunları görselleştirebilirsiniz.

---
**Kuantum Dünyasına Hoş Geldiniz!** 🌌
