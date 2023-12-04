from pyautogui import *
import keyboard
import time
import pandas as pd
import pyperclip
import cv2

# FUNÇÕES DO PROGRAMA
def point_click(image,time=0,side='left',deslocx=0,deslocy=0,number=1):
    while True:
        if locateOnScreen(image,confidence=0.9) != None:
            x,y = locateCenterOnScreen(image,confidence=0.9)
            click(x=x+deslocx,y=y+deslocy,button=side,clicks=number)
            sleep(time)
            break

def check_swap_direction(value,deslocx=-50,deslocy=0):
    if float(value) < 0:
        sleep(2)    
        if locateOnScreen(r'Graphics\uncheck_inverter_dimensao.png',confidence=0.9) != None:
            x,y = locateCenterOnScreen(r'Graphics\uncheck_inverter_dimensao.png',confidence=0.9)
            click(x=x+deslocx,y=y+deslocy)
        return str(abs(float(value)))
    else:
        sleep(2)
        if locateOnScreen(r'Graphics\check_inverter_dimensao.png',confidence=0.9) != None:
            x,y = locateCenterOnScreen(r'Graphics\check_inverter_dimensao.png',confidence=0.9)
            click(x=x+deslocx,y=y+deslocy)
        return value

           


def insert_text(image,text,deslocx=0,deslocy=0,time=0.5):
    while True:
        if locateOnScreen(image) != None:
            x,y = locateCenterOnScreen(image)
            click(x=x+deslocx,y=y+deslocy)
            sleep(time)
            write(text)
            sleep(time)
            break    

def standart_procedure(main_image,input_image,check_image,value):
    point_click(main_image,side = 'right')
    point_click(r'Graphics\editar_recurso.png')

    if check_image == True:
        value = check_swap_direction(value)
    point_click(input_image,deslocx = 100,number=2)
    print(value)
    write(value)
    #insert_text(input_image,text = value,deslocx= 'inserir desloc', deslocy = 'inserir desloc')
    point_click(r'Graphics\check_menu.png')
    press('enter')
    press('enter')

def save_file(name,path):
    point_click(r'Graphics\Arquivo.png')
    point_click(r'Graphics\Salvar_como.png')
    write(name)
    point_click(r'Graphics\folder_name.png',deslocx=-50,number=1)
    press('del')
    pyperclip.copy(path)
    hotkey('ctrl','v')
    press('enter')
    point_click(r'Graphics\tipo.png',deslocx = 200)
    point_click(r'Graphics\parasolid.png')
    point_click(r'Graphics\Salvar.png')

# LEITURA DE DADOS DO EXCEL

time.sleep(2)
data = pd.read_excel('planejamento_mapa.xlsx',sheet_name= 'leitura_python')
folder = r'C:\Users\savic\OneDrive\Área de Trabalho\UFMG\Formula SAE\Aeromap\novos_setups_cad'


FRH = data['FRH']
RRH = data['RRH']
ANG_DIR = data['graus_dir']
ANG_ESQ = data['graus_esq']
VOL_POS = data['vol_pos']
setups = {}

for i in range(len(data)):
    setups[f'teste{i}'] = [FRH[i],RRH[i],ANG_DIR[i],ANG_ESQ[i]]

for i in range(len(setups)):
    print('recomeçou')
    frh = str(FRH[i])
    rrh = str(RRH[i])
    ang_dir = str(ANG_DIR[i])
    ang_esq = str(ANG_ESQ[i])
    print('dados cadastrados')
    if VOL_POS[i] < 0:
        name = name = f'setup_FRH{FRH[i]}_RRH{RRH[i]}_volpos_neg_{VOL_POS[i]}°'
    else:
        name = f'setup_FRH{FRH[i]}_RRH{RRH[i]}_volpos{VOL_POS[i]}°'
    standart_procedure(r'Graphics\FRH.png',r'Graphics\distancia.png',False,frh)
    standart_procedure(r'Graphics\RRH.png',r'Graphics\distancia.png',False,rrh)
    standart_procedure(r'Graphics\roda_direita.png',r'Graphics\angulo.png',True,ang_dir)
    standart_procedure(r'Graphics\roda_esquerda.png',r'Graphics\angulo.png',True,ang_esq)
    save_file(name,folder)
    

# ORDEM DE AFAZERES
# * CRIAR FUNÇOES:
# A. ENCONTRE E CLIQUE EM UM BOTAO V
# B. INSERIR OS VALORES EM UMA CAIXA DE TEXTO
# C. VERIFICAR O INVERTER DIREÇÃO

# 1- ENCONTRAR O BOTAO DE FRH
# 2- CLICAR NELE COM O BOTÃO DIREITO
# 3- CLICAR EM EDIITAR RECURSO
# 4- ENCONTRAR A CAIXA DE DISTÂNCIA
# 5- INSERIR NELA O VALOR DE <frh>
# 6- ENCONTRAR O <V> DE CONFIRMAR
# 7- CLICAR NELE
# 8- ENCONTRAR O PROXIMO V DE CONFIRMAR
# 9- CLICAR NELE
    
# # 10- EXATAMENTE A MESMA COISA PARA O RRH (CRIAR FUNÇÃO)
# standart_procedure('RRH.png','input_RRH.png',rrh)
# # 11- EXATAMENTE A MESMA COISA PARA O ANGULO DA RODA DIREITA (LEMBRAR DE AVALIAR DE O BOTAO DE INVERTER DIREÇÃO ESTA CLICADO PARA VALORES NEGATIVOS E LIVRE PARA VALORES POSITIVOS)
# standart_procedure('RRH.png','input_RRH.png',ang_dir)
# # 12- EXATAMENTE A MESMA COISA PARA O ANGULO DA RODA ESQUERDA
# standart_procedure('RRH.png','input_RRH.png',ang_esq)
# 13- ENCONTRAR O BOTAO DE ARQUIVO

# 14- CLICAR NELE
# 15- ENCONTRAR O BOTAO DE SALVAR COMO
# 16- CLICAR NELE 
# 17- DAR NOME AO ARQUIVO CONFORME O PADRÃO DESEJADO
# 18- MUDAR A PASTA DE DESTINO DOS ARQUIVOS DE SETUP 
# 19- ACHAR O BOTAO DE SALVAR
# 20- CLICAR NELE
# 21- FAZER TUDO DENOVO PARA OS PROXIMOS SETUPS 

    
