import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

# Proje kök dizinini ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kaynak.devre_tasarimci import DevreTasarimci
from kaynak.analiz_araclari import AnalizAraclari

def run_teleportation_test():
    console_width = 50
    print("=" * console_width)
    print("KUANTUM-GECIDI: ISINLANMA PROTOKOLU TESTI".center(console_width))
    print("=" * console_width)
    
    # 1. Hazırlık
    tasarimci = DevreTasarimci()
    qc, qr, crz, crx = tasarimci.isinlanma_devresi_hazirla()
    
    # Işınlanacak başlangıç durumunu (psi) belirle
    theta = 1.25  # rad
    phi = 0.8     # rad
    tasarimci.durum_hazirla(qc, qr[0], theta, phi)
    
    # Başlangıç durumunu simülasyon öncesi kaydet (Ideal q0 durumu)
    # Sadece ilk qubitin beklenen durumunu oluşturuyoruz
    expected_psi = Statevector.from_label('0').evolve(
        AnalizAraclari.qubit_durumu_cikar(Statevector.from_instruction(qc), 0)
    )
    # Daha basitçe:
    expected_psi = Statevector.from_instruction(qc)
    expected_psi = AnalizAraclari.qubit_durumu_cikar(expected_psi, 0)
    
    # 2. Protokol Adımları
    tasarimci.dolaniklik_olustur(qc, qr[1], qr[2])
    tasarimci.alice_islemleri(qc, qr[0], qr[1])
    
    # Alice'in ölçümleri
    qc.measure(qr[0], crz)
    qc.measure(qr[1], crx)
    
    # Bob'un düzeltmeleri
    tasarimci.bob_duzeltmeleri(qc, qr[2], crz, crx)
    
    print("[+] Protokol devresi başarıyla oluşturuldu.")
    
    # 3. Simülasyon (Statevector bazlı doğrulama için)
    # Not: Dinamik devrelerde statevector takibi için backend ayarları önemlidir
    backend = AerSimulator(method='statevector')
    
    # Devreyi koştur (Ölçümler olsa bile statevector simülatörü son durumu verir)
    # Ancak ölçümler Bob'a bilgi verir. Bob'un qubiti (q2) hedef durumunda olmalıdır.
    qc.save_statevector()
    t_qc = transpile(qc, backend)
    result = backend.run(t_qc).result()
    final_statevector = result.get_statevector()
    
    # Bob'un qubitinin (q2) durumunu çıkar (Partial Trace)
    # Qiskit'te qubit sırası q2, q1, q0 şeklindedir (Little-endian)
    bob_final_state = AnalizAraclari.qubit_durumu_cikar(final_statevector, 2)
    
    print("[+] Simülasyon tamamlandı.")
    
    # 4. Sadakat (Fidelity) Hesaplama
    fidelity = AnalizAraclari.sadakat_hesapla(expected_psi, bob_final_state)
    
    # 5. Görselleştirme ve Raporlama
    if not os.path.exists("gorseller"):
        os.makedirs("gorseller")
        
    # Devre şemasını kaydet
    AnalizAraclari.devre_kaydet(qc, "gorseller/isinlanma_devresi.png")
    
    # Bloch küresi karşılaştırmasını kaydet
    AnalizAraclari.karsilastirmali_bloch_ciz(
        expected_psi, bob_final_state, 
        baslik1="Girdi (Alice)", baslik2="Çıktı (Bob)"
    )
    
    AnalizAraclari.sonuc_ozeti(theta, phi, fidelity.real)
    
    print(f"[i] Çizimler 'gorseller/' klasörüne kaydedildi.")
    print("=" * console_width)

if __name__ == "__main__":
    run_teleportation_test()
