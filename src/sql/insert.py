

import sys, os
import random

from pathlib import Path
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.join(os.getcwd(), '.'))

from src.sql import db

from src.loading import audioclip_data_generator

Session = sessionmaker(bind=db.engine)
session = Session()

datapath = Path('data/usvi-whoi/reefST_4CH/d5_MAR2017/ST13_67694600_TK/')

for i, audioclip_data in enumerate(audioclip_data_generator (src=datapath)):
    filename, startT, endT, minF, maxF, desc = audioclip_data

    ac = db.audioclips(
        audioclip_id = i,
        filename = filename,
        isLabeled = True,
        start_time = startT,
        end_time = endT,
        min_frequency = minF,
        max_frequency = maxF,
        description = desc
    )
    session.add(ac)

session.commit()
