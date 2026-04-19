# Tılsım-ı Hendese Projesi
# Kuantum Mimarı: Bahattin Yunus Çetin | IT Architect
# Protokol: Hata Deryası ve Kaos Analizi (Noise Modeling)

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, thermal_relaxation_error, amplitude_damping_error

def create_noise_model(prob_1q, prob_2q, t1=50e-6, t2=70e-6, gate_time=50e-9):
    """
    Kapsamlı bir gürültü modeli yaratır.
    prob_1q: 1-qubit kapı hata olasılığı (depolarizing)
    prob_2q: 2-qubit (CNOT) kapı hata olasılığı
    t1: Boyuna gevşeme süresi (Longitudinal relaxation)
    t2: Enine gevşeme süresi (Transverse relaxation)
    gate_time: Kapı işlem süresi
    """
    noise_model = NoiseModel()
    
    # 1. Depolarizing Hataları
    error_1q = depolarizing_error(prob_1q, 1)
    error_2q = depolarizing_error(prob_2q, 2)
    
    # 2. Thermal Relaxation (T1/T2) Hataları
    # Her qubit için aynı süreleri varsayıyoruz (basitlik için)
    error_thermal = thermal_relaxation_error(t1, t2, gate_time)
    
    # Hataları modele ekle
    # 1-qubit kapıları için hem depolarizing hem thermal relaxation
    error_combined_1q = error_1q.compose(error_thermal)
    noise_model.add_all_qubit_quantum_error(error_combined_1q, ['h', 'x', 'z', 't', 'ry', 'rz'])
    
    # 2-qubit kapıları için
    # Basitleştirme: 2-qubit termal hata (her iki qubit için)
    error_thermal_2q = error_thermal.tensor(error_thermal)
    error_combined_2q = error_2q.compose(error_thermal_2q)
    noise_model.add_all_qubit_quantum_error(error_combined_2q, ['cx'])
    
    return noise_model

def run_noise_analysis():
    """
    Laboratuvarın dışındaki gürültülü deryanın (Kaos) Nur-Zerreler üzerindeki etkisini inceler.
    Nifak-ı Zerre (Decoherence) seviyelerini haritalandırır.
    """
    print("\n" + "=" * 60)
    print("      HATA DERYASI: KAOS ANALİZİ BAŞLATILDI      ".center(60))
    print("=" * 60)
    
    error_rates = np.linspace(0, 0.1, 10)
    fidelities = []
    
    for p in error_rates:
        # Kaosun (Gürültü Modelinin) inşası
        noise_model = create_noise_model(p, p*2)
        
        # Basit bir Tayy-i Mekân zerresi
        qc = QuantumCircuit(1)
        qc.h(0)
        
        simya_lab = AerSimulator(noise_model=noise_model)
        qc.save_statevector()
        tqc = transpile(qc, simya_lab)
        result = simya_lab.run(tqc).result()
        rho_noisy = result.get_statevector()
        
        # İdeal tecelli ile karşılaştırma
        from qiskit.quantum_info import Statevector
        ideal_qc = QuantumCircuit(1)
        ideal_qc.h(0)
        rho_ideal = Statevector.from_instruction(ideal_qc)
        
        fidelities.append(state_fidelity(rho_noisy, rho_ideal))
        
    # Kaos Grafiğinin Nakşedilmesi
    plt.figure(figsize=(10, 6))
    plt.plot(error_rates, fidelities, marker='o', color='purple', label='Nazar-ı Sadakat')
    plt.title("Hata Deryasında Nur-Zerre Bozulması", fontsize=14)
    plt.xlabel("Kaos Oranı (Error Probability)", fontsize=12)
    plt.ylabel("Sadakat (Fidelity)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    output_path = "gorseller/hata_deryasi_analizi.png"
    plt.savefig(output_path)
    print(f"\n[v] Kaosun tasviri '{output_path}' olarak mühürlendi.")
    print(f"[*] En yüksek kaos seviyesinde bile sadakat: {fidelities[-1]:.4f}")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    run_noise_analysis()
