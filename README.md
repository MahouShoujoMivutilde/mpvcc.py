Этот скрипт - лишь урезанная по функционалу адаптация webm.py, добавляющая возможность использовать ffmpeg с какими угодно другими параметрами, а не ограничивающаяся лишь vp8/vp9/av1. 

Код на ~90% взят [отсюда](https://github.com/Kagami/webm.py).

```
>>> mpvcc.py -h
usage: mpvcc.py [-h] -i I

Скрипт для интерактивных кропа и обрезки видео с помощью mpv и ffmpeg.
Все аргументы, кроме -i и его значения, будyт напрямую отправлены ffmpeg.

Использование
    Кроп изображения
        выделить мышью нужную часть, нажать "a" для подтверждения.

    Обрезка видео по времени
        нажать "c" для отметки начала,
        нажать еще раз для отметки окончания нужного фрагмента.

    (Нажать q для выхода из mpv и начала кодирования с выбранными параметрами)

Примеры
    команда
        mpvcc.py -i input.mkv -c:v vp9 -crf 30 -b:v 0 -threads 16 -an output.webm

    даст на выходе из mpv, при отсутствии какого-либо с ним взаимодействия, просто
        ffmpeg -hide_banner -i input.mkv -c:v vp9 -crf 30 -b:v 0 -threads 16 -an output.webm

    но, если, скажем, выбрать кроп картинки, то будет что-то вроде
        ffmpeg -hide_banner -i input.mkv -vf crop=593:356:259:115 -c:v vp9 -crf 30 -b:v 0 -threads 16 -an output.webm

    а если выбрать обрезку длины, то получится, например
        ffmpeg -hide_banner -ss 1.018 -i input.mkv -t 5.822 -c:v vp9 -crf 30 -b:v 0 -threads 16 -an output.webm

    и, если задать всё одновременно, то будет
        ffmpeg -hide_banner -ss 5.589 -i input.mkv -t 9.676 -vf crop=847:417:199:179 -c:v vp9 -crf 30 -b:v 0 -threads 16 -an output.webm

optional arguments:
  -h, --help  show this help message and exit

required arguments:
  -i I        Путь к видео
```