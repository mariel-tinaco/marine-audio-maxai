'''
Audio Processing Suite


'''

import os
from pathlib import Path
from typing import Callable

import sox

from utils import grouped
from loading import load_from_path
from soundtrap import soundtraps_data_convention

def trim (src : Path, dest : Path, start : float, end : float):

    tfm = sox.Transformer()
    tfm.trim(start_time=start, end_time=end)
    tfm.build(str(src), str(dest))

def main (src : Path, traverser : Callable):
    dot_to_underscore = lambda x : str(x).replace('.', '_')

    for wav, label in traverser(sorted(os.listdir(src)), 2):
        audio_path = src / wav
        label_path = src / label

        # Create directory
        os.mkdir(f'data/trimmed/{dot_to_underscore(audio_path.stem)}')

        for audio_data in load_from_path(label_path, data_convention=soundtraps_data_convention):
            dest = f'data/trimmed/{dot_to_underscore(audio_path.stem)}/{dot_to_underscore(audio_data.start_time)}-{dot_to_underscore(audio_data.end_time)}.wav'
            trim(audio_path, dest, audio_data.start_time, audio_data.end_time)

if __name__ == "__main__" :

    datapath = Path('data/usvi-whoi/reefST_4CH/d5_MAR2017/ST13_67694600_TK/')
    audio = '67694600.170609000502'

    # for audio_data in load_from_path(datapath / f'{audio}_labels.txt', data_convention=soundtraps_data_convention):
    #     print(audio_data.start_time, audio_data.end_time)
    #     # trim(datapath / f'{audio}.wav', start, end)


    main (datapath, grouped)
