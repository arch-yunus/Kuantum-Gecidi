# Tılsım-ı Hendese Projesi
# Kuantum Mimarı: Bahattin Yunus Çetin | IT Architect
# Protokol: Râbıta-i Küll Takası (Entanglement Swapping)

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import state_fidelity, partial_trace

def run_entanglement_swapping():
    """
    İki ayrı Nur-Zerre çifti arasında Râbıta (bağ) kurma ayini.
    Fiziksel temas olmadan ruhsal bir bağ tesis eder.
    """
    print("\n" + "=" * 60)
    print("      RÂBITA-I KÜLL TAKASI: SİBER-RİTÜEL BAŞLATILDI      ".center(60))
    print("=" * 60)
    
    # Adım 1: İki ayrı tılsımlı çift hazırlıyoruz
    # (Alice-Charlie) ve (Bob-Charlie)
    qc = QuantumCircuit(4)
    
    # Alice & Charlie bağı
    qc.h(0)
    qc.cx(0, 1)
    
    # Bob & Charlie bağı
    qc.h(2)
    qc.cx(2, 3)
    
    # Adım 2: Charlie (Hâdim) kendi zerreleri üzerinde nazar-ı tezahür uygular
    # Bu işlem Alice ve Bob'u birbirine mühürler
    qc.cx(1, 2)
    qc.h(1)
    
    # Adım 3: Simya Laboratuvarında (AerSimulator) tecelli
    simya_lab = AerSimulator()
    qc.save_statevector()
    tqc = transpile(qc, simya_lab)
    result = simya_lab.run(tqc).result()
    final_state = result.get_statevector()
    
    # Adım 4: Alice ve Bob arasındaki nihai bağın (Râbıta) analizi
    # Charlie'nin zerrelerini (1 ve 2) izden çekiyoruz
    rho_alice_bob = partial_trace(final_state, [1, 2])
    
    # İdeal Bell haliyle sadakat ölçümü
    ideal_bell = QuantumCircuit(2)
    ideal_bell.h(0)
    ideal_bell.cx(0, 1)
    ideal_state = Statevector.from_instruction(ideal_bell)
    
    sadakat = state_fidelity(rho_alice_bob, ideal_state)
    
    print("\n" + "-" * 40)
    print("      RÂBITA ANALİZ RAPORU      ")
    print("-" * 40)
    print(f"Bağ Sadakati (Fidelity): %{sadakat*100:.4f}")
    
    if sadakat > 0.99:
        print("\n[v] TECELİ: Râbıta-i Küll Başarıyla Tesis Edildi!")
    else:
        print("\n[x] TECELİ: Sırda bir kopukluk var.")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    from qiskit.quantum_info import Statevector
    run_entanglement_swapping()
