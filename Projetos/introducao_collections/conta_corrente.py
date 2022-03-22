from operator import attrgetter

class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self._saldo = 0

    def deposita (self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>> Codigo {} Saldo {} <<]".format(self.codigo, self._saldo)

    def __lt__(self, other): #deixando a classe de maneira comparavel
        return self._saldo < other._saldo


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

conta_do_gui = ContaCorrente(15)
print (conta_do_gui)
conta_do_gui.deposita(100)
print (conta_do_gui)
conta_da_dani = ContaCorrente(12)
conta_da_dani.deposita(1000)
print(conta_da_dani)
contas = [conta_da_dani, conta_do_gui]
for conta in contas:
    print(conta)
deposita_para_todas(contas)
for conta in contas:
    print(conta)
for conta in sorted(contas, key=attrgetter("_saldo")): #jeito para acessar atributos privados
    print("conta com sorted: {}".format(conta))

print(conta_da_dani > conta_do_gui)

for conta in sorted(contas): #ordenando de forma natural depois de implementar __lt__
    print(conta)




