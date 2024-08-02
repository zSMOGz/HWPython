import pprint
import queue
from threading import Thread, Event

import requests

ACCESS_TOKEN = 'snf20WhUnN9jY1SvwQil94QRaeDIPv5CpK8K3YygTrRcqWaGSb-oqoVCXF1cl_K7'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

class GetGenre(Thread):
    def __init__(self,
                 queue,
                 stop_event):
        self.queue = queue
        self.stop_event = stop_event
        super().__init__()

    def run(self):
        while not self.stop_event.is_set():
            try:
                genre = requests.get(RANDOM_GENRE_API_URL).json()
                self.queue.put(genre)
            except IndexError as e:
                self.run()


class Genius(Thread):
    all_songs = []

    def __init__(self,
                 queue,
                 stop_event,
                 count_songs):
        self.queue = queue
        self.stop_event = stop_event
        self.count_songs = count_songs
        super().__init__()

    def run(self):
        while not self.stop_event.is_set():
            genre = self.queue.get()
            data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})

            data = data.json()
            try:
                song_id = data['response']['hits'][0]['result']['api_path']
                self.all_songs.append({'genre': genre,
                                  'song': f'{GENIUS_URL}{song_id}'})
                if self._list_is_filled():
                    self.stop_event.set()
            except IndexError as e:
                self.run()

    def _list_is_filled(self):
        return len(self.all_songs) > self.count_songs


queue = queue.Queue()
stop_event = Event()
count_songs = 10
genre_list = []
genius_list = []

for _ in range(6):
    genre_thread = GetGenre(queue,
                            stop_event)
    genre_thread.start()
    genre_list.append(genre_thread)

for _ in range(10):
    genius_thread = Genius(queue,
                           stop_event,
                           count_songs)
    genius_thread.start()
    genius_list.append(genius_thread)

for genius in genius_list:
    genius.join()
stop_event.set()
# Дождаться завершения после остановки
for g in genre_list:
    g.join()

print(queue.qsize())
pprint.pprint(Genius.all_songs)
