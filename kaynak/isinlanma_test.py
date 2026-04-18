import os
import sys

# Proje kök dizinini ekle (kaynak klasörüne erişim için)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qiskit import transpile
from qiskit_aer import Aer
from kaynak.devre_tasarimci import DevreTasarimci
from kaynak.analiz_araclari import AnalizAraclari

def main():
    print("Kuantum-Gecidi: Isinlanma Testi Baslatiliyor...")
    
    # 1. Devre Kurulumu
    tasarimci = DevreTasarimci()
    qc, qr, crz, crx = tasarimci.isinlanma_devresi_hazirla()
    
    # 2. Işınlanacak Durumu Hazırla (q0)
    # Rastgele bir durum seçelim
    theta, phi = tasarimci.durum_hazirla(qc, qr[0])
    
    # 3. Dolanıklık Oluştur (q1 ve q2 arasında)
    tasarimci.dolaniklik_olustur(qc, qr[1], qr[2])
    
    # 4. Alice'in İşlemleri
    tasarimci.alice_islemleri(qc, qr[0], qr[1])
    
    # 5. Ölçümler
    qc.measure(qr[0], crz)
    qc.measure(qr[1], crx)
    
    # 6. Bob'un Düzeltmeleri
    tasarimci.bob_duzeltmeleri(qc, qr[2], crz, crx)
    
    # 7. Simülasyon
    print("Basari: Protokol kuruldu.")
    
    # Devreyi kaydet
    gorsel_klasor = "gorseller"
    if not os.path.exists(gorsel_klasor):
        os.makedirs(gorsel_klasor)
    
    AnalizAraclari.devre_kaydet(qc, os.path.join(gorsel_klasor, "isinlanma_devresi.png"))
    
    tasarimci_info = f"Hazirlanan Durum: Theta={theta:.2f}, Phi={phi:.2f}"
    print(tasarimci_info)
    
    print("\nDevre Ozeti: Devre semasi gorseller/ klasörüne kaydedildi.")
    # print(qc.draw(output='text')) # Windows encoding sorunu nedeniyle devre dışı

if __name__ == "__main__":
    main()
