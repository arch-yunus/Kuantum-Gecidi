import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("""
    ============================================================
    🌌  KUANTUM-GECIDI: INTERAKTIF SIMULASYON MERKEZI  🌌
    ============================================================
    """)

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print("Lutfen bir simulasyon seciniz:")
        print("-" * 40)
        print("1) Standart Isinlanma Testi (Fidelity & Bloch)")
        print("2) Kapi Isinlanmasi (Gate Teleportation)")
        print("3) Gurultu ve Hata Analizi (NISQ Sim")
        print("4) Dolaniklik Takasi (Entanglement Swapping)")
        print("5) Proje Dokumantasyonunu Goruntule (README)")
        print("q) Cikis")
        print("-" * 40)
        
        choice = input("\nSeciminiz: ").strip().lower()
        
        if choice == '1':
            print("\n>> Standart Isinlanma baslatiliyor...")
            from kaynak.isinlanma_test import run_test
            run_test()
            input("\nDevam etmek icin Enter'a basin...")
        elif choice == '2':
            print("\n>> Kapi Isinlanmasi baslatiliyor...")
            from kaynak.gate_teleportation import run_gate_teleportation
            run_gate_teleportation()
            input("\nDevam etmek icin Enter'a basin...")
        elif choice == '3':
            print("\n>> Gurultu Analizi baslatiliyor...")
            from kaynak.gurultu_analizi import run_noise_analysis
            run_noise_analysis()
            input("\nDevam etmek icin Enter'a basin...")
        elif choice == '4':
            print("\n>> Dolaniklik Takasi baslatiliyor...")
            from kaynak.dolaniklik_takasi import run_entanglement_swapping
            run_entanglement_swapping()
            input("\nDevam etmek icin Enter'a basin...")
        elif choice == '5':
            with open("README.md", "r", encoding="utf-8") as f:
                print(f.read()[:1000] + "...") # Preview
            input("\nDevam etmek icin Enter'a basin...")
        elif choice == 'q':
            print("\nKuantum gecidinden cikiliyor. Iyi yolculuklar! 🚀")
            break
        else:
            print("\n[!] Gecersiz secim.")
            input("\nDevam etmek icin Enter'a basin...")

if __name__ == "__main__":
    main_menu()
