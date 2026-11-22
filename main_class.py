class registros:

    def __init__(self):
        self.name = " "
        self.value  = None
        self.type_mov = None
        self.inadout = None

    def insert_name(self):
        self.name = input("\ninsira o seu nome\n")
        
        while True:
            if self.name.replace(" ", "").isalpha():
                return self.name
            else:
                print("\nvalor de entrada não aceito, sem números:")
                self.name = input("\ninsira o seu nome")
    
    def insert_value(self):
        x = 1
        while x != 0:
            print("===========================")
            self.value = float(input("insira  o valor:\n"))
            print("===========================")
            if type(self.value) == "float":
                x = 0
                return self.value
            else:
                return ValueError("valor não é um float")
    
    def insert_typemv(self):
        types_trust = ["PIX","boleto","crédito","TED","débito"]
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
            raise ValueError("\nerro!!, insira apenas o valores determinados")

    def insert_inadouts(self):
        self.inadout = input("\no valor será uma entrada(digite 1) ou uma saída(digite 2) ?\n")
        match self.inadout:
            case "entrada":
                return 1
            case "saida" :
                return 2
            case _:
                return ValueError("insira apenas ""entradas"" ou saídas")
    
    def record(self):
        self.insert_name()
        self.insert_typemv()
        self.insert_inadouts()
        self.insert_value()
        return registros.__dict__