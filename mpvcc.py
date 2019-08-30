#!/usr/bin/python3

import os
import tempfile
import subprocess
import re
import json
import argparse
import base64
import gzip

MPV_SCRIPT = gzip.decompress(base64.b64decode(b'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'))

DESC = """
Скрипт для интерактивных кропа и обрезки видео с помощью mpv и ffmpeg.
Все аргументы, кроме -i и его значения, будyт напрямую отправлены ffmpeg.

Использование
    Кроп изображения
        выделить мышью нужную часть, нажать "a" для подтверждения.

    Обрезка видео по времени
        нажать "c" для отметки начала,
        нажать еще раз для отметки окончания нужного фрагмента.

    (Нажать "q" для выхода из mpv и начала кодирования с выбранными параметрами)

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
"""

def get_args():
    parser = argparse.ArgumentParser(description = DESC, formatter_class = argparse.RawTextHelpFormatter)
    requiredNamed = parser.add_argument_group("required arguments")
    requiredNamed.add_argument('-i', help = 'Путь к видео', required = True)
    return parser.parse_known_args()

def _timestamp(duration):
    idur = int(duration)
    ts = '{:02d}:{:02d}:{:02d}'.format(idur // 3600,
                                       idur % 3600 // 60,
                                       idur % 60)
    frac = duration % 1
    if frac >= 0.1:
        ts += str(frac)[1:3]
    return ts

def _mpv_run(args, check_code = True, catch_stdout = False):
    kwargs = {'stdout': subprocess.PIPE} if catch_stdout else {}
    try:
        p = subprocess.Popen(
            args, stderr = subprocess.PIPE,
            universal_newlines = True,
            **kwargs
        )
    except Exception as exc:
        raise Exception('failed to run mpv ({})'.format(exc))
    out, err = p.communicate()
    if check_code and p.returncode != 0:
        raise Exception('mpv exited with error')

    return {'stdout': out, 'stderr': err, 'code': p.returncode}

def _decode_lua_line(prefix, line):
    m = re.match(r'{}=(.+)'.format(prefix), line)
    if m:
        return json.loads(m.group(1))

def run_interactive_mode(options):
    luafh, luafile = tempfile.mkstemp(suffix = '.lua')
    try:
        os.write(luafh, MPV_SCRIPT)
    finally:
        os.close(luafh)

    # --osc conflicts with crop area dragging.
    # Possible to enable back with -po='--osc'
    args = ['mpv', '--msg-level', 'all=error', '--no-osc', '--script', luafile, options.i]

    # We let the user to see stderr output and catch stdout by ourself.
    out = _mpv_run(args)['stderr']
    cut = None
    crop = None
    for line in reversed(out.split('\n')):
        if not cut:
            cut = _decode_lua_line('cut', line)
            if cut:
                cut = [round(v, 3) for v in cut]
                continue
        if not crop:
            crop = _decode_lua_line('crop', line)
            if crop:
                continue

    if cut:
        print('[CUT] {} - {}'.format(
            'START' if cut[0] < 0 else _timestamp(cut[0]),
            'END' if cut[1] < 0 else _timestamp(cut[1])
        ))

        if cut[0] >= 0:
            options.ss = cut[0]
        if cut[1] >= 0:
            options.to = cut[1]

    if crop:
        print('[CROP] x={}, y={}, width={}, height={}'.format(crop[2], crop[3], crop[0], crop[1]))
        options.vfi = 'crop={}:{}:{}:{}'.format(*crop)

    return vars(options)

def encode(options, ffparams):
    args = ['ffmpeg', '-hide_banner']
    if options.get('ss') and options.get('to'):
        args += ['-ss', str(options['ss'])]
    args += ['-i', options['i']]
    if options.get('ss') and options.get('to'):
        args += ['-t', str(options['to'] - options['ss'])]
    if options.get('vfi'):
        args += ['-vf', options['vfi']]

    args += ffparams
    print(' '.join([str(i) for i in args]))
    p = subprocess.Popen(args)
    p.communicate()


if __name__ == '__main__':
    options, ffparams = get_args()

    opt = run_interactive_mode(options)
    encode(opt, ffparams)
