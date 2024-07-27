from time import sleep


class User:
    def __init__(self,
                 nickname: str,
                 password: int,
                 age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname


class Video:
    def __init__(self,
                 title: str,
                 duration: int,
                 time_now: int = 0,
                 adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class UrTube:
    def __init__(self,
                 users: list[User] = [],
                 videos: list[Video] = [],
                 current_user: User = None):
        self.current_user = current_user
        self.videos = videos
        self.users = users

    def is_video_exists(self,
                        title: str):
        for video in self.videos:
            if video.title == title:
                return True, video
        return False, None

    def is_registered(self,
                      nickname: str):
        for user in self.users:
            if user.nickname == nickname:
                return True, user
        return False, None

    def log_in(self,
               nickname: str,
               password: str):
        registered, user = self.is_registered(nickname)
        if registered:
            self.current_user = user

    def register(self,
                 nickname: str,
                 password: str,
                 age: int):
        registered, user = self.is_registered(nickname)
        if registered:
            print(f'Пользователь "{nickname}" уже существует')
            return False
        else:
            self.users.append(User(nickname, hash(password), age))
            self.log_in(nickname, password)
            return True

    def log_out(self):
        self.current_user = None

    def add(self,
            *other: Video):
        for video in other:
            is_exist, new_video = self.is_video_exists(video.title)
            if not is_exist:
                self.videos.append(video)

    def get_videos(self,
                   video_search_bar_value: str):
        finding_videos: list[Video] = []

        for video in self.videos:
            video_title = video.title
            video_title.lower()
            if video_title.find(video_search_bar_value):
                finding_videos.append(video)

        return finding_videos

    def watch_video(self,
                    title: str):
        if self.current_user is None:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
            return

        find, video = self.is_video_exists(title)
        if find:
            if (self.current_user.age < 18
                    and video.adult_mode):
                print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
                return
            for current_time in range(video.time_now, video.duration):
                video.time_now = current_time

                print(f'{video.time_now}', end=" ")
                sleep(1)

            print(f'Конец видео')
            video.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
