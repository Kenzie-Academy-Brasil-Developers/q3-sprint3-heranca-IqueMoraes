# Desenvolva sua classe Copo aqui.
from classes.recipiente import Recipiente

class Copo(Recipiente):

    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = True) -> None:
        super().__init__(tamanho, conteudo=conteudo, limpo=limpo)

    
    def encher(self, bebida: str = "água")-> str:
        if self.esta_limpo():
            self.sujar()
            self.conteudo = self.tamanho
            self.bebida = bebida
        else:
            return "Não se pode encher um copo sujo"

    def beber(self, quantidade: float)->str:
        if quantidade <= 0:
            return "Quantidade deve ser positiva"
        elif quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        else:
            self.conteudo = self.conteudo - quantidade

    def lavar(self) -> None:
        super().lavar()
        self.bebida = None

    
    def __repr__(self) -> str:
        if self.conteudo == 0:
            return f"Um copo vazio de {float(self.tamanho)}ml"
        else:
            return f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"

    def __str__(self) -> str:
        if self.conteudo == 0:
            return f"Um copo vazio de {float(self.tamanho)}ml"
        else:
            return f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"


c = Copo(300)
print(c)
c.encher('café')
print(c.bebida)
print(c)
c.beber(30)
print(c)
c.lavar()
print(c.esta_limpo())