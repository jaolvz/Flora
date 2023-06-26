import speech_recognition as sr
import requests
import re
import webbrowser as wb



def tocar_musica(nome_musica):
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
    if "tocar" in frase:
        frase = frase.replace("tocar", "")
        tocar_musica(frase)


def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa:")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print(frase)
        analise_frase(frase)
    except sr.UnknownValueError:
        print("Não entendi,João")

    return frase


ouvir_microfone()
