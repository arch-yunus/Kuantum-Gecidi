import matplotlib.pyplot as plt
import numpy as np
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector

class AnalizAraclari:
    """
    Kuantum sonuçlarını görselleştirmek ve analiz etmek için araçlar.
    """
    
    @staticmethod
    def histogram_ciz(counts, baslik="Ölçüm Sonuçları"):
        """
        Ölçüm sonuçlarını histogram olarak çizer.
        """
        plt.figure(figsize=(10, 6))
        plot_histogram(counts, title=baslik)
        plt.show()

    @staticmethod
    def bloch_kuresi_ciz(state, baslik="Bloch Küresi"):
        """
        Bir kuantum durumunu Bloch küresi üzerinde gösterir.
        """
        if not isinstance(state, Statevector):
            state = Statevector(state)
        return plot_bloch_multivector(state, title=baslik)

    @staticmethod
    def qubit_durumu_cikar(full_state, qubit_index):
        """
        Çoklu qubit sisteminden belirli bir qubitin yoğunluk matrisini çıkarır.
        """
        from qiskit.quantum_info import partial_trace
        
        if not isinstance(full_state, Statevector):
            full_state = Statevector(full_state)
            
        # İlgili qubit dışındaki tüm qubitleri trace et
        n_qubits = full_state.num_qubits
        other_qubits = [i for i in range(n_qubits) if i != qubit_index]
        reduced_density_matrix = partial_trace(full_state, other_qubits)
        
        return reduced_density_matrix

    @staticmethod
    def karsilastirmali_bloch_ciz(state1, state2, baslik1="Girdi", baslik2="Çıktı"):
        """
        İki kuantum durumunu ayrı ayrı Bloch küresinde kaydeder.
        """
        fig1 = plot_bloch_multivector(state1, title=baslik1)
        fig1.savefig("gorseller/bloch_girdi.png")
        plt.close(fig1)

        fig2 = plot_bloch_multivector(state2, title=baslik2)
        fig2.savefig("gorseller/bloch_cikti.png")
        plt.close(fig2)
        
        print("[v] Karsilastirmali Bloch kureleri (girdi/cikti) kaydedildi.")
        return None

    @staticmethod
    def sadakat_hesapla(state1, state2):
        """
        İki kuantum durumu arasındaki sadakati (fidelity) hesaplar.
        """
        from qiskit.quantum_info import state_fidelity
        return state_fidelity(state1, state2)

    @staticmethod
    def devre_kaydet(qc, dosya_yolu):
        """
        Kuantum devresinin çizimini bir dosyaya kaydeder.
        """
        try:
            # Modern Qiskit 1.0+ için 'mpl' çiziciyi zorla
            qc.draw(output='mpl', filename=dosya_yolu)
            print(f"[v] Devre çizimi kaydedildi: {dosya_yolu}")
        except Exception as e:
            print(f"[!] MPL çizim hatası (Dosyaya metin olarak kaydediliyor): {e}")
            with open(dosya_yolu.replace('.png', '.txt'), 'w', encoding='utf-8') as f:
                f.write(str(qc.draw(output='text')))

    @staticmethod
    def sonuc_ozeti(theta, phi, fidelity):
        """
        Hazırlanan durum ve sadakat sonucu hakkında bilgi yazdırır.
        """
        print("\n" + "=" * 45)
        print("KUANTUM ISINLANMA ANALIZ RAPORU".center(45))
        print("-" * 45)
        print(f"[*] Hazirlanan Durum: theta={theta:.4f}, phi={phi:.4f}")
        print(f"[*] Iletim Sadakati: %{fidelity*100:.2f}")
        
        if fidelity > 0.99:
            print(f"[v] SONUC: MUKEMMEL AKTARIM")
        elif fidelity > 0.90:
            print(f"[!] SONUC: KABUL EDILEBILIR (Kayipli)")
        else:
            print(f"[x] SONUC: BASARISIZ (Veri kaybi yuksek)")
        print("=" * 45 + "\n")
