import tkinter as tk
from random import randint
from random import seed
import numpy as np






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
            

            l_resultado['text'] = str_saida


        elif( len(entrada) == 4):
            print("4 bits!")
            l_saida['text'] = "4 bits detectados!"

             
            x0 = XOR( XOR( int(entrada[0]) , int(entrada[1]))  , int(entrada[3]))
            x1 = XOR( XOR( int(entrada[0]) , int(entrada[2]))  , int(entrada[3])) 
            x3 = XOR( XOR( int(entrada[1]) , int(entrada[2]))  , int(entrada[3]))
           

            entrada.insert(0, x0)
            entrada.insert(1,x1)
            entrada.insert(3, x3)

            str_saida = ""
            for i in range(len(entrada)):
                str_saida = str_saida + str(entrada[i])
            

            l_resultado['text'] = str_saida

        else:
            print("UFIDHIUSEHAD")
            l_saida['text'] = "Tamanho errado!"




    def transmite_com_erro():
        ham_correto = list(  l_resultado['text'] )

        

        posi = randint(0, len(ham_correto)-1)

        if( int(ham_correto[posi]) == 1):
            ham_correto[posi] = "0"
        else:
            ham_correto[posi] = "1"

        ham_errado =""
        for i in range( len(ham_correto) ):
            ham_errado = ham_errado + str( ham_correto[i] )

        l_resultado_erro['text'] = ham_errado

    
        
    def detecta_erro():
        
        hem_transmitido = list( l_resultado_erro['text'] )

        if( len(hem_transmitido) == 12): 
            k0 = XOR( XOR( XOR( XOR(  XOR( int(hem_transmitido[0]) , int(hem_transmitido[2])) , int(hem_transmitido[4])) ,  int(hem_transmitido[6])) , int(hem_transmitido[8])) , int(hem_transmitido[10])) 
            k1 = XOR( XOR( XOR( XOR(  XOR( int(hem_transmitido[1]) , int(hem_transmitido[2])) , int(hem_transmitido[5])) ,  int(hem_transmitido[6])) , int(hem_transmitido[9])) , int(hem_transmitido[10]))
            k3 = XOR( XOR( XOR(  XOR( int(hem_transmitido[3]) , int(hem_transmitido[4])) , int(hem_transmitido[5])) ,  int(hem_transmitido[6])) , int(hem_transmitido[11]))
            k7 = XOR( XOR( XOR(  XOR( int(hem_transmitido[7]) , int(hem_transmitido[8])) , int(hem_transmitido[9])) ,  int(hem_transmitido[10])) , int(hem_transmitido[11]))

            posicao_erro_12 = str(k7) + str(k3) + str(k1) + str(k0)  
            print(posicao_erro_12)

            posi= np.packbits( [0,0,0,0,k7,k3,k1,k0] , -1) 
        
        else:
            k2 = XOR( XOR(  XOR( int(hem_transmitido[3]) , int(hem_transmitido[4])) , int(hem_transmitido[5])) ,  int(hem_transmitido[6]))
            k1 = XOR( XOR(  XOR( int(hem_transmitido[1]) , int(hem_transmitido[2])) , int(hem_transmitido[5])) ,  int(hem_transmitido[6]))
            k0 = XOR( XOR(  XOR( int(hem_transmitido[0]) , int(hem_transmitido[2])) , int(hem_transmitido[4])) ,  int(hem_transmitido[6]))

            posicao_erro_7 = str(k2) + str(k1) + str(k0) 
            print(posicao_erro_7)

            posi= np.packbits( [0,0,0,0,0,k2,k1,k0] , -1)



        l_posicao_do_erro['text'] = str( int(posi) ) 


    def corrigir_erro():

        errada = list( l_resultado_erro['text'] )
        posicao = int( l_posicao_do_erro['text'] ) - 1

        if( errada[posicao] == '1'):
            errada[posicao] = '0'
        else:
            errada[posicao] = '1'

        errado_str=""

        for i in range( len( errada) ):
            errado_str = errado_str + str( errada[i] )
        
        l_m_corrigido['text'] = errado_str









    window = tk.Tk()

    window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12], minsize=20, weight=1)
    window.columnconfigure([0, 1, 2], minsize=20, weight=1)
    window.title("Hamming")
    window.geometry("500x500")


    i_8_bit = tk.Entry(master=window, width=60)
    i_8_bit.grid(row=1, column=1)

    b_about = tk.Button(master=window, text="Gerar Hamming",width=50, command=gera_hamming, bg="grey")
    b_about.grid(row=2,column=1)

    b_erro = tk.Button(master=window, text="Transmitir",width=50, command=transmite_com_erro, bg="red")
    b_erro.grid(row=5,column=1)


    l_saida = tk.Label(master=window, text="" )
    l_saida.grid(row=3, column=1)

    l_intrucao = tk.Label(master=window, text="Insira uma mensagem de 4 ou 8 bits!")
    l_intrucao.grid(row=0,column=1)

    l_resultado = tk.Label(master=window, text="")
    l_resultado.grid(row=4,column=1)

    l_resultado_erro = tk.Label(master=window, text="")
    l_resultado_erro.grid(row=6, column=1)

    b_posicao_erro = tk.Button(master=window, text="Verificar",width=50, command=detecta_erro, bg="green")
    b_posicao_erro.grid(row=7,column=1)
    l_posicao_do_erro = tk.Label(master=window, text= "")
    l_posicao_do_erro.grid(row=8,column=1)


    b_corigir = tk.Button(master=window, text="Corrigir", width=50, command=corrigir_erro, bg="SteelBlue1")
    b_corigir.grid(row=9,column=1)
    l_m_corrigido = tk.Label(master=window, text="")
    l_m_corrigido.grid(row=10, column=1)









    window.mainloop()