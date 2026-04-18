# 🌌 Kuantum-Geçidi: Kuantum Işınlanma Rehberi

![Kuantum Geçidi Banner](assets/banner.png)

**Kuantum-Geçidi**, kuantum mekaniğinin en büyüleyici fenomenlerinden biri olan "Kuantum Işınlanma" (Quantum Teleportation) protokolünü, yazılım dünyasından gelenlerin anlayabileceği bir dille modellemek, simüle etmek ve öğretmek için tasarlanmış bir eğitim deposudur.

---

## 🏗 Repository Structure

| Module | Description | Location |
| :--- | :--- | :--- |
| 📚 **Lessons** | Interactive Jupyter Notebooks for learning. | `dersler/` |
| 🛠 **Source** | Core Qiskit implementation and helpers. | `kaynak/` |
| 🖼 **Gallery** | Circuit diagrams and visualization results. | `gorseller/` |
| 📖 **Guide** | Detailed setup and usage instructions. | [KULLANIM_REHBERI.md](KULLANIM_REHBERI.md) |

---

## 🧐 Nedir Bu Kuantum Işınlanma?

Popüler kültürdeki "ışınlanma" sahnelerinin aksine, kuantum ışınlanma verinin (qubit durumunun) transferidir. **No-Cloning (Kopyalanamazlık) Teoremi** gereği, bir kuantum durumu kopyalanamaz; ancak "aktarılabilir". Bu aktarım gerçekleştiğinde, orijinal kaynaktaki bilgi yok olur ve hedef noktada yeniden belirir.

### Temel Kavramlar
1.  **Qubit:** Süperpozisyon halindeki veri birimi.
2.  **Süperpozisyon:** Bir qubitin aynı anda hem 0 hem 1 olma durumu.
3.  **Dolanıklık (Entanglement):** Parçacıkların mesafeden bağımsız birbirine bağlanması.
4.  **Bell Ölçümü:** Bilgiyi Alice'den Bob'a aktarmak için kullanılan yöntem.

---

## 🛠 Teknik Mimari

Proje, kuantum devrelerini simüle etmek için Python ve **Qiskit** (IBM Quantum SDK) kullanmaktadır. Protokol 4 ana aşamadan oluşur:

1.  **Hazırlık:** Işınlanacak durumun oluşturulması.
2.  **Dolanıklık Kanalı:** Alice ve Bob arasında EPR çifti kurulması.
3.  **Bell Ölçümü:** Alice'in qubitler üzerinde ölçüm yapması.
4.  **Düzeltme:** Bob'un ölçüm sonuçlarına göre qubitini güncellemesi.

---

## 🚀 Başlangıç

### 1. Kütüphaneleri Kurun
```bash
pip install -r requirements.txt
```

### 2. İlk Işınlanma Devresini Çalıştırın
Terminal üzerinden testi başlatın:
```bash
python kaynak/isinlanma_test.py
```

---

## 🤝 Katkıda Bulunma

Bu bir eğitim projesidir. Pull Request göndererek katkıda bulunabilirsiniz!
1. Depoyu çatallayın.
2. Feature branch açın.
3. Değişikliklerinizi kaydedin ve PR açın.

---

## 📜 Lisans

Bu proje MIT Lisansı ile korunmaktadır.

---

**[Yunus Çetin - 2026]** | [GitHub](https://github.com/arch-yunus)