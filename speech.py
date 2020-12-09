import speech_recognition as sr
from googleapiclient.discovery import build
import time
import webbrowser

api_key = "API_KEY"
link = "https://www.youtube.com/watch?v="
videoId = ""
videoTitle = ""


r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    r.energy_threshold = 400
    r.dynamic_energy_threshold = False
    # print('Sing OR Tell me the title of an English song')
    print("Say Something")
    # audio = r.listen(source)
    # recon = r.recognize_google(audio)

    goliath = False
    while (goliath == False):
        audio2 = r.listen(source)
        recon2 = r.recognize_google(audio2)
        print(recon2)
        if recon2.lower() == "hey goliath":
            audio = r.listen(source)
            recon = r.recognize_google(audio)
            print(recon)
            goliath = True

# contact = recon.split(" ")
# # print(contact)
# for each in contact:
#     if each == "contact":
#         webbrowser.open("http://localhost:8000/pythonweb/contact")
#     elif each == "home":
#         webbrowser.open("http://localhost:8000")


try:
    print("Identifying the song")
    time.sleep(2)
    recon = (r.recognize_google(audio)+" song")
    youtube = build('youtube', 'v3', developerKey=api_key)
    # print(recon)
    search_response = youtube.search().list(
        q=recon,
        part='id,snippet',
        maxResults=1
    ).execute()
    videos = []

    for search_result in search_response.get('items', []):
        # print(search_result)
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (
                search_result['snippet']['title']))
            videoTitle = search_result['snippet']['title']
            videoId = link+search_result['id']['videoId']
    print('\n'.join(videos))
    # print(videoId+"\n"+videoTitle)
    print("Playing the song.....")
    time.sleep(3)
    webbrowser.open(videoId)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))
