### EDIT ###
qtt_character = 15 #Colocar quantidade de heroes

### SCRIPT ###
import random
import base64

### IMPORT PASSWORD ###
with open ('pass.txt','r') as f:
    metamask = f.read()
    pw = base64.b64decode(metamask).decode('utf-8')

def connect():
    sleep(5)
    click(Location(86, 51)) #local exato do botão reload do Google chrome
    sleep(10)
    click("1639624000323.png")
    sleep(10)
    if exists ("1638061307171.png"):
        type(pw)
        click("1638061307171.png")
        sleep(10)
        click("1639624000323.png")
        sleep(5)
        click("1635776519047.png")
    else:     
        click("1635776519047.png")

def next_game():
    xtimes = 3
    for y in range(xtimes):
        sleep(random.randrange(720,900))	    
        if exists ("1637065273377.png", 2):
	        click("1637065273377.png")
    sleep(random.randrange(7200,10800)) #Espera entre 2 e 3 horas para iniciar um novo jogo.
    
while True:
    try:
        connect()
        load = 0
        while not exists("1635776574163.png"):
            sleep(5)
            load += 1
            if load > 22:
                load = 0
                sleep(random.randrange(1,420))
                connect()
        click("1635776574163.png") #clica no robo para abrir conf de herois
        sleep(2)
        click("1635776846916.png") #Clica em rest para selecionar campo de herois
        sleep(1)
        wheel(WHEEL_DOWN, 40) #rola a pagina para baixo
        sleep(2)
        qtt_character += 1
        for x in range(qtt_character):
            click(Location(891, 762)) #local exato do botão WORK do último heroi
            sleep(4)
        click("1635777357010.png") #Fecha a tela de configuracao
        sleep(3)
        click("1635777381308.png") #Comeca o jogo
        next_game()
    except FindFailed:
        #popError("Did not work, try to restart")
        sleep(random.randrange(1,600)) #Caso nao encontre os botoes, espera ate 10 min para uma proxima tentativa
