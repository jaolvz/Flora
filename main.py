import speech_recognition as sr
import requests
import re
import scripts
import pyautogui
import webbrowser as wb
from gtts import gTTS
import pygame
from datetime import datetime
import ctypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


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
def modoIzabella():

    falar("Ativando modo Izabella")
    # Minimize todas as janelas
    pyautogui.keyDown('winleft')
    pyautogui.press('d')
    pyautogui.keyUp('winleft')
   #mudança de papel de parede
    SPI_SETDESKWALLPAPER = 0x0014
    WALLPAPER_PATH = r"C:\Users\Principal\Desktop\modoIzabella.jpg"
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 1)
   #abrindo música
    wb.open("https://www.youtube.com/watch?v=AENA_nvF-L0&ab_channel=pagodepontocom")

def modoEstudo():
   falar("Ativando modo estudo")
   scripts.bloqueando_site("twitter.com")

def desativarModoEstudo():
    falar("Desativando modo estudo")
    scripts.desbloqueando_site("twitter.com")

def volumeDesejado(volume_desejado):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_desejado, None)
    falar(f"Volume alterado para {volume_desejado*100}%");

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

    if "mudar volume" in frase:
        falar("para quantos por cento ?")
        novo_volume =  int(resposta_microfone())
        novo_volume = novo_volume/100
        volumeDesejado(novo_volume)

    if "ativar modo isabela" in frase:
        modoIzabella()

    if "ativar modo estudo" in frase:
        modoEstudo()

    if "desativar modo estudo" in frase:
        desativarModoEstudo()

    if "conte uma piada" in frase:
        falar(scripts.contar_piada())


def ouvir_microfone():
   while True:
       microfone = sr.Recognizer()
       with sr.Microphone() as source:
           microfone.adjust_for_ambient_noise(source)
           audio = microfone.listen(source)
       try:
           frase = microfone.recognize_google(audio, language='pt-BR')
           print(frase)
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


ouvir_microfone()