import os
import sys

# Proje kök dizinini ekle (kaynak klasörüne erişim için)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qiskit import transpile
from qiskit_aer import Aer
from kaynak.devre_tasarimci import DevreTasarimci
from kaynak.analiz_araclari import AnalizAraclari

def main():
    print("🌌 Kuantum-Geçidi: Işınlanma Testi Başlatılıyor...")
    
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
    print("🚀 Devre simüle ediliyor...")
    # Not: Bob'un qubitini ölçmek için sona bir ölçüm ekleyebiliriz 
    # veya durumu doğrudan statevector ile kontrol edebiliriz.
    # Burada sadece devreyi görselleştirelim ve çalıştıralım.
    
    backend = Aer.get_backend('qasm_simulator')
    # Bob'un sonucunu görmek için bir ölçüm daha ekleyelim (opsiyonel)
    # qc.measure_all() # Bu tüm devreyi bozar, son q2'yi ölçmeliyiz
    
    # Devreyi kaydet
    gorsel_klasor = "gorseller"
    if not os.path.exists(gorsel_klasor):
        os.makedirs(gorsel_klasor)
    
    # AnalizAraclari.devre_kaydet(qc, os.path.join(gorsel_klasor, "isinlanma_devresi.png"))
    
    print("\n✅ Protokol başarıyla kuruldu.")
    tasarimci_info = f"Hazırlanan Durum: Theta={theta:.2f}, Phi={phi:.2f}"
    print(tasarimci_info)
    
    print("\nDevre Özeti:")
    print(qc.draw(output='text'))

if __name__ == "__main__":
    main()
