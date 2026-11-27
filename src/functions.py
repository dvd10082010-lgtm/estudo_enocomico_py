from genericpath import exists

from main_class import registros
def saveasdict(arr):
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

def show_dta(arr):
    print("\n===========\n")
    for i,intem in enumerate(arr,1):
        print("-------------\n")
        print(f"--- Registro {i} ---")
        for chave,valor in intem.items():
            print(f"{chave} : {valor}")
        print("\n===========")
        print()
    print("\n======================\n")

def  saveasjson(arr):
    import json 
    
    if not exists("src/file.json"):
        with open("src/file.json","w",encoding="utf-8") as fl_js:
             ent = json.dumps(arr,ensure_ascii=False,indent=4)
             fl_js.write(ent)
    else:
        with open("src/file.json","r+",encoding="utf-8") as fl_js:
            arr_js = json.load(fl_js)
            for dict in arr:
                arr_js.append(dict)
            S_js = json.dumps(arr_js,ensure_ascii=False,indent=4)
        with open("src/file.json","w",encoding="utf-8") as fl_js:
            fl_js.write(S_js)

        for dict in arr_js:
            print(f" nome : {dict["name"]} \n valor : {dict["value"] } \n tipo de movimentação: {dict["type_mov"]} \n entrada ou saida?: {dict["inadout"]} \n ==================")

def calcular_saldo(arr):
    saldo = 0
    for item in arr:
        if item["inadout"] == "1":
            saldo += item["value"]
        elif item["inadout"] == "2":
            saldo -= item["value"]
    return saldo
