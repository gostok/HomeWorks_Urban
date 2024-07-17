class User:

    def __init__(self, nickname, password, age):

        self.nickname = nickname
        self.age = age
        self.password = password


class Video:

    def __init__(self, title, duration, time_now=1, adult_mode=False):

        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self, users=None, videos=None, current_user=None):

        self.users = []
        self.videos = []
        self.current_user = None
        self.current_user1 = None

    def log_in(self, nickname, password):

        for i in self.users:
            if nickname == i.nickname and password == i.password:
                self.current_user1 = i
                self.current_user = self.current_user1.nickname

    def register(self, nickname, password, age):

        a = 0
        for i in self.users:
            if nickname != i.nickname:
                a += 1
                continue
        if a == len(self.users):
            us = User(nickname, password, age)
            self.users.append(us)
            self.current_user1 = us
            self.current_user = self.current_user1.nickname
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):

        self.current_user = None

    def add(self, *args):

        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, sear):

        search = []
        for i in self.videos:
            if sear.lower() in i.title.lower():
                search.append(i.title)
        return search

    def watch_video(self, other):

        for i in self.videos:
            if other == i.title:
                user1 = self.current_user1
                if not user1:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                elif i.adult_mode and user1.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    print(' '.join([str(j) for j in range(i.time_now, i.duration + 1)]), 'Конец видео')


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
