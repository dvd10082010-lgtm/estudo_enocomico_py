from main_class import registros
def saveasdict(arr = []):
    msg = "sim"
    while msg == "sim":
        regis = registros()
        regis.record()
        sort_dta = regis.__dict__
        arr.append(sort_dta)   
        print("===================\n") 
        print("deseja repetir o processo?\n")
        msg = input()
        print("(digite ""sim"" para continuar, ou qualquer tecla para sair...!)")
        print("\n===================\n: - ") 

def show_dta(arr = []):
    print("\n===========\n")
    for i,intem in enumerate(arr,1):
        print("-------------\n")
        print(f"--- Registro {i} ---")
        for chave,valor in intem.items():
            print(f"{chave} : {valor}")
        print("\n===========")
        print()
    print("\n======================\n")

def  saveasjson(arr = []):
    import json
    x = True
    with open("file.json","w", encoding="utf-8") as filejson:
        filejson.write("[\n")
        for dict in arr:
            if x == False:
                filejson.write(",\n")
            else:
                x = False
            json.dump(dict,filejson,ensure_ascii=False,indent=4)
        filejson.write("\n]")

    with open("file.json","r", encoding="utf-8") as filejson:
        dict = json.load(filejson)
        for i in dict:
            print(f" - {i}")
    print("\n")

def calcular_saldo(arr = []):
    saldo = 0
    for item in arr:
        if item['inadout'] == 1:
            saldo += item['value']
        else:
            saldo -= item['value']
    print(saldo)
