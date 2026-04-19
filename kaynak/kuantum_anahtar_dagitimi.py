# Tılsım-ı Hendese Projesi
# Kuantum Mimarı: Bahattin Yunus Çetin | IT Architect
# Protokol: Sırların Paylaşımı (BB84 QKD)

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def run_qkd_simulation():
    """
    Alice ve Bob arasında Nur-Zerreler üzerinden sır paylaşımı (Anahtar Dağıtımı).
    No-Cloning kanunuyla korunan ilahî bir mühür oluşturur.
    """
    print("\n" + "=" * 60)
    print("      SIRLARIN PAYLAŞIMI: BB84 QKD BAŞLATILDI      ".center(60))
    print("=" * 60)
    
    n_bits = 20 # Paylaşılacak sırrın uzunluğu
    
    # 1. Alice niyetini (rastgele bitler) ve miftâhlarını (bazlar) hazırlar
    alice_bits = np.random.randint(2, size=n_bits)
    alice_bases = np.random.randint(2, size=n_bits) # 0: Z (Düz), 1: X (Çapraz)
    
    # 2. Nur-Zerrelerin Esir-Deryası'na salınması
    bob_results = []
    bob_bases = np.random.randint(2, size=n_bits)
    
    simya_lab = AerSimulator()
    
    for i in range(n_bits):
        qc = QuantumCircuit(1, 1)
        
        # Alice bitini kodluyor
        if alice_bits[i] == 1:
            qc.x(0)
            
        # Alice bazını seçiyor (Miftâh-ı Esrar)
        if alice_bases[i] == 1:
            qc.h(0)
            
        # Bob kendi miftâhı ile Nazar-ı Tezahür uyguluyor
        if bob_bases[i] == 1:
            qc.h(0)
            
        qc.measure(0, 0)
        
        tqc = transpile(qc, simya_lab)
        result = simya_lab.run(tqc, shots=1, memory=True).result()
        bob_results.append(int(result.get_memory()[0]))
        
    # 3. Sırrın Ayıklanması (Sifting)
    # Alice ve Bob miftâhlarını (bazlarını) karşılaştırır
    agreed_key = []
    for i in range(n_bits):
        if alice_bases[i] == bob_bases[i]:
            agreed_key.append(alice_bits[i])
            
    print(f"\n[1] Alice'in Niyeti:  {alice_bits}")
    print(f"[2] Bob'un Tezahürü: {np.array(bob_results)}")
    print(f"[3] Ortak Miftâhlar: {alice_bases == bob_bases}")
    print(f"\n[v] Mühürlenmiş Sır (Final Key): {agreed_key}")
    print(f"[*] Sırrı başarıyla paylaştınız. {len(agreed_key)} bitlik mühür tesis edildi.")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    run_qkd_simulation()
