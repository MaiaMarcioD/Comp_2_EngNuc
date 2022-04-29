from Pf import Pessoa
from Conta import Conta
from Banco import Banco

def main():
    marcio = Pessoa("Márcio")
    marcio.setCpf(12601181770)
    marcio.set_telefone(982267596)
    marcio.setEmail("marciodmaia21@gmail.com")
    print(marcio)
    carine = Pessoa("Carine", 127831278213, 12309128409, "carine@gmail.com")
    print(carine)

    Corrente= Conta([marcio, carine], Nconta=1234)
    print(Corrente)
    Corrente.getAtributos()
    Corrente.deposito(12601181770, 500)
    Corrente.deposito(12601181770, 500)
    Corrente.deposito(126011870, 500)
    Corrente.getSaldo(12601181770)
    Corrente.saque(12601181770, 1000)
    Corrente.saque(12601181770, 1000)
    Corrente.saque(1260118, 122)
    Corrente.deposito(237126318, 2000)
    Corrente.historico(12601181770)

    Itau = Banco("Itau")
    Itau.cadastrasCliente()
    Itau.criaContas()
    Itau.mostraClientes()
    Itau.mostraContas()

if __name__ == "__main__":
    main()

    
