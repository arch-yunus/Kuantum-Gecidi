# Tılsım-ı Hendese Projesi
# Kuantum Mimarı: Bahattin Yunus Çetin | IT Architect
# Protokol: Miftâh-ı Esrar (Gate Teleportation)

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import state_fidelity, partial_trace

def run_gate_teleportation():
    """
    Sırların miftâhını (anahtarını) Nur-Zerre transferiyle harmanlar.
    İşlem yapılmış bir durumu, Esir-Deryası üzerinden aktarır.
    """
    print("\n" + "=" * 60)
    print("      MİFTÂH-I ESRAR: KAPI IŞINLANMASI BAŞLATILDI      ".center(60))
    print("=" * 60)
    
    # Adım 1: Sırrı (U kapısı) bünyesinde barındıran Nur-Zerreleri hazırlıyoruz
    qc = QuantumCircuit(3)
    
    # Girdi durumu: Âlem-i Berzah'tan bir tecelli (Süperpozisyon)
    qc.h(0)
    
    # Alice & Bob arasındaki Râbıta (EPR)
    qc.h(1)
    qc.cx(1, 2)
    
    # Bob kendi miftâhını (U kapısı - e.g. T gate) önceden hazırlar
    qc.t(2)
    
    # Adım 2: Alice'in niyetini bağa mühürleme
    qc.cx(0, 1)
    qc.h(0)
    
    # Adım 3: Simya Laboratuvarında (AerSimulator) hakikati ortaya çıkarma
    simya_lab = AerSimulator()
    qc.save_statevector()
    tqc = transpile(qc, simya_lab)
    result = simya_lab.run(tqc).result()
    final_state = result.get_statevector()
    
    # Adım 4: Nazar-ı Tezahür (Partial Trace & Fidelity)
    # Bob'un nihai tecellisini (2. qubit) süzüyoruz
    rho_bob = partial_trace(final_state, [0, 1])
    
    # İdeal tecelli (Girdi + T kapısı)
    ideal_qc = QuantumCircuit(1)
    ideal_qc.h(0)
    ideal_qc.t(0)
    from qiskit.quantum_info import Statevector
    ideal_state = Statevector.from_instruction(ideal_qc)
    
    sadakat = state_fidelity(rho_bob, ideal_state)
    
    print("\n" + "-" * 40)
    print("      MİFTÂH ANALİZ RAPORU      ")
    print("-" * 40)
    print(f"Miftâh Sadakati (Fidelity): %{sadakat*100:.4f}")
    
    if sadakat > 0.99:
        print("\n[v] TECELİ: Miftâh Başarıyla Aktarıldı!")
    else:
        print("\n[x] TECELİ: Sırrın anahtarı Esir-Deryası'nda kayboldu.")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    run_gate_teleportation()
