# 📖 Kuantum-Geçidi: Kullanım Rehberi

Bu rehber, projenin yerel makinenizde nasıl kurulacağını ve çalıştırılacağını adım adım açıklar.

## 🛠 1. Kurulum

Sisteminizde Python 3.8+ yüklü olduğundan emin olun. Bağımlılıkları kurmak için:

```bash
pip install -r requirements.txt
```

### ❗ Troubleshooting (Olası Sorunlar)
*   **Grafik Hatası:** Eğer devre çizimleri (`mpl` output) hata veriyorsa, `pylatexenc` kütüphanesinin yüklü olduğundan emin olun.
*   **Aero Simulator:** Qiskit Aer bazen C++ derleyicisi gerektirebilir. Hata alırsanız `qiskit-aer` yerine `qiskit-aer-gpu` (uygun donanım varsa) deneyebilir veya sanal ortamınızı (venv) kontrol edebilirsiniz.

## 📚 2. Eğitim İçerikleri

Dersler Jupyter Notebook formatındadır:
1.  **[01_Qubit_Nedir.ipynb](dersler/01_Qubit_Nedir.ipynb):** Temeller.
2.  **[02_Dolaniklik_Olusturma.ipynb](dersler/02_Dolaniklik_Olusturma.ipynb):** Bell durumları.
3.  **[03_Isinlanma_Protokolu.ipynb](dersler/03_Isinlanma_Protokolu.ipynb):** Tam simülasyon.

## 🚀 3. Test Simülasyonu

Terminal üzerinden hızlı bir test için:
```bash
python kaynak/isinlanma_test.py
```

Bu işlem `gorseller/isinlanma_tam_devre.png` dosyasını oluşturacak ve Alice ile Bob arasındaki kuantum sadakat (fidelity) oranını terminale yazdıracaktır.

## 🔍 4. Mimari
*   `kaynak/devre_tasarimci.py`: Protokol mantığı.
*   `kaynak/analiz_araclari.py`: Görselleştirme katmanı.
