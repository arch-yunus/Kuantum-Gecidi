# Tılsım-ı Hendese Projesi
# Kuantum Mimarı: Bahattin Yunus Çetin | IT Architect
# Protokol: Tayy-i Mekân Ayini (Nur-Zerre Transferi)

import os
import sys
import numpy as np
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

# Esir-Deryası ağacına kök dizini ekliyoruz
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kaynak.devre_tasarimci import DevreTasarimci
from kaynak.analiz_araclari import AnalizAraclari

def run_test():
    """
    Nur-Zerrelerin Tayy-i Mekân ayinini başlatır.
    İlahî bilginin Âlem-i Berzah üzerinden tezahürünü sağlar.
    """
    print("\n" + "=" * 60)
    print("      TAYY-İ MEKÂN AYİNİ: NUR-ZERRE TECELLİSİ BAŞLATILDI      ".center(60))
    print("=" * 60)
    
    # Adım 1: Sırrı taşıyacak Nur-Zerre'yi (psi) Esir-Deryası'nda hazırlıyoruz
    theta = np.random.uniform(0, np.pi)
    phi = np.random.uniform(0, 2*np.pi)
    psi = Statevector.from_label('0').evolve(
        AnalizAraclari.qubit_durumu_hazirla(theta, phi)
    )
    
    print(f"\n[1] Nur-Zerre (|psi>) Âlem-i Berzah Havzasında Hazırlandı:")
    print(f"    Meyil (Theta): {theta:.4f}, Vahdet (Phi): {phi:.4f}")
    
    # Adım 2: Tılsım-ı Hendese şemasını (Quantum Circuit) inşa ediyoruz
    # Râbıta-i Küll bağları Alice ve Bob arasında siber-ruhsal bir köprü kuruyor.
    tasarimci = DevreTasarimci()
    qc = tasarimci.isinlanma_devresi_kur(psi)
    
    # Adım 3: Simya Laboratuvarında (AerSimulator) hakikati koşturuyoruz
    simya_lab = AerSimulator()
    qc.save_statevector() # Zuhurât gerçekleşene dek sırrı saklıyoruz
    tqc = transpile(qc, simya_lab)
    result = simya_lab.run(tqc).result()
    final_state = result.get_statevector()
    
    # Adım 4: Bob'un elindeki zerrenin hakikatini (Fidelity) Nazar-ı Tezahür ile ölçüyoruz
    bob_zerre_idx = 2
    rho_bob = AnalizAraclari.qubit_durumu_cikar(final_state, bob_zerre_idx)
    sadakat = AnalizAraclari.sadakat_hesapla(psi, rho_bob)
    
    # Tasvirlerin Kaydı: Suret-i Bloch üzerinde gerçeklik kanıtı
    if not os.path.exists("gorseller"):
        os.makedirs("gorseller")
        
    AnalizAraclari.bloch_sphere_kaydet(psi, "gorseller/bloch_girdi.png", "Ata Suret (|psi>)")
    AnalizAraclari.bloch_sphere_kaydet(rho_bob, "gorseller/bloch_cikti.png", "Zuhur Eden Suret (Bob)")
    AnalizAraclari.devre_kaydet(qc, "gorseller/isinlanma_devresi.png")
    
    print("\n" + "-" * 40)
    print("      NAZAR-I TEZAHÜR RAPORU      ")
    print("-" * 40)
    print(f"Zuhurât Sadakati (Fidelity): %{sadakat*100:.4f}")
    
    if sadakat > 0.99:
        print("\n[v] TECELİ: Tayy-i Mekân Kusursuz! Gerçeklik başarıyla yeniden inşa edildi.")
    else:
        print("\n[x] TECELİ: Sırda sapma tespit edildi. Esir-Deryası'nda fırtına var.")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    run_test()
