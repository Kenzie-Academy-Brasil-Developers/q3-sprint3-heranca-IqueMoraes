# Desenvolva sua classe Recipiente aqui.


class Recipiente:

    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = True) -> None:
        if tamanho < 0:
            self.tamanho = 0
        else:
            self.tamanho = tamanho
        self.conteudo = conteudo
        self.limpo = limpo

    def esvaziar(self) -> None:
        self.conteudo = 0
    
    def esta_vazio(self) -> bool:
        if self.conteudo == 0:
            return True
        else:
            return False

    def lavar(self) -> None:
        self.conteudo = 0
        self.limpo = True
    
    def esta_limpo(self) -> bool:
        if self.limpo:
            return True
        else:
            return False

    
    def estado(self) -> str:
        if self.limpo:
            return "limpo"
        else:
            return "sujo"
    
    def sujar(self) -> None:
        self.limpo = False

    
    def __repr__(self)-> str:
        return f"Um recipiente {self.estado()} não especificado"

    def __str__(self)-> str:
        return f"Um recipiente {self.estado()} não especificado"

