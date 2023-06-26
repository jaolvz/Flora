import speech_recognition as sr
import requests
import re
import webbrowser as wb
from gtts import gTTS
import pygame
from datetime import datetime
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



def iniciando():
    if datetime.now().hour>=6 and datetime.now().hour<12:
        falar("Bom dia")
    elif datetime.now().hour>=12 and datetime.now().hour<18:
        falar("Boa tarde")
    elif datetime.now().hour >= 18 and datetime.now().hour < 24:
        falar("Boa Noite")
    elif datetime.now().hour >= 0 and datetime.now().hour <6:
        falar("Vai dormir")


def tocar_musica(nome_musica):
    falar(f"Tocando {nome_musica} no Youtube")
    url_busca = f'https://www.youtube.com/results?search_query={nome_musica}'
    response = requests.get(url_busca)
    pattern = r'/watch\?v=([A-Za-z0-9_\-]+)'
    match = re.search(pattern, response.text)
    if match:
        video_id = match.group(1)
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        wb.open(video_url)
    else:
        print('Nenhum vídeo encontrado.')

def analise_frase(frase):
    frase= frase.lower()
    if "tocar" in frase:
        frase = frase.replace("tocar", "")
        tocar_musica(frase)

    if "que horas são" in frase:
        hora_atual = datetime.now().hour
        minuto_atual = datetime.now().minute
        falar(f"São exatamente {hora_atual} horas e {minuto_atual} minutos ")

    if "clima" in frase:
        falar("De qual cidade você deseja saber o clima ?")
        cidade = resposta_microfone()


def ouvir_microfone():
   while True:
       microfone = sr.Recognizer()
       with sr.Microphone() as source:
           microfone.adjust_for_ambient_noise(source)
           audio = microfone.listen(source)
       try:
           frase = microfone.recognize_google(audio, language='pt-BR')
           print(frase)
           if "Flora" in frase:
             frase = frase.replace("Flora", "")
             analise_frase(frase)
       except sr.UnknownValueError:
        print("Não entendi")

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

iniciando()
ouvir_microfone()
