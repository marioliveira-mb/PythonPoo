from models.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Mariana', 10)
restaurante_praca.receber_avaliacao('Mari', 2)

# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

# restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()