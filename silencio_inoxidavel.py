import sys
import os
import time
import pygame
import cv2
import pygame
import numpy as np


#Animação da escrita
def escrever(texto, velocidade=0.04):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidade)
    print()

#Trilha sonora principal
pygame.mixer.init()
pygame.mixer.music.load('trilha sonora.mp3')
pygame.mixer.music.play(-1)

#Menu do jogo
while True:
    print('''-----SILÊNCIO INOXIDÁVEL-----\n
       [1] Iniciar Jogo
       [2] Créditos
       [3] Sair\n''')
    
    escolha = int(input('Digite o número da opção desejada: \n '))
    if escolha == 1:
            print('\nIniciando o jogo...\n')
            break
    elif escolha == 2:
            print('''----Créditos----
Desenvolvedoras:
Iana Nogueira
Sara Letícia
Ana Alice
Ana Kevillin
Micaele Sousa''')
    elif escolha == 3:
            print('Saindo do jogo...Obrigado por jogar!')
            sys.exit()
            
    else:
            print('Opção inválida!\n')



#Tela final
CAMINHO_VIDEO = "Tela_final.mp4"
CAMINHO_MUSICA = "mus_final.mp3"

def combatefinal():
    pygame.display.init()
    cap = cv2.VideoCapture(CAMINHO_VIDEO)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    try:
        pygame.mixer.music.load(CAMINHO_MUSICA)
    except Exception as erro:
        print(f"Erro ao carregar a música: {erro}")
        cap.release()
        return
    
    pygame.mixer.music.stop()

    info_tela = pygame.display.Info()
    largura = info_tela.current_w
    altura = info_tela.current_h
    tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)

    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    relogio = pygame.time.Clock()
    musica_iniciada = False
    frame_atual = 0

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        ret, frame = cap.read()
        if not ret:
            rodando = False
            break

        frame_atual += 1
        segundos = frame_atual / fps

        if segundos >= 4 and not musica_iniciada:
            pygame.mixer.music.play()
            musica_iniciada = True

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (largura, altura))
        surface = pygame.surfarray.make_surface(np.transpose(frame, (1, 0, 2)))
        tela.blit(surface, (0, 0))
        pygame.display.flip()
        relogio.tick(fps)

    cap.release()
    pygame.mixer.music.stop()
    pygame.display.quit()
    sys.exit()

