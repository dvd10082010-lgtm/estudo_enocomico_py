from src.main_class import registros
def saveasdict(arr):
    msg = "sim"
    while msg == "sim":
        regis = registros()
        regis.record()
        sort_dta = regis.__dict__
        arr.append(sort_dta)   
        print("===================\n") 
        msg = input("deseja repetir o processo\n")
        print("\n===================\n") 

def show_dta(arr):
    for i,intem in enumerate(arr,1):
        print(f"--- Registro {i} ---")
        for chave,valor in intem.items():
            print(f"{chave} : {valor}")
        print("-------------")
        print()