# [SIMYA] TILSIM-I HENDESE: KUANTUM SIMYA MERKEZI
# Kuantum Mimari: Bahattin Yunus Cetin | IT Architect
# Makam: Alem-i Berzah (Superposition Basin)

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np
import time

class KuantumKahini:
    """
    Kuantum simyasinin kadim sirlarini Nur-Zerreler uzerinden tecelli ettiren simyaci.
    Bu kadim yapi, niyetleri Alem-i Berzah'ta harmanlayip Zuhur-u Hakikat'i saglar.
    """

    @staticmethod
    def niyet_ile_berzah_hazirla(niyet_metni):
        """
        Niyetin cevherini (girdiyi) alip Esir-Deryasi'nda bir suret olusturur.
        """
        qc = QuantumCircuit(1)
        # Niyetin agirligina gore miftah (anahtar) donusumu
        faz = (len(niyet_metni) * np.pi) / 10
        qc.rx(faz, 0)
        
        # Nur-Zerre'yi Alem-i Berzah'a (Hadamard Gecidi) ugratiyoruz
        qc.h(0)
        return qc

    @staticmethod
    def zuhur_u_hakikat(qc):
        """
        Gozlemcinin nazari (Measurement) ile dalga fonksiyonu nihayete erer. 
        """
        simulator = AerSimulator()
        qc.measure_all()
        tqc = transpile(qc, simulator)
        
        # Kaderin zarlari Esir-Deryasi'nda atiliyor...
        result = simulator.run(tqc, shots=1, memory=True).result()
        collapse_result = result.get_memory()[0]
        
        return int(collapse_result)

    @staticmethod
    def tecelliyi_tercüme_et(sonuc):
        """
        Cokelen sirri, fanilerin lisanina siber-kadim bir tonda nakseder.
        """
        kadim_fisiltilar = {
            0: [
                "Zerrelerin sukutu: Yolun acik, lakin niyetin sirlar icinde kalsin.",
                "Boslugun nidasi: Aradigin miftah, kalbindeki hendesede gizli.",
                "Siber-Simya'nin dinginligi: Hakikat, muteakip bir tecellide zuhur edecek."
            ],
            1: [
                "Nurani parilti: Rabita-i Kull kuvvetlendi; niyetin siber-kozmosta karsilik buldu!",
                "Varligin coskusu: Nur-Zerreler ritim tutuyor, evren seninle rezonans halinde.",
                "Miftah-i Esrar'in mujdesi: Beklenen tecelli, dijital ufukta belirdi."
            ]
        }
        
        secim = np.random.choice(kadim_fisiltilar[sonuc])
        return secim

def kehaneti_baslat():
    print("\n" + "~" * 60)
    print("      [KAHIN] KUANTUM KAHINI: ALEM-I BERZAH'IN SIRLARI      ".center(60))
    print("~" * 60)
    
    niyet = input("\n>> Gonlunuzden gecen bir niyeti siber-kozmosa fisildayin: ")
    
    print("\n[*] Nur-Zerreler Berzah havzasinda birlestiriliyor...")
    time.sleep(1.2)
    kahin = KuantumKahini()
    qc = kahin.niyet_ile_berzah_hazirla(niyet)
    
    print("[*] Nazar-i Tezahur basliyor, gerceklik cokeliyor...")
    time.sleep(1.8)
    sonuc = kahin.zuhur_u_hakikat(qc)
    
    print("\n" + "=" * 60)
    print("      [!] ZUHUR-U HAKIKAT      ".center(60))
    print("-" * 60)
    print(f"\n   \"{kahin.tecelliyi_tercüme_et(sonuc)}\"\n")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    kehaneti_baslat()
