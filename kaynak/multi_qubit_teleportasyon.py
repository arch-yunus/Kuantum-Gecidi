# Tılsım-ı Hendese Projesi
# Kuantum Mimarı: Bahattin Yunus Çetin | IT Architect
# Protokol: Küllî Tayy-i Mekân (Multi-Qubit Teleportation)

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, state_fidelity, partial_trace

# Esir-Deryası ağacına kök dizini ekliyoruz
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kaynak.devre_tasarimci import DevreTasarimci
from kaynak.analiz_araclari import AnalizAraclari

def run_multi_qubit_teleportation():
    """
    Küllî Tayy-i Mekân: Birden fazla Nur-Zerre'nin kolektif tecellisi.
    Vahdet-i Mevcud (Global State) üzerinden hakikati yeniden inşa eder.
    """
    print("\n" + "=" * 65)
    print("      KULLI TAYY-I MEKAN: COKLU NUR-ZERRE AYINI BASLATILDI      ".center(65))
    print("=" * 65)
    
    try:
        # Terminal encoding issues on Windows: using safe input
        prompt = "\n>> Kac adet Nur-Zerre tayy-i mekan edilsin? (Max 8, Oneri: 3): "
        val = input(prompt) or "3"
        n_zerre = int(val)
    except ValueError:
        n_zerre = 3
        
    if n_zerre > 8:
        print("[!] Siniri astiniz. Sukunet icin 8 zerre secildi.")
        n_zerre = 8
    elif n_zerre < 1:
        n_zerre = 1

    print(f"\n[*] {n_zerre} adet Nur-Zerre Alem-i Berzah'a hazirlaniyor...")
    
    # Adım 1: Her bir zerre için girdi durumlarını hazırlıyoruz
    input_states = []
    for i in range(n_zerre):
        theta = np.random.uniform(0, np.pi)
        phi = np.random.uniform(0, 2*np.pi)
        psi = Statevector.from_label('0').evolve(
            AnalizAraclari.qubit_durumu_hazirla(theta, phi)
        )
        input_states.append(psi)
        
    # Adım 2: Küllî Tılsım-ı Hendese (Parallel Teleportation Circuit)
    qc = QuantumCircuit(n_zerre * 3)
    
    for i in range(n_zerre):
        psi_idx = i * 3
        alice_idx = i * 3 + 1
        bob_idx = i * 3 + 2
        
        qc.prepare_state(input_states[i], [psi_idx])
        qc.h(alice_idx)
        qc.cx(alice_idx, bob_idx)
        qc.cx(psi_idx, alice_idx)
        qc.h(psi_idx)
        
        with qc.if_test((qc.measure(psi_idx), 1)):
            qc.z(bob_idx)
        with qc.if_test((qc.measure(alice_idx), 1)):
            qc.x(bob_idx)
            
    # Adım 3: Simya Laboratuvarında (AerSimulator) hakikati arama
    print("[*] Esir-Deryasi'nda dalga fonksiyonlari kosturuluyor...")
    simya_lab = AerSimulator()
    qc.save_statevector()
    tqc = transpile(qc, simya_lab)
    result = simya_lab.run(tqc).result()
    v_mevcud = result.get_statevector()
    
    # Adım 4: Nazar-ı Tezahür ve Analiz
    print("\n" + "-" * 40)
    print("      KULLI TEZAHUR RAPORU      ")
    print("-" * 40)
    
    total_sadakat = 1.0
    
    if not os.path.exists("gorseller/multi"):
        os.makedirs("gorseller/multi")

    for i in range(n_zerre):
        indices_to_trace = [j for j in range(n_zerre * 3) if j != (i * 3 + 2)]
        rho_bob = partial_trace(v_mevcud, indices_to_trace)
        
        sadakat = state_fidelity(rho_bob, input_states[i])
        total_sadakat *= sadakat
        
        print(f"Zerre #{i+1} Sadakati: %{sadakat*100:.4f}")
        
        if i < 3:
            AnalizAraclari.bloch_sphere_kaydet(input_states[i], f"gorseller/multi/girdi_{i+1}.png", f"Zerre #{i+1} Girdi")
            AnalizAraclari.bloch_sphere_kaydet(rho_bob, f"gorseller/multi/cikti_{i+1}.png", f"Zerre #{i+1} Cikti")

    print("-" * 40)
    print(f"KOLEKTIF SADAKAT (Global Fidelity): %{total_sadakat*100:.4f}")
    
    if total_sadakat > 0.95:
        print("\n[v] TECELI: Kulli Tayy-i Mekan Basariyla Muhurlendi!")
    else:
        print("\n[x] TECELI: Kulli yapida sapmalar var. Kaos artiyor.")
        
    print("-" * 65 + "\n")

if __name__ == "__main__":
    run_multi_qubit_teleportation()