#Tela de morte
def tela_morte():
    pygame.init()
    largura = 1100
    altura = 620
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Game Over")
    pygame.mixer.music.stop()

    pygame.mixer.music.load("mus_morte.mp3")
    pygame.mixer.music.play(-1)  
    fundo = pygame.image.load("fundo 1.jpeg")
    fundo = pygame.transform.scale(fundo, (largura, altura))
    fonte = pygame.font.Font(None, 100)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tela.blit(fundo, (0, 0))
        texto1 = fonte.render("SISTEMA CORROMPIDO", True, (255, 0, 0))
        texto2 = fonte.render("VOCÊ MORREU", True, (255, 0, 0))
        tela.blit(texto1, texto1.get_rect(center=(largura // 2, altura // 2 - 60)))
        tela.blit(texto2, texto2.get_rect(center=(largura // 2, altura // 2 + 40)))
        pygame.display.flip()


#Final do jogo
def final():
    escrever("""
A porta blindada começa a amassar com os socos brutais do androide infectado. 
As luzes vermelhas de emergência piscam sem parar. É agora ou nunca!
O painel do robô aliado acende uma luz amarela, esperando o seu comando.
        """)
    while True:
        print("""
Escolha uma ação:
        [1] Ligar o Robô Aliado e Ativar o Sistema de Combate.
        [2] Analisar se o robô está em boas condições para combate.
            """)
        escolhafim = int(input("O que você deseja fazer? \n"))
        if escolhafim == 1:
            combatefinal()
            break
        elif escolhafim == 2:
            escrever("""
Você decide analisar se a fiação e as juntas do robô estão prontas para combate.
Porém isso demandou mais tempo do que o esperado, o robô arromba a porta e dispara em sua direção.\n""")
            tela_morte()
            sys.exit()
        else:
            print("Opção inválida! Tente novamente.\n")


#Escolhas do jogo
def escolha_2_1():
    escrever("""
Você olha a caixa de perto. O cadeado está velho e enferrujado, mas quebrá-lo vai fazer barulho.
No chão, perto do armário, você encontra a Chave da Zeladoria e resolve guardar.\n
Parabéns! Você adquiriu Chave da Zeladoria, este item pode ser importante.\n
Sabendo que o cadeado velho faria barulho, você decide não arriscar. 
Com a Chave da Zeladoria no bolso, você espia pela fresta da porta. 
O corredor parece limpo, mas um eco distante avisa que você precisa se mover rápido. 
Você sai de mansinho e corre em direção à única porta com luzes de emergência piscando no fim do corredor:
o Laboratório de Robótica.""")
    escrever(bate)
    escrever("""
Você vê um armário de ferro trancado no canto da sala. Usando a Chave da Zeladoria que você achou no chão do laboratório,
a porta se abre com facilidade! Lá dentro estão as duas peças que faltavam: os Motores de Movimento e a Câmera Sensor. 
Você corre contra o tempo e encaixa as duas no robô.
        """)
    final()

def escolha_2_2():
    escrever("""
Você força o trinco com as mãos. O cadeado quebra com um estalo alto que ecoa pelo laboratório.
Você pega a Câmera Sensor, mas o barulho chama a atenção do androide, que começa a voltar pelo corredor.\n
Parabéns! Você adquiriu Câmera Sensor, este item pode ser importante.\n
O estalo do cadeado quebrando ecoa como um tiro no silêncio do bloco. 
Você enfia a Câmera Sensor na mochila, mas os passos pesados do androide mudam de direção abruptamente no pátio.
Ele está voltando! O pânico toma conta. 
Você dispara pelo corredor enquanto ouve o metal do inimigo colidir contra as paredes logo atrás.
Você alcança a porta blindada do Laboratório de Robótica e se joga para dentro, batendo a tranca com força.\n""")
    escrever(bate)
    escrever("""
Você tira a Câmera Sensor da mochila e encaixa direto no rosto do robô. 
Depois, revirando rapidamente as gavetas de ferramentas ali perto, você dá muita sorte e encontra os Motores de Movimento.
Você prende os motores nas pernas do robô. Todas as 5 peças estão no lugar!\n""")
    final()

def escolha_2():
    escrever('''
Você se move agachado e entra sem ruídos no Laboratório de Ciências.
Ela não nota sua presença e segue em direção ao pátio. 
O perigo imediato passou.
Pela janela de vidro, você vê a silhueta escura do androide se afastar em direção ao pátio central da escola.
O laboratório está um caos: frascos de vidro quebrados cobrem o chão e as bancadas químicas estão reviradas.
No entanto, ao iluminar uma mesa nos fundos da sala com a lanterna, você vê uma Caixa de Metal trancada com um cadeado simples.
Pela fresta da caixa de metal, você observa uma Câmera Sensor.''')
    while True:
        print("""
Escolha uma opção:
        [1] Observar a caixa
        [2] Pegar a câmera sensor
        """)
        escolha_2 = int(input("O que você deseja fazer? "))
        if escolha_2 == 1:
            escolha_2_1() 
            break  
        elif escolha_2 == 2:
            escolha_2_2()
            break   
        else:
            print("Opção inválida! Tente novamente.")

def escolha_3_1():
    escrever(''' 
Você entra na sala trancando a porta atrás de você. 
Vasculhando as prateleiras rapidamente, você encontra um poster com dois androides 
programando juntos: "Israely e Eduarda". Nenhum sentimento a relatar sobre o poster.
Vamos apenas continuar. AGORA!
Após vasculhar mais um pouco, você encontra uma Pilha Reserva e um Rádio Velho.\n
Parabéns! Você adquiriu Pilha Reserva e um Rádio Velho, estes itens podem ser importantes.\n
De repente, você ouve passos pesados descendo as escadas correndo! O androide está voltando para o térreo. 
Sem pensar duas vezes, você sai da Zeladoria e corre para a única sala com porta blindada no fim do corredor: 
o Laboratório de Robótica.\n''')
    escrever(bate)
    escrever('''
Você não tem nenhuma das peças principais na mochila. Desesperado, você tenta revirar os armários do laboratório procurando algo útil, 
mas a sua demora na sala anterior custou caro. A porta blindada cede com um estrondo violento. 
O Androide infectado invade a sala antes que você possa reagir.''')
    tela_morte()
    sys.exit()

def escolha_3_2():
    escrever('''
Você usa a chave e entra na oficina. Na bancada principal, você encontra os Motores de Movimento brilhando sob a poeira. 
Você guarda a peça na mochila.\n
Parabéns! Você adquiriu Motores de Movimento, este item pode ser importante.\n
Um estrondo alto vindo do teto mostra que o androide está descendo pelos dutos de ventilação! 
Assustado, você sai correndo da oficina e se joga para dentro da única sala com porta blindada 
no fim do corredor: o Laboratório de Robótica.\n''')
    escrever(bate)
    escrever('''
Você abre a mochila, pega os Motores de Movimento e os prende rapidamente nas pernas do robô. Agora só falta a Câmera Sensor. 
Olhando para o teto da sala, você nota que as câmeras de segurança são do mesmo modelo. 
Você arranca a Câmera Sensor da parede com uma ferramenta e faz a fiação direto no rosto do robô aliado. 
Todas as 5 peças estão prontas!
Faíscas voam da fechadura enquanto a porta blindada começa a ceder. O painel do robô aliado finalmente acende, emitindo um bipe agudo. 
Na tela do computador, uma barra de progresso pisca em verde:\n [SISTEMA PRONTO PARA INICIALIZAÇÃO].\n
É o seu tudo ou nada. Resta apenas dar a ordem para trazer o seu aliado à vida.\n''')
    final()

def escolha_3():
    escrever('''
\nVocê paralisa no breu total.
Os passos param a poucos metros de você.
Sem detectar som ou movimento, a IA do androide assume
que a área está vazia e ele sobe as escadas para o segundo andar.
Você solta o ar devagar após o robô subir as escadas. O corredor do térreo está livre, mas o silêncio é assustador.\n 
Sabendo que o androide está no andar de cima, você precisa agir rápido antes que ele desça.
À sua frente, você vê duas portas: a da Zeladoria e a do Bloco Técnico.\n''')
    while True:
        print('''
Escolha uma opção:
        [1] Entrar na Zeladoria para procurar itens.
        [2] Usar a Chave de Metal para entrar no Bloco Técnico.\n''')
        escolha_3 = int(input('O que você deseja fazer agora? '))
        if escolha_3 == 1:
            escolha_3_1()
            break
        elif escolha_3 == 2:
            escolha_3_2()
            break
        else:
            print('"Opção inválida! Tente novamente."')
        
       
#textos 
bate = ("""\nBOOM! BOOM! O androide infectado bate com força contra a porta blindada, mas ela resiste.
Você está seguro... por enquanto.
No centro da sala, sobre uma mesa, está o corpo de um robô desligado. No monitor principal, uma mensagem avisa:\n
[ROBÔ ALIADO - STATUS: 3/5 PEÇAS INSTALADAS]\n
Prontos: Bateria Principal, Placa de Circuito e Chip de IA.\n
FALTANDO: Motores de Movimento e Câmera Sensor.""")
      
       
#início do jogo
while True:
    escrever('''A névoa da meia-noite cobre os portões enferrujados da antiga Escola Técnica de 
Tecnologia Avançada (ETTA). Para o resto do mundo, este lugar foi fechado às pressas 
devido a um acidente químico. Mas você sabe a verdade: os laboratórios subterrâneos 
escondiam protótipos de Inteligência Artificial Avançada, núcleos de processamento 
autônomos que nunca foram a público. Essa escola desenvolvia robótica militar e civil de 
ponta sob o disfarce de projetos estudantis.  
Movido pela curiosidade, você força a janela e entra no bloco de engenharia.  
De repente, um estrondo violento ecoa na entrada. As portas de aço da fachada se trancam 
automaticamente e as luzes do corredor principal se apagam por completo, deixando você 
na escuridão total. O androide infectado está patrulhando a área e se aproximando da sua posição...''')   
    print('''
Escolha uma opção:
        [1] Ligar a lanterna e correr em direção à Sala de Informática à esquerda. 
        [2] Agachar-se e tentar entrar silenciosamente no Laboratório de Ciências mais próximo.  
        [3] Permanecer estático na escuridão total para ouvir a rota exata do androide\n''')
    escolha = int(input('O que você deseja fazer? '))

    if escolha ==1:
        escrever('''\nO barulho dos seus passos e a luz da lanterna chamam a atenção imediata do inimigo.
O androide solta um chiado de estática e dispara em sua direção.\n''')
        tela_morte()
       
    elif escolha == 2:
        escolha_2()
        break
    elif escolha == 3:
        escolha_3()
        break
    else:
        print("Opção inválida! Tente novamente.")
pygame.mixer.music.stop()


