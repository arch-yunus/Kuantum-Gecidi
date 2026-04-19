import os
import sys
import io

# [KORUMA] Terminal kodlamasını UTF-8'e zorluyoruz (Emoji ve Egzotik karakterler için)
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    # 'Simyasal' bir hava katan ASCII Banner
    print(r"""
    .---.      .---.      .---.      .---.      .---.
   /   / \    /   / \    /   / \    /   / \    /   / \
  |   |   |  |   |   |  |   |   |  |   |   |  |   |   |
   \   \ /    \   \ /    \   \ /    \   \ /    \   \ /
    '---'      '---'      '---'      '---'      '---'
    
    ============================================================
           [SIMYA]  TILSIM-I HENDESE: KUANTUM SIMYA MERKEZI [SIMYA]
    ------------------------------------------------------------
    Makam: Hibrit Kuantum (Python & Julia Yao.jl)
    Kuantum Mimari: Bahattin Yunus Cetin | IT Architect
    ============================================================
    """)

def check_julia():
    import subprocess
    try:
        subprocess.check_output(["julia", "--version"])
        return True
    except:
        return False

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print("  Âlem-i Berzah'tan bir tecelli seçin:")
        print("-" * 55)
        print("1) Standart Isinlanma Testi (Python / Qiskit)")
        print("2) Julia Simya Ayini (Julia / Yao.jl) [EXOTIC]")
        print("3) Kapi Isinlanmasi (Gate Teleportation)")
        print("4) Gurultu ve Hata Analizi (NISQ Sim)")
        print("5) Dolaniklik Takasi (Entanglement Swapping)")
        print("6) Çoklu Qubit Isinlanma (Multi-Qubit)")
        print("7) Kuantum Tekrarlayici Zinciri (Quantum Repeater)")
        print("8) Proje Dokumantasyonunu Goruntule (README)")
        print("9) 🔮 Kuantum Kahini'ne Danis (Belirsizligin Sesini Duy)")
        print("q) Cikis")
        print("-" * 55)
        
        choice = input("\nNazarınız (Gerçeklik çökeliyor...): ").strip().lower()
        
        if choice == '1':
            print("\n>> Nur-Zerreler hizalaniyor...")
            from kaynak.isinlanma_test import run_test
            run_test()
            input("\nBerzah'tan dönmek için Enter'a basın...")
        elif choice == '2':
            if check_julia():
                print("\n>> Julia Simya Labaratuvari açiliyor...")
                os.system("julia kaynak/isinlanma_ayini.jl")
            else:
                print("\n[!] Kadim lisan (Julia) sistemde bulunamadi.")
                print("[*] Lütfen 'https://julialang.org/' üzerinden Julia'yı yükleyin.")
            input("\nBerzah'tan dönmek için Enter'a basın...")
        elif choice == '3':
            print("\n>> Kapi Esrari aciliyor...")
            from kaynak.gate_teleportation import run_gate_teleportation
            run_gate_teleportation()
            input("\nBerzah'tan dönmek için Enter'a basın...")
        elif choice == '4':
            print("\n>> Kaosun deryasında hata zerreleri aranıyor...")
            from kaynak.gurultu_analizi import run_noise_analysis
            run_noise_analysis()
            input("\nBerzah'tan dönmek için Enter'a basın...")
        elif choice == '5':
            print("\n>> Ruhsal bağlar evrensel bir ağ kuruyor...")
            from kaynak.dolaniklik_takasi import run_entanglement_swapping
            run_entanglement_swapping()
            input("\nBerzah'tan dönmek için Enter'a basın...")
        elif choice == '6':
            print("\n>> Çoklu Qubit Isinlanma baslatiliyor...")
            from kaynak.multi_qubit_teleportasyonu import run_multi_qubit_teleportation
            run_multi_qubit_teleportation(3)
            input("\nDevam etmek icin Enter'a basin...")
        elif choice == '7':
            print("\n>> Kuantum Tekrarlayici Zinciri baslatiliyor...")
            from kaynak.kuantum_tekrarlayici import run_quantum_repeater_demo
            run_quantum_repeater_demo(3)
            input("\nDevam etmek icin Enter'a basin...")
        elif choice == '8':
            try:
                with open("README.md", "r", encoding="utf-8") as f:
                    print("\n📖 Simya Arşivinden Kadim Bilgiler:\n")
                    print(f.read()[:500] + "...") 
            except Exception as e:
                print(f"\n[!] Arşiv okunamadı: {e}")
            input("\nDevam etmek icin Enter'a basin...")
        elif choice == '9':
            print("\n>> Kehanet dalgaları zihin deryasında süzülüyor...")
            from kaynak.kuantum_kahini import kehaneti_baslat
            kehaneti_baslat()
            input("\nDevam etmek icin Enter'a basin...")
        elif choice == 'q':
            print("\nSimya laboratuvarı mühürleniyor. Nur-Zerreler sönümlendi. 🚀")
            break
        else:
            print("\n[!] Geçersiz tecelli. Olasılık deryasında kayboldunuz.")
            input("\nYola devam etmek için Enter'a basın...")

if __name__ == "__main__":
    main_menu()
