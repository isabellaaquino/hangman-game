listaForcas = []
# Casos de erros:
listaForcas.append("-")
listaForcas.append("_________\n |      |\n |      O\n |        \n |      \n |       \n |")
listaForcas.append("_________\n |      |\n |      O\n |      |  \n |      \n |       \n |")
listaForcas.append("_________\n |      |\n |      O\n |    --|  \n |      \n |       \n |")
listaForcas.append("_________\n |      |\n |      O\n |    --|--\n |      \n |       \n |")
listaForcas.append("_________\n |      |\n |      O\n |    --|--\n |      |\n |       \n |")
listaForcas.append("_________\n |      |\n |      O\n |    --|--\n |      |\n |     /  \n |")
listaForcas.append("_________\n |      |\n |      O\n |    --|--\n |      |\n |     / \  \n |")
#
contErros = 0
print("-=-"*5)
print("BEM VINDO AO JOGO DA FORCA! ESCOLHA UMA PALAVRA PARA COMEÇAR: (obs: hífens não são permitidos.)")
print("-=-"*5)
palavra=input("Digite a palavra desejada:").upper()  
tam=len(palavra)
palavraOculta =['-' if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' else x for x in palavra]
print("-=-"*3)
print("JOGO INICIADO!")
print("_________\n |      |\n |      \n |        \n |      \n |       \n |")
print("PALAVRA:")
print(*palavraOculta, sep='')
testes=input("Digite uma letra.").upper()

while contErros <7:
    if contErros==6:
        print(listaForcas[7])
        print("Você cometeu erros demais, e o personagem foi enforcado!")
        break
    
    if palavra.count(testes)>0:
        vzs=palavra.count(testes)
        print("Você acertou! A letra aparece {} vez(es).".format(vzs))
        if vzs>1:
            pos=palavra.find(testes)
            palavraOculta[pos]=testes
            for c in range(vzs):
                if pos==-1:
                    break
                
                if c==0:
                    pos1=palavra.find(testes,pos+1)
                    if pos1==-1:
                        break
                    novopos=pos1
                    palavraOculta[pos1]=testes
                
                pos1=palavra.find(testes,novopos+1)
                if pos1>novopos:
                    novopos=pos1 
                elif pos1==-1:
                    break
                
                palavraOculta[pos1]=testes
                  
            print(listaForcas[contErros])
            print(*palavraOculta, sep='')
        else:
            pos=palavra.find(testes)
            palavraOculta[pos]=testes
            print(listaForcas[contErros])
            print(*palavraOculta, sep='')
        
        if palavraOculta.count('-')==0:
            print("Parabéns! Você acertou! A palavra era: {}".format(palavra))
            break
  
        testes=input("Digite uma letra.").upper()
    else:
        print("Você errou.")
        contErros+=1
        print(listaForcas[contErros])
        print(*palavraOculta, sep='')
        testes=input("Digite uma letra.").upper()