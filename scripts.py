import random
import os
import webbrowser as wb
from gtts import gTTS
import pygame
import speech_recognition as sr

def desbloqueando_site(site_to_unblock):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    with open(hosts_path, "r") as file:
        hosts_content = file.readlines()
    new_content = [line for line in hosts_content if site_to_unblock not in line]
    with open(hosts_path, "w") as file:
        file.writelines(new_content)
    print("O site foi desbloqueado com sucesso.")
    os.system("ipconfig /flushdns")

def bloqueando_site(site):
    # Caminho do arquivo hosts (no Windows)
    caminho_hosts = r"C:\Windows\System32\drivers\etc\hosts"
    # Verifica se o site já está bloqueado no arquivo hosts
    with open(caminho_hosts, "r") as file:
        hosts_conteudo = file.read()
    if caminho_hosts in hosts_conteudo:
        pass
    else:
        # Adiciona o site ao arquivo hosts para bloqueá-lo
        with open(caminho_hosts, "a") as file:
            file.write("\n127.0.0.1 " + site)
    # Limpa o cache DNS para que as alterações entrem em vigor
    os.system("ipconfig /flushdns")

def abrir(app):
    if "twitter" in app:
        wb.open("https://www.twitter.com")
    if "youtube" in app:
        wb.open("https://www.youtube.com")
    if "thm" in app:
        wb.open("https://sm4rty.medium.com/free-350-tryhackme-rooms-f3b7b2954b8d")
    if "google" in app:
        wb.open("https://www.google.com")
    if "chat gpt" in app:
        wb.open("https://chat.openai.com/")
    if "lol" in app:
        os.startfile("C:\Riot Games\League of Legends\LeagueClient.exe")
    if "virtualbox" in app:
        os.startfile("C:\Program Files\Oracle\VirtualBox\VirtualBox.exe")

