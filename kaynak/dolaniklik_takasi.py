import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, partial_trace, DensityMatrix, state_fidelity

# Proje kök dizinini ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kaynak.analiz_araclari import AnalizAraclari

def run_entanglement_swapping():
    print("=" * 60)
    print("DOLANIKLIK TAKASI (ENTANGLEMENT SWAPPING) TESTI".center(60))
    print("=" * 60)
    
    # 4 Qubitlik Yapı
    # q0: Alice, q1: Charlie-A, q2: Charlie-B, q3: Bob
    qr = QuantumRegister(4, name="q")
    cr = ClassicalRegister(2, name="c_charlie")
    qc = QuantumCircuit(qr, cr)
    
    # Adım 1: İki bağımsız dolanık çift hazırla
    # Çift 1: Alice (0) ve Charlie-A (1)
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    
    # Çift 2: Charlie-B (2) ve Bob (3)
    qc.h(qr[2])
    qc.cx(qr[2], qr[3])
    qc.barrier()
    
    # Adım 2: Charlie (orta düğüm) dolanıklık takası işlemini yapar (Deferred Measurement)
    qc.cx(qr[1], qr[2])
    qc.h(qr[1])
    # Düzeltmeler: Charlie'nin qubitlerinden Bob'a (q3) 
    # Bu kombinasyon Alice(0) ve Bob(3) arasında |Phi+> oluşturur.
    qc.cx(qr[2], qr[3]) 
    qc.cz(qr[1], qr[3])
    qc.barrier()
    
    print("[+] Protokol devresi olusturuldu.")
    
    # Adım 4: Simülasyon ve Doğrulama
    backend = AerSimulator()
    qc.save_statevector()
    tqc = transpile(qc, backend)
    result = backend.run(tqc).result()
    final_sv = result.get_statevector()
    
    # Alice (q0) ve Bob (q3) arasındaki ilişkiyi incelemek için 
    # q1 ve q2 (Charlie'nin ölçülen qubitleri) üzerinden trace alıyoruz.
    rho_alice_bob = partial_trace(final_sv, [1, 2])
    
    # Hedef Bell durumu
    target_qc = QuantumCircuit(2)
    target_qc.h(0)
    target_qc.cx(0, 1)
    target_bell = Statevector.from_instruction(target_qc)
    target_rho = DensityMatrix(target_bell)
    
    fidelity = state_fidelity(target_rho, rho_alice_bob)
    
    # Adım 5: Kayıt ve Rapor
    if not os.path.exists("gorseller"):
        os.makedirs("gorseller")
    
    AnalizAraclari.devre_kaydet(qc, "gorseller/dolaniklik_takasi_devresi.png")
    
    print("\n" + "-" * 40)
    print("ANALIZ RAPORU: DOLANIKLIK TAKASI")
    print("-" * 40)
    print(f"Alice (q0) ve Bob (q3) Dolaniklik Sadakati: %{fidelity*100:.2f}")
    
    if fidelity > 0.99:
        print("v SONUC: Basarili! Alice ve Bob artik dolanik.")
    else:
        print("x SONUC: Takas basarisiz.")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    run_entanglement_swapping()
