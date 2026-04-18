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
    def devre_kaydet(qc, dosya_yolu):
        """
        Kuantum devresinin çizimini bir dosyaya kaydeder.
        """
        qc.draw(output='mpl', filename=dosya_yolu)
        print(f"Devre çizimi şuraya kaydedildi: {dosya_yolu}")

    @staticmethod
    def sonuc_ozeti(theta, phi, counts):
        """
        Hazırlanan durum ve ölçüm sonuçları hakkında bilgi yazdırır.
        """
        print("-" * 30)
        print("ANALIZ OZETI")
        print("-" * 30)
        print(f"Hazırlanan Durum Açısı (Theta): {theta:.4f} rad")
        print(f"Hazırlanan Faz Açısı (Phi): {phi:.4f} rad")
        print(f"Toplam Ölçüm Sayısı (Shots): {sum(counts.values())}")
        print("-" * 30)
