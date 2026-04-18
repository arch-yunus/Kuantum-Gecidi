import os
import sys
import numpy as np
from qiskit import transpile
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector

# Proje kök dizinini ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kaynak.devre_tasarimci import DevreTasarimci
from kaynak.analiz_araclari import AnalizAraclari

def run_teleportation_test():
    console_width = 50
    print("=" * console_width)
    print("🌌 KUANTUM-GECIDI: ISINLANMA PROTOKOLU TESTI".center(console_width))
    print("=" * console_width)
    
    # 1. Hazırlık
    tasarimci = DevreTasarimci()
    qc, qr, crz, crx = tasarimci.isinlanma_devresi_hazirla()
    
    # Işınlanacak başlangıç durumunu (psi) belirle
    # Örnek: Adım adım bir durum hazırlayalım
    theta = 1.25  # rad
    phi = 0.8     # rad
    tasarimci.durum_hazirla(qc, qr[0], theta, phi)
    
    # Başlangıç durumunu Statevector olarak kaydet (Verifikasyon için)
    # Sadece ilk qubitin durumunu alıyoruz
    initial_psi = Statevector.from_instruction(qc.copy().remove_final_measurements())
    # Not: Bu statevector 3 qubitliktir, ancak Alice'in elindeki q0 durumunu temsil eder.
    
    # 2. Protokol Adımları
    tasarimci.dolaniklik_olustur(qc, qr[1], qr[2])
    tasarimci.alice_islemleri(qc, qr[0], qr[1])
    
    # Alice'in ölçümleri
    qc.measure(qr[0], crz)
    qc.measure(qr[1], crx)
    
    # Bob'un düzeltmeleri (Alice'in ölçümlerine bağlı)
    tasarimci.bob_duzeltmeleri(qc, qr[2], crz, crx)
    
    print("[+] Protokol devresi başarıyla oluşturuldu.")
    
    # 3. Simülasyon (Statevector Simulator kullanarak başarıyı ölçme)
    # Not: Ölçüm yapıldıktan sonra statevector çöker. 
    # Ancak stabil bir simülasyon için AerSimulator kullanabiliriz.
    
    backend = Aer.get_backend('statevector_simulator')
    tqc = transpile(qc, backend)
    result = backend.run(tqc).result()
    final_state = result.get_statevector(tqc)
    
    # Verifikasyon: Bob'un qubiti (q2) artık Alice'in orijinal q0 durumunda olmalı.
    # q2'nin durumunu izole edelim (Partial Trace yapısı)
    # Statevector.probabilities_dict([2]) ile q2'nin durumunu kontrol edebiliriz.
    # Ancak daha iyisi Fidelity hesaplamaktır.
    
    # Alice'in orijinal durumu (Sadece q0)
    # Basitçe: psi = cos(theta/2)|0> + e^{i*phi}sin(theta/2)|1>
    alice_original = [np.cos(theta/2), np.exp(1j*phi)*np.sin(theta/2)]
    
    # Bob'un final durumu (Partial Trace over q0, q1)
    # Qiskit quantum_info kullanarak izole edelim
    from qiskit.quantum_info import partial_trace
    rho_bob = partial_trace(final_state, [0, 1])
    
    # Sadakat (Fidelity) Hesapla
    fidelity = AnalizAraclari.sadakat_hesapla(alice_original, rho_bob)
    
    # 4. Görselleştirme ve Raporlama
    if not os.path.exists("gorseller"):
        os.makedirs("gorseller")
        
    AnalizAraclari.devre_kaydet(qc, "gorseller/isinlanma_tam_devre.png")
    AnalizAraclari.sonuc_ozeti(theta, phi, fidelity)
    
    print("\n[i] Detaylı analiz görseller/ klasörüne kaydedildi.")
    print("=" * console_width)

if __name__ == "__main__":
    run_teleportation_test()
