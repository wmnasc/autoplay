### SCRIPT ###
import random
import base64
ciclo = 0 

### IMPORT PASSWORD ###
with open ('pass.txt','r') as f:
    metamask = f.read()
    pw = base64.b64decode(metamask).decode('utf-8')

def forceReload():
    keyDown(Key.CTRL + Key.F5)

def rload1():
    sleep(5)
    click(Location(85, 59)) #Tela 1
    sleep(10)
    click(Location(457, 451)) #Connect Tela 1
    
def rload2():
    sleep(5)
    click(Location(87, 576)) #Tela 2
    sleep(10)
    click(Location(460, 969)) #Connect Tela2

def rload3():
    sleep(5)
    click(Location(1060, 60)) #Tela 1
    sleep(10)
    click(Location(1440, 430)) #Connect Tela 1

def connect():
    sleep(10)
    if exists ("1638061307171.png"):
        type(pw)
        click("1638061307171.png")
        while not exists("1635776519047.png"):
            sleep(5)
        click("1635776519047.png")
    else:     
        click("1635776519047.png")

def loadhero():
    global ciclo
    load = 0    
    while not exists("1641422420564.png"):
        sleep(5)
        load += 1
        if load > 22:
            load = 0
            sleep(random.randrange(1,420))
            if ciclo == 1:
                rload1()
            elif ciclo == 2:
                rload2()
            elif ciclo == 3:
                rload3()
            connect()
    click("1641422420564.png")
    sleep(8)
    if exists ("1641422541417.png", 2):
        click("1641422541417.png")
    sleep(5)
    click("1641422576755.png")
    sleep(3)
    click("1641422610010.png") #Comeca o jogo
    ciclo += 1

def padrao():
    connect()
    loadhero()

def game1():
    rload1()
    padrao()

def game2():
    rload2()
    padrao()

def game3():
    rload3()
    padrao()
    
while True:
    try:
        global ciclo
        ciclo = 1
        game1()
        game2()
        game3()
        sleep(random.randrange(5400,7200)) #Espera entre 1:30 e 2 horas para iniciar um novo jogo.
    except FindFailed:
        sleep(random.randrange(1,600)) #Caso nao encontre os botoes, espera ate 10 min para uma proxima tentativa
        forceReload()
