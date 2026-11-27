from functions import saveasdict,show_dta,saveasjson,calcular_saldo
import time

def menu():
    
    lsrecord = []  
    arr_vali = (1,2,3,4,5)
    while True:
        print("===========================")
        print("1.registrar movimentação\n2.salvar dados\n3.ver histórico\n4.calcular saldo\n5.sair")
        print("===========================")
        in_put = int(input("---------\n- "))
        print("\n-----------------")
        if in_put not in arr_vali:
            print("valor fora do padrão estabelcido(apenas de 1 á cinco)") 
            continue
        match in_put:
            case 1:
                cont = 0
                saveasdict(lsrecord)
            case 2:
                cont +=1
                if cont == 1:
                    print("salvando dados...")
                    time.sleep(1)
                    saveasjson(lsrecord)
                    cont += 1 
                elif cont >1:
                    print("dados salvos com sucesso!")  
            case 3:
                show_dta(lsrecord)
            case 4:
                print(calcular_saldo(lsrecord)) # fazer função que soma e retorna o quanto se tem na conta (seja divida ou saldo)
            case 5:
                break
menu()