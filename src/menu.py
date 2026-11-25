from functions import saveasdict,show_dta,saveasjson,calcular_saldo

def menu():
    lsrecord = []  
    while True:
        print("===========================")
        print("1.registrar movimentação\n2.salvar dados\n3.ver histórico\n4.calcular saldo\n5.sair")
        print("===========================")
        in_put = int(input("---------\n- "))
        print("\n-----------------")
        match in_put:
            case 1:
                saveasdict(lsrecord)
            case 2:
                saveasjson(lsrecord)# fazer função que cria um json
            case 3:
                show_dta(lsrecord)
            case 4:
                print(calcular_saldo(lsrecord)) # fazer função que soma e retorna o quanto se tem na conta (seja divida ou saldo)
            case 5:
                break
            case _ :
                print("valor fora do padrão estabelcido(apenas de 1 á cinco)") 

menu()