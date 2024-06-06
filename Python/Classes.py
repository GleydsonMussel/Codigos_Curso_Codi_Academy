
# Para Encapsulamento: _ -> Protected, __ -> Privado, basta colocá-los antes do nome de um atributo ou método para deixá-lo encapsulado

class Classe:
    
    # Variáveis declaradas fora dos métodos, viram atributos da classe
    n_objetos = 0
    
    # Construtor
    def __init__(self, atributo1, atributo2, atributo3):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self.__atributo_privado = atributo3
        Classe.n_objetos += 1
    
    # Método de objeto
    def printa_dados_objeto(self):
        print("Atributo 1: "+str(self.atributo1))
        print("Atributo 2: "+str(self.atributo2))
    
    # Métodos de Classe: são os métodos static do Java
    @classmethod
    def printa_dados_classes(classe):
        print("Numero de objetos da classe: "+str(classe.n_objetos))
    
    def get_atributo_privado(self):
        return self.__atributo_privado
    
    def print_publico(self):
        print("Chamei o método público para acessar o privado")
        self.__print_privado()
        
    def __print_privado(self):
        print("Chamei o método privado")
    
    # Aqui tem-se um método abstrato, o "pass" permite que ele seja declarado sem nada dentro, pois seu conteúdo deverá ser reescrito pelas subclasses herdeiras    
    def metodo_abstrato(self):
        pass

# HERANÇA
class SubClasse(Classe):
    def __init__(self,atributo1, atributo2, atributo3, atributo4):
        # Super permite usar diretamente o método como foi implementado na classe pai
        super().__init__(atributo1, atributo2, atributo3)
        self.atributo4 = atributo4
        
    def metodo_abstrato(self):
        print("Reescrita do método abstrato")
        
obj1 = Classe("Alal", 2, 6)
Classe.printa_dados_classes()
obj1.print_publico()

obj2 = SubClasse("Alal", 2, 6, "Aoba")
obj2.metodo_abstrato()

