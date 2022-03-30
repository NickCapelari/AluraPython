from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("quantidade de digitos incorreta")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Invalido!!")
    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    def __str__(self):
        return self.format()

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Invalido!!")

    def valida(self, documento):
        validade_cnpj = CNPJ()
        return validade_cnpj.validate(documento)
    def format (self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    def __str__(self):
        return self.format()
