import pyautogui as pa
from time import sleep 
def teste():
    '''-------------------------------PAGINA_LOGIN--------------------------------'''
    # Digitar CNPJ + Senha
    with open('dados.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas[1:]:  
            cnpj, senha = linha.strip().split(',')  
            # Clique em CPNJ
            pa.tripleClick(-999, 598, duration=0.5)  
            pa.write(cnpj)    
            # Clique em Senha
            pa.click(-974, 675, duration=0.5)  
            pa.write(senha)  
            # Entrar
            pa.click(-829, 729, duration=0.5)

        '''-------------------------------INSCREVER-------------------------------------'''
            #Increver-se
        pa.click(-275, 361, duration=30)
        pa.click(-277, 427,duration=1)

            #Clique iniciar Processo de Inscrição
        pa.click(-1281, 957, duration=5) 


        '''-------------------------------iNICIO_PROPOSTA--------------------------------'''

        # Nome Da proposta
        pa.click(-1084, 332, duration=10)
        pa.write('TESTE')

        #Caixas de marcação
        pa.press('TAB')
        pa.press('SPACE')
        pa.press('TAB')
        pa.press('SPACE')

        #Cadastrar
        pa.press('TAB')
        pa.press('ENTER')
        pa.press('ENTER')

        '''-------------------------------DADOS_DO_PROJETO--------------------------------'''
            #Nome
        pa.doubleClick(-1230, 385, duration=5)
        pa.write('Teste')
            
            #Razão Social
        pa.tripleClick(-1262, 462, duration=1)
        pa.write('Teste')
            
            #Nome Fantasia
        pa.tripleClick(-514, 460, duration=1)
        pa.write('Teste')
            
            #Inscrição estadual 
        pa.doubleClick(-1054, 540, duration=1)
        pa.write('Teste')

            #Inscrição Municipal
        pa.doubleClick(-688, 537, duration=1)
        pa.write('12345678')

            #Email 1
        pa.tripleClick(-1274, 612, duration=1)
        pa.write('teste@gmail.com')

            #Email 2
        pa.tripleClick(-540, 610, duration=1)
        pa.write('teste1@gmail.com')

            #Telefone
        pa.doubleClick(-1386, 685, duration=1)
        pa.write('21111111111')

            #Celular
        pa.tripleClick(-579, 685, duration=1)
        pa.write('21111111112')

            #CEP
        pa.tripleClick(-1466, 762,duration=1)
        pa.write('22220040')

            #Endereço
        pa.tripleClick(-1081, 760 ,duration=1)
        pa.write('Rua Teste Teste')

            #Número
        pa.tripleClick(-593, 763, duration=1)
        pa.write('111')

            #Complemento
        pa.tripleClick(-233, 763, duration=1)
        pa.write('Fundos')

            #Bairro
        pa.tripleClick(-1229, 833, duration=1)
        pa.write('Teste')

            #Municipio
        pa.tripleClick(-1229, 833, duration=1)
        pa.write('Teste')

            #UF
        pa.tripleClick(-181, 834 ,duration=1)
        pa.write('RJ')

            #Gravar
        pa.click(-852, 921, duration=1)

            #OK
        pa.click(-788, 190, duration=5)

        '''-------------------------------SOCIOS--------------------------------'''
            #Sócios
        pa.click(-1531, 236, duration=5)

            #Nome Completo
        pa.click(-1365, 388, duration=1)
        pa.write('TESTE')

            #CPF
        pa.click(-927, 390, duration=1)
        pa.write('12345678900')

            #Adicionar
        pa.click(-101, y=394, duration=5)

        '''----------------------------INFO_SOCIOECONOMICA---------------------------'''
            #Informações Sócioeconomicas
        pa.click(-1393, 234, duration=5)

            #Nome Fantasia Do CNPJ
        pa.click(-1212, 411, duration=5)
        pa.write('TESTE')

            #Data
        pa.click(-1165, 482, duration=1)
        pa.write('14122003')

            #PrimeiraCaixa
        pa.click(-1621, 557, duration=1)

            #SegundaCaixa
        pa.click(-1090, 558, duration=1)

            #TerceiraCaixa
        pa.click(-560, 558, duration=1)

            #QuartaCaixa
        pa.click(-1619, 794, duration=1)

            #QuintaCaixa
        pa.click(-1086, 793, duration=1)

            #SextaCaixa
        pa.click(-562, 794, duration=1)

            #Scroll
        pa.scroll(-1000)

            #SetimaCaixa
        pa.click(-1620, 383, duration=1)
            
            #OitavaCaixa
        pa.click(-1091, 363, duration=1)
            
            #NonaCaixa
        pa.click(-560, 382, duration=1)

            #DecimaCaixa
        pa.click(-1620, 640, duration=1)

            #Decima1Caixa
        pa.click(-1092, 617, duration=1)

            #Decima2Caixa
        pa.click(-560, 642, duration=1)  

            #GRAVAR
        pa.click(-828, 881, duration=1)  


            #OK
        pa.click(-790, 189, duration=5)


        '''----------------------------DADOS_RESPONSAVEL-----------------------------'''
            #Responsavel Pela Execução
        pa.click(-1203, 236, duration=5)


            #Nome Do Responsavel
        pa.click(-1097, 433, duration=5)
        pa.write('Teste Teste Teste Teste')

            #CPF Do Responsavel
        pa.click(-1414, 511, duration=1)
        pa.write('12345678900')

            #RG Do Responsavel
        pa.click(-1010, 512, duration=1)
        pa.write('283664993')

            #Orgão Expeditor Do Responsavel
        pa.click(-301, 513, duration=1)
        pa.write('Teste')    
            

            #Email Do Responsavel
        pa.click(-1420, 587, duration=1)
        pa.write('teste@gmail.com')

            #Telefone Do Responsavel
        pa.click(-1357, 668, duration=1)
        pa.write('11111111100')

            #Celular Do Responsavel
        pa.click(-728, 658, duration=1)
        pa.write('11111111122')

            #CEP Responsavel
        pa.click(-1390, 742,duration=1)
        pa.write('22220040')

            #Endereço Responsavel
        pa.tripleClick(-950, y=740 ,duration=1)
        pa.write('Rua Teste Teste')

            #Número Responsavel
        pa.tripleClick(-609, 739, duration=1)
        pa.write('111')

            #Complemento Responsavel
        pa.tripleClick(-357, 739, duration=1)
        pa.write('Fundos')

            #Bairro Responsavel
        pa.tripleClick(-1306, 813, duration=1)
        pa.write('Teste')

            #Municipio Responsavel 
        pa.tripleClick(-719, 810, duration=1)
        pa.write('Teste')

            #UF Responsavel
        pa.tripleClick(-258, 814 ,duration=1)
        pa.write('RJ')

            #Gravar Responsavel
        pa.tripleClick(-852, 921, duration=1)

            #OK Responsavel
        pa.tripleClick(-788, 190, duration=5)


        '''-------------------------------DADOS_PROPOSTA--------------------------------'''
            #Dados da Proposta Cultural
        pa.click(-994, 234, duration=2)

            #Nome da Proposta
        pa.tripleClick(-1096, 374, duration=5)
        pa.write('Teste')

            #Caixona1
        pa.tripleClick(-1299, 465, duration=1)
        pa.write('Teste')

            #Caixona2
        pa.tripleClick(-865, 667, duration=1)
        pa.write('Teste')

            #Caixona3
        pa.tripleClick(-1218, 810, duration=1)
        pa.write('Teste')

            #Caixona4
        pa.tripleClick(-1347, 960, duration=1)
        pa.write('Teste')

            #Caixona5
        pa.press('TAB')
        pa.write('Teste')

            #Gravar
        pa.click(-853, 886, duration=1)

            #OK
        pa.click(-785, 186, duration=30)


        '''-------------------------------EQUIPE--------------------------------'''
            #Equipe
        pa.click(-884, 235, duration=10)

            #Nome do Membro
        pa.doubleClick(-1270, 382, duration=10)
        pa.write('Teste')

            #CPF Do Membro
        pa.click(-712, 385, duration=1)
        pa.write('12345678900')

            #Função Do Membro
        pa.click(-163, 385, duration=1)
        pa.write('Testador')

            #Curriculo Do Membro
        pa.click(-1269, 499, duration=1)
        pa.write('TesteTesteTesteTesteTeste')

            #Adicionar
        pa.click(-851, 689, duration=1)

            #OK
        pa.click(-786, 184, duration=8)


        '''-------------------------------ANEXOS--------------------------------'''
        #Anexo
        pa.click(-818, 238, duration=5)

            #Tipo de Documento1
        pa.click(-1409, 390, duration=5)

            #Documento1
        pa.click(-1371, 453, duration=5)

            #Escolher doc1
        pa.click(-923, y=391, duration=5)

            #Arquivo1
        pa.doubleClick(-1651, 143, duration=5)


            #Calendario1
        pa.click(-235, 393, duration=3)

            #Data1
        pa.click(-294, 571, duration=3)

            #Anexar1
        pa.click(-156, 394, duration=1)



        #Tipo de Documento2
        pa.click(-1409, 390, duration=10)

            #Documento2
        pa.click(-1348, 487, duration=5)

            #Escolher doc2
        pa.click(-885, 391, duration=5)

            #Arquivo2
        pa.doubleClick(-1651, 143, duration=5)

            #Calendario2
        pa.click(-235, 393, duration=3)

            #Data2
        pa.click(-294, 571, duration=2)

            #Anexar2
        pa.click(-156, 394, duration=3)

        #Tipo de Documento3
        pa.click(-1409, 390, duration=10)

            #Documento3
        pa.click(-1242, 521, duration=5)

            #Escolher doc3
        pa.click(-885, 391, duration=5)

            #Arquivo3
        pa.doubleClick(-1651, 143, duration=5)


            #Calendario3
        pa.click(-235, 393, duration=3)

            #Data3
        pa.click(-294, 571, duration=3)

            #Anexar3
        pa.click(-156, 394, duration=2)


        '''-------------------------------REVISAR--------------------------------'''
            #Revisar e enviar
        pa.click(-733, 237, duration=10)

            #Revisar e enviar
        pa.click(-833, 415, duration=5)

            #Fechar
        pa.click(-703, 368, duration=10)

            #Clique direcional 
        pa.click(-373, 253, duration=5)
        pa.press('ESC')
        pa.press('ESC')

            #Clique Direcional
        pa.click(-436, 243, duration=3)

            #Scroll
        pa.scroll(-3000)

            #Enviar
        pa.click(-877, 874, duration=5)

            #OK
        pa.click(-889, 190, duration=5)

        pa.PAUSE=5
            #OK
        pa.press('ENTER')
        pa.press('ENTER')

        #Sair
        pa.click(-76, 149, duration=30)
        pa.click(-144, 245, duration=5)
total_linhas = 85

        # Itera sobre o número total de linhas
for _ in range(total_linhas):
    teste()        
