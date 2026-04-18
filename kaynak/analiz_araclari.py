import matplotlib.pyplot as plt
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
    def karsilastirmali_bloch_ciz(state1, state2, baslik1="Girdi", baslik2="Çıktı"):
        """
        İki kuantum durumunu yan yana Bloch küresinde gösterir.
        """
        fig = plt.figure(figsize=(12, 6))
        ax1 = fig.add_subplot(1, 2, 1)
        ax2 = fig.add_subplot(1, 2, 2)
        
        plot_bloch_multivector(state1, title=baslik1, ax=ax1)
        plot_bloch_multivector(state2, title=baslik2, ax=ax2)
        return fig

    @staticmethod
    def sadakat_hesapla(state1, state2):
        """
        İki kuantum durumu arasındaki sadakati (fidelity) hesaplar.
        1.0 tam eşleşme demektir.
        """
        if not isinstance(state1, Statevector):
            state1 = Statevector(state1)
        if not isinstance(state2, Statevector):
            state2 = Statevector(state2)
            
        from qiskit.quantum_info import state_fidelity
        fidelity = state_fidelity(state1, state2)
        return fidelity

    @staticmethod
    def devre_kaydet(qc, dosya_yolu):
        """
        Kuantum devresinin çizimini bir dosyaya kaydeder.
        """
        try:
            qc.draw(output='mpl', filename=dosya_yolu)
            print(f"Devre çizimi şuraya kaydedildi: {dosya_yolu}")
        except Exception as e:
            print(f"Devre çizilemedi (Matplotlib/Pylatexenc hatası): {e}")
            qc.draw(output='text', filename=dosya_yolu.replace('.png', '.txt'))

    @staticmethod
    def sonuc_ozeti(theta, phi, fidelity):
        """
        Hazırlanan durum ve sadakat sonucu hakkında bilgi yazdırır.
        """
        print("-" * 40)
        print("KUANTUM ISINLANMA ANALIZ OZETI")
        print("-" * 40)
        print(f"Hazırlanan Durum: Theta={theta:.4f}, Phi={phi:.4f}")
        print(f"Işınlanma Sadakati (Fidelity): {fidelity:.4f}")
        
        if fidelity > 0.99:
            print("BAŞARILI: Kuantum bilgisi mükemmel aktarıldı!")
        else:
            print("UYARI: Sadakat düşük. Devreyi kontrol edin.")
        print("-" * 40)
