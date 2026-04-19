import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, thermal_relaxation_error
from qiskit.quantum_info import Statevector, DensityMatrix, state_fidelity

# Proje kök dizinini ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kaynak.analiz_araclari import AnalizAraclari

def create_noise_model(prob_1q, prob_2q):
    """
    Basit bir gurultu modeli yaratir.
    prob_1q: 1-qubit kapi hata olasiligi
    prob_2q: 2-qubit (CNOT) kapi hata olasiligi
    """
    noise_model = NoiseModel()
    
    # 1-qubit depolarizing error
    error_1q = depolarizing_error(prob_1q, 1)
    noise_model.add_all_qubit_quantum_error(error_1q, ['h', 'x', 'z', 't'])
    
    # 2-qubit depolarizing error
    error_2q = depolarizing_error(prob_2q, 2)
    noise_model.add_all_qubit_quantum_error(error_2q, ['cx'])
    
    return noise_model

def simulate_teleportation_with_noise(noise_prob):
    """
    Verilen gurultu olasiligi ile bir teleportasyon simulasyonu yapar ve sadakati doner.
    """
    # 1. Kaynak Durum Prep (|1> durumu)
    psi = Statevector.from_label('1')
    rho = DensityMatrix(psi)
    
    # 2. Protokol Operatorleri
    # Ideal kanali ve gurultuyu manuel uygulayacagiz daha net sonuc icin
    
    # Kapi Hatalari
    error_1q = depolarizing_error(noise_prob, 1)
    error_2q = depolarizing_error(noise_prob * 10, 2)
    
    # Protokol: Alice'in qubiti psi, kanal qubitleri |Phi+>
    # Toplam sistem: psi (q0) x |Phi+> (q1, q2)
    bell_qc = QuantumCircuit(2)
    bell_qc.h(0)
    bell_qc.cx(0, 1)
    bell = Statevector.from_label('00').evolve(bell_qc)
    total_rho = DensityMatrix(psi.tensor(bell))
    
    # Alice'in islemleri (q0, q1)
    qc_alice = QuantumCircuit(3)
    qc_alice.cx(0, 1)
    qc_alice.h(0)
    
    # Gurultulu evrim
    total_rho = total_rho.evolve(qc_alice)
    # Burada basitlik adına her kapi sonrasi gurultu eklenebilir ama 
    # Qiskit'in evolve metodu gurultu modelini dogrudan almaz.
    # O yuzden AerSimulator ile devam edip metod='density_matrix' zorlayalim.
    
    simulator = AerSimulator(method='density_matrix', noise_model=create_noise_model(noise_prob, noise_prob*5))
    
    qc = QuantumCircuit(3)
    qc.x(0)
    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)
    # Deferred Measurement (Bob'un duzeltmeleri)
    qc.cx(1, 2)
    qc.cz(0, 2)
    qc.save_density_matrix()
    
    tqc = transpile(qc, simulator)
    result = simulator.run(tqc).result()
    final_rho = result.data()['density_matrix']
    
    # Bob'un qubitini (q2) cikar
    bob_rho = AnalizAraclari.qubit_durumu_cikar(final_rho, 2)
    
    target_rho = DensityMatrix.from_label('1')
    fidelity = state_fidelity(target_rho, bob_rho)
    
    return fidelity

def run_noise_analysis():
    print("=" * 60)
    print("GURULTU VE HATA ANALIZI: SADAKAT DEGISIMI".center(60))
    print("=" * 60)
    
    noise_levels = np.linspace(0, 0.05, 10)
    fidelities = []
    
    print("[*] Farkli gurultu seviyeleri simule ediliyor...")
    for p in noise_levels:
        f = simulate_teleportation_with_noise(p)
        fidelities.append(f)
        print(f"    Gurultu Olasiligi: {p:.4f} | Sadakat: %{f*100:.2f}")
    
    # Grafik Plotlama
    plt.figure(figsize=(10, 6))
    plt.plot(noise_levels, fidelities, marker='o', linestyle='-', color='red')
    plt.title("Hata Olasiligina Karsi Iletim Sadakati (Fidelity)")
    plt.xlabel("Kapi Hata Olasiligi (Depolarizing)")
    plt.ylabel("Sadakat (Fidelity)")
    plt.grid(True, alpha=0.3)
    
    if not os.path.exists("gorseller"):
        os.makedirs("gorseller")
    
    plt.savefig("gorseller/gurultu_analizi.png")
    print("\n[v] Analiz grafigi kaydedildi: gorseller/gurultu_analizi.png")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_noise_analysis()
