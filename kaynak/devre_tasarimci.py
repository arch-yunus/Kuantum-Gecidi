import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

class DevreTasarimci:
    """
    Kuantum devrelerini tasarlamak için yardımcı sınıf.
    """
    
    @staticmethod
    def isinlanma_devresi_hazirla():
        """
        Standart bir kuantum ışınlanma devresi (3 qubit) oluşturur.
        q0: Işınlanacak durum
        q1: Alice'in dolanık qubiti
        q2: Bob'un dolanık qubiti
        """
        qr = QuantumRegister(3, name="q")
        crz = ClassicalRegister(1, name="crz") # Alice'in Z ölçümü
        crx = ClassicalRegister(1, name="crx") # Alice'in X ölçümü
        qc = QuantumCircuit(qr, crz, crx)
        
        return qc, qr, crz, crx

    @staticmethod
    def dolaniklik_olustur(qc, q1, q2):
        """
        İki qubit arasında Bell durumu (dolanıklık) oluşturur.
        """
        qc.barrier()
        qc.h(q1)
        qc.cx(q1, q2)
        qc.barrier()
        return qc

    @staticmethod
    def alice_islemleri(qc, psi, q_alice):
        """
        Alice'in kendi qubitleri (psi ve q_alice) üzerindeki işlemlerini uygular.
        """
        qc.cx(psi, q_alice)
        qc.h(psi)
        qc.barrier()
        return qc

    @staticmethod
    def bob_duzeltmeleri(qc, q_bob, crz, crx):
        """
        Alice'in ölçüm sonuçlarına göre Bob'un qubitine düzeltme kapıları ekler.
        """
        with qc.if_test((crx, 1)):
            qc.x(q_bob)
        with qc.if_test((crz, 1)):
            qc.z(q_bob)
        return qc

    @staticmethod
    def durum_hazirla(qc, qubit, theta=None, phi=None):
        """
        Belirli bir qubiti istenen bir duruma getirir.
        Varsayılan: Rastgele bir durum.
        """
        if theta is None:
            theta = np.random.uniform(0, np.pi)
        if phi is None:
            phi = np.random.uniform(0, 2*np.pi)
            
        qc.ry(theta, qubit)
        qc.rz(phi, qubit)
        qc.barrier()
        return theta, phi
