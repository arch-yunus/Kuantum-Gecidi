# 🌌 Kuantum-Geçidi: Kuantum Işınlanma Rehberi

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Qiskit: 1.0+](https://img.shields.io/badge/Qiskit-1.0+-orange.svg)](https://qiskit.org/)
[![Build: Success](https://img.shields.io/badge/Build-Success-brightgreen.svg)]()

**Kuantum-Geçidi**, kuantum mekaniğinin en büyüleyici fenomenlerinden biri olan **Kuantum Işınlanma** (Quantum Teleportation) protokolünü modern yazılım perspektifiyle modelleyen, simüle eden ve öğreten kapsamlı bir eğitim platformudur.

> [!NOTE]
> Bu depo, "ışınlanma" kavramını bilim kurgudan çıkarıp, kuantum bilgi kuramı çerçevesinde somut bir algoritma olarak ele alır.

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

Kuantum ışınlanma, bir parçacığın üzerindeki kuantum bilgisinin (durumunun), parçacığın kendisi hareket etmeden, dolanıklık ve klasik iletişim kullanılarak başka bir parçacığa aktarılmasıdır.

### Temel Sütunlar
1.  **No-Cloning (Kopyalanamazlık):** Bir kuantum durumu kopyalanamaz; veri aktarıldığında orijinal kaynaktaki bilgi yok olur.
2.  **Süperpozisyon:** Verinin aynı anda hem 0 hem 1 olasılığını taşıma yeteneği.
3.  **Dolanıklık (Entanglement):** Einstein'ın "uzaktan ürkütücü etkileşim" dediği, parçacıkların kader birliği.

---

## 🧪 Teknik Derin Bakış

### Protokolün Matematiği

Alice, elindeki bilinmeyen $| \psi \rangle$ durumunu Bob'a göndermek ister:

$$| \psi \rangle = \alpha | 0 \rangle + \beta | 1 \rangle$$

Süreç şu adımları izler:

1.  **Dolanıklık Hazırlığı:** Alice ve Bob bir Bell çifti paylaşır: $| \Phi^+ \rangle = \frac{1}{\sqrt{2}} (| 00 \rangle + | 11 \rangle)$.
2.  **Alice'in Etkileşimi:** Alice kendi qubitlerini birbirine bağlar ve Bell ölçümüne hazırlar.
3.  **Ölçüm Çöküşü:** Alice ölçüm yaptığında, Bob'un elindeki qubit Alice'in sonucuna göre 4 olası durumdan birine girer.
4.  **Klasik Düzeltme:** Bob, Alice'den gelen 2 klasik biti kullanarak kendi qubitine $X$ ve/veya $Z$ kapıları uygular ve orijinal $| \psi \rangle$ durumunu %100 sadakatle (fidelity) elde eder.

---

## 🖼 Görsel Galeri (Showcase)

Bu proje, karmaşık kuantum süreçlerini anlamayı kolaylaştırmak için otomatik görselleştirmeler üretir:

| Devre Şeması | Girdi Durumu (Alice) | Çıktı Durumu (Bob) |
| :---: | :---: | :---: |
| ![Circuit](gorseller/isinlanma_devresi.png) | ![Girdi](gorseller/bloch_girdi.png) | ![Çıktı](gorseller/bloch_cikti.png) |

> [!TIP]
> `kaynak/isinlanma_test.py` dosyasını çalıştırarak kendi görsel çıktılarınızı anında üretebilirsiniz.

---

## 🚀 Başlangıç

### 1. Kütüphaneleri Kurun
```bash
pip install -r requirements.txt
```

### 2. İlk Işınlanma Devresini Çalıştırın
```bash
python kaynak/isinlanma_test.py
```

---

## 🗺 Yol Haritası (Roadmap)

- [x] Temel Işınlanma Protokolü (Qiskit 1.0+)
- [x] Fidelity (Sadakat) Analiz Aracı
- [ ] **Gürültü Modelleri:** Gerçek kuantum cihazlarındaki (decoherence) hataların simülasyonu.
- [ ] **Kuantum Tekrarlayıcılar:** Uzun mesafe kuantum ağları için modelleme.
- [ ] **Multi-Qubit Teleportasyon:** Birden fazla qubitin aynı anda aktarımı.

---

## 📜 Tarihçe ve Kilometre Taşları

Kuantum ışınlanma, teorik bir öngörüden küresel ölçekte deneylere uzanan büyük bir yolculuktur:

*   **1993 - Teorik Temel:** Charles Bennett ve ekibi, kuantum ışınlanmanın protokolünü ilk kez teorik olarak ortaya koydu.
*   **1997 - İlk Deney:** Anton Zeilinger ve ekibi (Viyana Üniversitesi), fotonların polarizasyon durumunu ilk kez başarıyla ışınladı.
*   **2004 - Atomik Işınlanma:** Innsbruck ve NIST ekipleri, bilgiyi atomdan atoma aktarmayı başardı.
*   **2017 - Micius Uydusu:** Jian-Wei Pan liderliğindeki ekip, Tibet'teki bir istasyondan yörüngedeki **Micius** uydusuna **1,400 km** mesafeden foton ışınlayarak rekor kırdı.
*   **2020+ - Kuantum İnterneti:** Günümüzde teleportasyon, kıtalararası kuantum ağlarının (Quantum Internet) kalbi olarak kabul edilmektedir.

---

## 📜 Kaynakça & Teşekkür

1.  **Bennett, C. H. et al.** (1993). "Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels". [Physical Review Letters].
2.  **Qiskit Documentation** - [docs.quantum.ibm.com](https://docs.quantum.ibm.com/)

---

## 🤝 Katkıda Bulunma

Bu bir eğitim projesidir ve her türlü katkıya açıktır!
1. Depoyu çatallayın (Fork).
2. Yeni bir özellik dalı (Feature Branch) açın.
3. Değişikliklerinizi kaydedin ve bir Pull Request oluşturun.

---

**[Yunus Çetin - 2026]** | [GitHub](https://github.com/arch-yunus)