def contar_piada():
    piadas = [
        "Por que o livro de matemática se apaixonou pelo livro de história? Porque viu que juntos formavam uma bela história de amor!",
        "Por que o pássaro não usa Facebook? Porque ele já tem o Twitter!",
        "Qual é o cúmulo do surrealismo? Encontrar um canguru com uma mochila nas costas pedindo informações sobre o metrô!",
        "O que o pato disse para a pata? Fica 'quack'!",
        "Por que a matemática é o bicho-papão dos números? Porque ela tem muitos problemas!",
        "O que um peixe falou para o outro peixe? Nada, porque peixe não fala!",
        "Por que o pombo não usa chapéu? Porque ele já tem topete!",
        "O que um barco falou para o outro? Estou de 'naval'!",
        "Qual é o rei dos queijos? O reiqueijão!",
        "O que a banana suicida falou? Macacos me mordam!",
        "Qual é o carro preferido do Darth Vader? O Volkswagen 'Dark Side'!",
        "Por que o livro de receitas foi preso? Porque ele matou a fome de leitura!",
        "O que o zero disse para o oito? Gostei do seu cinto!",
        "Por que o jacaré tirou o jacarezinho da escola? Porque ele 'reptil' de ano!",
        "O que é um pontinho amarelo no céu? Um yellowcóptero!",
        "O que é, o que é? É verde, está no céu e dá voltas e voltas? Uma ervilha em uma roleta!",
        "Por que o elefante não usa computador? Porque ele tem medo do mouse!",
        "O que o advogado do frango foi fazer na delegacia? Foi soltar a franga!",
        "O que é um pontinho vermelho no meio do mar? Um 'polvo' vermelho!",
        "O que é um pontinho amarelo nadando no mar? Um peixe chinês!",
        "Por que o abajur se matriculou na academia? Porque queria ficar 'luminado'!",
        "O que o cavalo foi fazer na farmácia? Comprar xarope de potro!",
        "Por que o pepino foi ao psicólogo? Porque ele se achava um legume 'em conserva'!",
        "Qual é o cumulo do absurdo? Encontrar um palhaço no baralho!",
        "Por que o galo não bota ovos? Porque ele já tem 'desova'!",
        "O que é um pontinho azul no meio do oceano? Um peixinho fazendo tricô!",
        "O que é um pontinho vermelho no canto do quarto? Uma cereja de castigo!",
        "Por que a loja de calçados faliu? Porque deu um passo maior que a perna!",
        "Por que a girafa tem um pescoço tão longo? Porque sua mãe mandava ela comer verduras!",
        "O que o cavalo foi fazer na manicure? Foi trocar de ferradura!",
        "Por que o jacaré não gosta de apostar corrida? Porque ele sempre 'largarto'!",
        "O que um 'doido' falou para o outro? Nada, porque 'doido' não fala!",
        "Por que o livro de biologia é tão forte? Porque ele tem capa de 'músculo'!",
        "O que um prédio falou para o outro? Que elevador legal!",
        "Por que a velhinha não usa relógio? Porque ela é sem hora!",
        "Qual é o lugar mais alto da biblioteca? O topo das estantes!",
        "O que o canibal vegetariano come? A planta do pé!",
        "O que o pintinho falou para a pintinha? Você pintou o cabelo?",
        "Por que a água foi presa? Porque matou a sede!",
        "O que é um pontinho vermelho na pia? Uma goiaba espremida!",
        "O que é um pontinho azul nadando no mar? Um peixinho com frio!",
        "O que a minhoca falou para o minhoco? Nada, porque minhoca não fala!",
        "Por que a coruja não usa óculos? Porque ela já tem 'corujal'!",
        "O que o vidro disse para o espelho? Estou me vendo em você!",
        "Por que o carro se suicidou? Porque ele perdeu o 'estacionamento'!",
        "O que o elevador falou para o prédio? Estou descendo para dar uma volta!",
        "O que é um pontinho vermelho no alto da escada? Uma cereja no degrau!",
        "Por que o livro foi na igreja? Porque ele era um livro 'sagrado'!",
        "O que a pedra falou para a outra pedra? Nada, porque pedra não fala!",
        "Qual é o animal mais antigo do mundo? O zebroide, porque está sempre a 'zebrar'!",
        "Por que a bicicleta não consegue parar em pé? Porque ela é 'ciclista'!",
        "O que o raio disse para a tempestade? Vamos parar de trovejar!",
        "O que a galinha foi fazer no cinema? Assistir a 'coxinha'!",
        "Qual é o cúmulo do vegetarianismo? Comer repolho e depois soltar um 'cheiro verde'!",
        "Por que a formiga foi ao médico? Porque estava se sentindo 'inseticida'!",
        "O que um semáforo disse para o outro? Não olhe agora, mas estou mudando de sinal!",
        "O que um espelho disse para o outro espelho? Vamos nos encontrar mais tarde, estou refletindo sobre isso!",
        "Por que o gato mia para a lua? Porque ela é o seu 'mi-au'!",
        "Qual é o contrário de chocolate quente? Suco de pó!",
        "O que é um pontinho vermelho em cima da geladeira? Um morango alpinista!",
        "O que é um pontinho preto voando no céu? Uma 'meia' de pássaro!",
        "Por que a minhoca não briga? Porque ela é 'boa de paz'!",
        "O que o lápis disse para o papel? Desse jeito você me risca!",
        "Qual é o dia da semana favorito das galinhas? A 'se-xta'!",
        "Por que a matemática é tão complexa? Porque tem muitos problemas!",
        "O que um canibal vegetariano come? Palmas!",
        "Por que o computador foi ao médico? Porque estava com vírus de 'resfriador'!",
        "Qual é o cúmulo do absurdo? Encontrar uma agulha no palheiro e achar graça!",
        "O que o sinal disse para o carro? Não me olhe, estou mudando!",
        "Por que a aranha é a melhor aluna da escola? Porque ela é 'ponta nas teias'!",
        "O que um livro de matemática foi fazer na praia? Foi tentar resolver problemas 'areais'!",
        "Qual é o cúmulo da distração? Procurar o celular com o celular na mão!",
        "Por que o bombeiro não usa perfume? Porque ele prefere água de colônia!",
        "O que o tomate foi fazer no banco? Foi tirar extrato 'bancário'!",
        "Qual é o cúmulo da rapidez? Fechar a geladeira com a luz apagada!",
        "O que a abelha foi fazer no banco? Foi depositar o mel!",
        "Por que o pato se recusou a emprestar dinheiro? Porque ele era um 'pato avarento'!",
        "Qual é o cúmulo do desespero? Procurar agulha no palheiro com luvas de boxe!",
        "O que um sinal de trânsito disse para o outro? Não olhe agora, mas estou mudando de cor!",
        "Por que o jacaré tomou um susto? Porque viu o preço da bolsa da sua mulher!",
        "O que o chão falou para a poça d'água? Seja mais rasa!",
        "Qual é o cúmulo da economia? Usar um abajur de vela!",
        "Por que a loja de roupas faliu? Porque foi por água abaixo!",
        "O que o café foi fazer na igreja? Tomar um 'espresso'!",
        "Qual é o cúmulo da vaidade para um astronauta? Ter um espelho no capacete!",
        "O que um semáforo disse para o outro? Não olhe agora, mas estou mudando de cor!",
        "Por que o livro foi ao médico? Porque estava cheio de histórias malucas!",
        "O que uma laranja disse para a outra? Somos da mesma 'casca'!",
        "Qual é o cúmulo da lerdeza? Pintar uma casa de tinta fresca e ficar esperando secar!",
        "O que o espelho falou para o computador? Cuidado, você tem vírus!",
        "Por que o pato tomou um susto? Porque viu a nota do veterinário!",
        "O que o livro de receitas falou para o livro de história? Vamos temperar essa história com muita emoção!",
    ]
    piada = random.choice(piadas)
    return piada


# FUNÇÕES DE RESPOSTA E INTERAÇÃO COM A ASSISTENTE

def resposta_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source)
    try:
        resposta = microfone.recognize_google(audio, language='pt-BR')
        return resposta
    except sr.UnknownValueError:
        print("Não entendi")


def falar(texto):
    tts = gTTS(text=texto, lang='pt')
    arquivo_saida = "saida.mp3"
    tts.save(arquivo_saida)
    pygame.init()
    caminho_arquivo = r"C:\Users\Principal\PycharmProjects\Flora\saida.mp3"
    pygame.mixer.music.load(caminho_arquivo)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.quit()







