import tkinter as tk







def start():

    def XOR(v1,v2):
        if((v1 == 0 and v2 == 0) or (v1 == 1 and v2 == 1)):
            return 0
        else:
            return 1



    def gera_hamming():

        entrada_direta = i_8_bit.get()
        entrada = list(entrada_direta)


        if( len(entrada) == 8):
            print("8 bits!")
            l_saida['text'] = "8 bits detectados!"
            
            x0 = XOR( XOR( XOR( XOR( int(entrada[0]) , int(entrada[1]))  , int(entrada[3])) , int(entrada[5])) , int(entrada[7]))
            x1 = XOR( XOR( XOR( XOR( int(entrada[0]) , int(entrada[2]))  , int(entrada[3])) , int(entrada[6])) , int(entrada[7]))
            x3 = XOR( XOR( XOR( int(entrada[1]) , int(entrada[2]))  , int(entrada[3])) , int(entrada[7]))
            x7= XOR( XOR( XOR( int(entrada[4]) , int(entrada[5]))  , int(entrada[6])) , int(entrada[7]))

            entrada.insert(0, x0)
            entrada.insert(1,x1)
            entrada.insert(3, x3)
            entrada.insert(7,x7)

            str_saida = ""
            for i in range(len(entrada)):
                str_saida = str_saida + str(entrada[i])

            l_resultado['text'] = "Hamming realizado! " + str_saida


        elif( len(entrada) == 4):
            print("4 bits!")
            l_saida['text'] = "4 bits detectados!"
        
        else:
            print("UFIDHIUSEHAD")
            l_saida['text'] = "Tamanho errado!"
















    window = tk.Tk()

    window.rowconfigure([0,1,2,3,4,5,6,7,8], minsize=20, weight=1)
    window.columnconfigure([0, 1, 2], minsize=20, weight=1)
    window.title("Hamming")
    window.geometry("500x500")


    i_8_bit = tk.Entry(master=window, width=60)
    i_8_bit.grid(row=1, column=1)

    b_about = tk.Button(master=window, text="Gerar Hamming",width=50, command=gera_hamming, bg="grey")
    b_about.grid(row=2,column=1)



    l_saida = tk.Label(master=window, text="" )
    l_saida.grid(row=3, column=1)

    l_intrucao = tk.Label(master=window, text="Insira uma mensagem de 4 ou 8 bits!")
    l_intrucao.grid(row=0,column=1)

    l_resultado = tk.Label(master=window, text="")
    l_resultado.grid(row=4,column=1)



    window.mainloop()