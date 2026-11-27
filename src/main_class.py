class registros:

    def __init__(self):
        self.name = " "
        self.value  = None
        self.type_mov = None
        self.inadout = None

    def insert_name(self):
        self.name = input("\ninsira o seu nome:\n- ")
        
        while True:
            if self.name.replace(" ", "").isalpha():
                return self.name
            else:
                print("\nvalor de entrada não aceito, sem números:")
                self.name = input("\ninsira o seu nome:\n- ")
    
    def insert_value(self):
        while True:  
                print("===========================")
                self.value = float(input("insira  o valor:\n"))
                print("===========================")
                if isinstance(self.value, float):
                    return self.value
                else:
                    print("valor não é um numero")

    
    def insert_typemv(self):
        types_trust = ["PIX","boleto","crédito","TED","débito"]
        while True:
            print("===========================")
            print("tipos de movimentação aceitos:\n")
            for types in types_trust:
                print(f"- {types}")
            print("===========================")        
            self.type_mov = input("\ninsira o tipo de transação:\n").strip()
            print("===========================")
            if self.type_mov  in types_trust:
                return self.type_mov
            else:
                print("erros!!, insira apenas o valores determinados")

    def insert_inadouts(self):
        while True:
            opcao = input("\no valor será uma entrada(digite 1) ou uma saída(digite 2) ?\n")
            match opcao:
                case "1":
                    self.inadout = "entrada" 
                    return self.inadout
                case "2":
                    self.inadout = "saída"
                    return self.inadout
                case _:
                    print("insira apenas 1 ou 2")
            
    def record(self):
        self.insert_name()
        self.insert_typemv()
        self.insert_inadouts()
        self.insert_value()
        return self.__dict__.copy()