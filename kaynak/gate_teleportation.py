import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, DensityMatrix, state_fidelity

# Proje kök dizinini ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kaynak.analiz_araclari import AnalizAraclari

def run_gate_teleportation():
    print("=" * 60)
    print("KUANTUM KAPI ISINLANMASI (GATE TELEPORTATION) TESTI".center(60))
    print("=" * 60)
    
    # 1. Kaynak Hazirliği (Gate-Infused Resource State)
    # Hedef: Bir T-gate işlemini ışınlayacağız.
    qr = QuantumRegister(3, name="q")
    cr = ClassicalRegister(2, name="c")
    qc = QuantumCircuit(qr, cr)
    
    # Adım 1: Alice (q1) ve Bob (q2) arasında Bell Durumu
    qc.h(qr[1])
    qc.cx(qr[1], qr[2])
    
    # Adım 2: Bob'un qubitine ışınlamak istediğimiz kapıyı uyguluyoruz (T-Gate)
    # Bu noktada kanal (I x T)|Phi+> durumundadır.
    qc.t(qr[2])
    qc.barrier()
    
    # 2. Hazırlanan Durum (Alice'in ışınlamak istediği durum)
    # Örnek: q0 qubitini |+> durumuna getirelim (Hadamard ile)
    qc.h(qr[0])
    qc.barrier()
    
    # Beklenen Çıktı Analizi
    # Alice'in qubiti |+> ve kapı T olduğu için sonuç T|+> olmalıdır.
    target_qc = QuantumCircuit(1)
    target_qc.h(0)
    target_qc.t(0)
    target_matrix = Statevector.from_instruction(target_qc)
    
    # 3. Işınlanma Protokolü
    # Alice kendi qubitleri (target q0 ve kanal q1) üzerinde Bell ölçümü yapar
    qc.cx(qr[0], qr[1])
    qc.h(qr[0])
    qc.measure(qr[0], cr[0])
    qc.measure(qr[1], cr[1])
    qc.barrier()
    
    # 4. Bob'un Düzeltmeleri
    # Alice'in ölçüm sonuçlarına göre Bob kendi qubitini (q2) düzeltir
    with qc.if_test((cr[0], 1)):
        qc.z(qr[2])
    with qc.if_test((cr[1], 1)):
        qc.x(qr[2])
    
    print("[+] Kapı Işınlanması devresi oluşturuldu (T-Gate).")
    
    # 5. Simülasyon
    backend = AerSimulator(method='statevector')
    qc.save_statevector()
    t_qc = transpile(qc, backend)
    result = backend.run(t_qc).result()
    final_sv = result.get_statevector()
    
    # Bob'un qubit durumunu (q2) çıkar
    bob_state = AnalizAraclari.qubit_durumu_cikar(final_sv, 2)
    fidelity = state_fidelity(target_matrix, bob_state)
    
    # Adım 6: Sonuçlar
    if not os.path.exists("gorseller"):
        os.makedirs("gorseller")
        
    AnalizAraclari.devre_kaydet(qc, "gorseller/kapi_isinlanmasi_devresi.png")
    
    print("\n" + "-" * 40)
    print("ANALIZ RAPORU: KAPI ISINLANMASI")
    print("-" * 40)
    print(f"Isinlanan Kapi: T-Gate")
    print(f"Girdi Durumu: |+>")
    print(f"Hesaplanan Sadakat (Fidelity): %{fidelity*100:.2f}")
    
    if fidelity > 0.99:
        print("v SONUC: Kapi islemi basariyla isinlandi!")
    else:
        print("x SONUC: Hata payi yuksek.")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    run_gate_teleportation()
