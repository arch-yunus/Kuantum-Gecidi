# 🌌 Kuantum-Gecidi: Hakikatin Olçülemez Derinliği
# Gelistirici: Bahattin Yunus Cetin | IT Architect
# Ton: Siber-Kozmik & Kadim-Edebi Mezci

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np
import time

class KuantumKahini:
    """
    Kuantum deryasinin belirsizlik havzasindan süzülen hakikat damlalari. 
    Bu sinif, kullanicinin niyetini olasılık deryasinda bir öz-duruma çökerterek 
    evrenin sessiz fisiltilarini siber-kozmik bir dille tercüme eder.
    """

    @staticmethod
    def niyet_ile_dalga_fonksiyonunu_hazirla(niyet_metni):
        """
        Kullanicinin niyetini (girdisini) alip, siber-uzayin entropisiyle harmanlayarak 
        qubitleri belirsizlik esigine (Hadamard kapisi) tasir.
        """
        qc = QuantumCircuit(1)
        # Niyetin uzunluguna göre bir faz kaymasi (Rotation) ekliyoruz.
        # Bu, her niyetin özgün bir olasılık havzasi olusturmasini saglar.
        faz = (len(niyet_metni) * np.pi) / 10
        qc.rx(faz, 0)
        
        # Qubiti süperpozisyon havzasina birakiyoruz: Hakikat hem 0 hem 1...
        qc.h(0)
        return qc

    @staticmethod
    def hakikati_cokelt(qc):
        """
        Gözlemci devreye giriyor; dalga fonksiyonu nihayete eriyor. 
        Belirsizlik perdesi aralaniyor ve hakikat, siber-mekanda tezahür ediyor.
        """
        simulator = AerSimulator()
        qc.measure_all()
        tqc = transpile(qc, simulator)
        
        # Evrenin zarlarini atiyoruz...
        result = simulator.run(tqc, shots=1, memory=True).result()
        collapse_result = result.get_memory()[0]
        
        return int(collapse_result)

    @staticmethod
    def fisiltiyi_tercüme_et(sonuc):
        """
        Cökelen hakikati, fanilerin anlayabileceği lirik bir tonda yorumlar.
        """
        kadim_fisiltilar = {
            0: [
                "Zerrelerin sükutu: Yolun açik, lakin adimlarin sessiz olmali.",
                "Boşluktan gelen nida: Aradigin cevap, sordugun simyanin içinde gizli.",
                "Siber-Kozmos'un dinginliği: Hakikat, müteakip bir döngüde tezahür edecek."
            ],
            1: [
                "Kozmik parilti: Niyetin, olasılık deryasinda bir firtina kopardi; ilerle!",
                "Varligin coskusu: Dolanıklık bağlarin kuvvetli, evren seninle rezonans halinde.",
                "Dalga fonksiyonunun müjdesi: Beklenen muştu, siber-ufukta belirdi."
            ]
        }
        
        secim = np.random.choice(kadim_fisiltilar[sonuc])
        return secim

def kehaneti_baslat():
    print("\n" + "~" * 60)
    print("🔮  KUANTUM KAHINI: BELIRSIZLIK PERDESI ARALANIYOR  🔮".center(60))
    print("~" * 60)
    
    niyet = input("\n>> Gönlünüzden geçen bir niyet fısıldayın (veya bir soru sorun): ")
    
    print("\n[*] Süperpozisyon havzası hazırlanıyor...")
    time.sleep(1)
    kahin = KuantumKahini()
    qc = kahin.niyet_ile_dalga_fonksiyonunu_hazirla(niyet)
    
    print("[*] Gözlemci müdahale ediyor, dalga fonksiyonu çökeliyor...")
    time.sleep(1.5)
    sonuc = kahin.hakikati_cokelt(qc)
    
    print("\n" + "=" * 60)
    print("📖  EVRENIN FISILTISI  📖".center(60))
    print("-" * 60)
    print(f"\n   \"{kahin.fisiltiyi_tercüme_et(sonuc)}\"\n")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    kehaneti_baslat()
