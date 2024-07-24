class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca            
        self._modelo = modelo         
        self.__ano = None            

    def consultar_modelo(self):
        return self._modelo          

    def alterar_modelo(self, novo_modelo):
        self._modelo = novo_modelo   

    def consultar_ano(self):
        return self.__ano            

    def alterar_ano(self, novo_ano):
        self.__ano = novo_ano        


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor                

    def exibir_informacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.consultar_modelo()}')
        print(f'Cor: {self.cor}')


class Teste:
    def __init__(self):
        pass

    def executar(self):
        # Criando uma instância de Carro
        carro1 = Carro('Toyota', 'Corolla', 'Prata')

        # Acessando e modificando atributos
        print('Informações antes da alteração:')
        carro1.exibir_informacoes()

        carro1.alterar_modelo('Camry')
        carro1.alterar_ano(2023)

        print('\nInformações após a alteração:')
        carro1.exibir_informacoes()


# Testando as classes
if __name__ == "__main__":
    teste = Teste()
    teste.executar()

