from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
prato_pao = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')

def main():
    print(bebida_suco)
    print(prato_pao)

if __name__ == '__main__':
    main()