'''
Data Loading


'''


import os
from pathlib import Path
from typing import Callable, Iterable
from collections import namedtuple

SoundtrapSample = namedtuple('SoundtrapSample', ['start_time', 'end_time', 'min_frequency', 'max_frequency', 'description'])

def soundtraps_data_convention (data_iterable : Iterable) -> SoundtrapSample:
    if isinstance (data_iterable, list):
        return SoundtrapSample(
            start_time= float(data_iterable[0]),
            end_time= float(data_iterable[1]),
            min_frequency= float(data_iterable[2]),
            max_frequency= float(data_iterable[3]),
            description= data_iterable[4]
        )

def load_from_path (src: Path, data_convention : Callable):
    with open(src, 'r') as txt:
        for line in txt.readlines():

            splitted = line.split()

            if len(splitted) == 4:
                splitted.append('N/A')

            if len(splitted) > 4:
                separator = ' '
                combined = separator.join(splitted[4:])
                splitted = splitted[0:4] + [combined]

            yield data_convention(splitted)

def audioclip_data_generator (src : Path):

    sorted_filenames = sorted(os.listdir(src))

    for wav_filename, label_filename in grouped(sorted_filenames, 2):
        for sample in load_from_path (src / label_filename, soundtraps_data_convention):
            yield wav_filename, sample.start_time, sample.end_time, sample.min_frequency, sample.max_frequency, sample.description

def grouped (iterable : Iterable, n : int):
    return zip(*[iter(iterable)]*n)


if __name__ == "__main__":
    # sorted_audioclip_data = sorted(audioclip_data_generator (Path('data/usvi-whoi/reefST_4CH/d5_MAR2017/ST13_67694600_TK/')))

    # for x, y in grouped(sorted_audioclip_data, 2):
    #     ...

    # for i in audioclip_data_generator(Path('data/usvi-whoi/reefST_4CH/d5_MAR2017/ST13_67694600_TK/')):
    #     print(i)

    datapath = Path('data/usvi-whoi/reefST_4CH/d5_MAR2017/ST13_67694600_TK/')

    for audioclip_data in audioclip_data_generator (src=datapath):
        print(audioclip_data)