from datetime import date

from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField("Название", max_length=50)
    description = models.CharField("Описание", max_length=50)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = "Проекты"


class Story(models.Model):
    preview = models.ImageField("Превью", upload_to="stories/")
    add_date = models.DateTimeField("Дата добавления", auto_now_add=True)
    start_date = models.DateTimeField("Дата старта")
    end_date = models.DateTimeField("Дата окончания")
    orderNum = models.IntegerField("Приоритет сториса")
    project = models.ForeignKey(Project, verbose_name="проект", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project} - {self.preview} - {self.orderNum}'

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = "Истории"


class StoryFile(models.Model):
    moreDetailedUrl = models.SlugField(verbose_name="Путь к файлам", max_length=160)
    moreDetailedText = models.CharField(verbose_name="Значение", max_length=250)
    contentType = models.CharField("Тип файла", max_length=50)
    content = models.TextField("Контент")
    duration = models.TimeField(verbose_name="Время показа", default=15)
    story = models.ForeignKey(Story, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField("Дата начала сториса",  auto_now_add=True)
    end_date = models.DateTimeField("Дата окончания сториса")

    def __str__(self):
        return f'{self.story} - {self.duration}'

    class Meta:
        verbose_name = 'Файл истории'
        verbose_name_plural = "Файлы истории"


class UserStoryFile(models.Model):
    storyFile = models.ForeignKey(StoryFile, on_delete=models.DO_NOTHING)
    subscriber = models.ForeignKey("Subscriber", on_delete=models.DO_NOTHING)
    is_watched = models.BooleanField(default=False)
    watch_date = models.DateTimeField("Просмотр")

    def __str__(self):
        return f'{self.subscriber} - {self.storyFile} - {self.is_watched}'

    class Meta:
        verbose_name = 'Файл истории пользователя'
        verbose_name_plural = "Файлы истории пользователя"


class Subscriber(models.Model):
    subs_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return f'{self.subs_id}'

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = "Подписчики"