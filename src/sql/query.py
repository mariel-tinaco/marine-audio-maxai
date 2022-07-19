import sys, os
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.join(os.getcwd(), '.'))

from src.sql import db

Session = sessionmaker(bind=db.engine)
session = Session()

for s in session.query(db.audioclips).all():
    print(s.audioclip_id, s.start_time)

print('*'*20)


for s in session.query(db.audioclips).filter(db.audioclips.start_time < 5):
    print(s.audioclip_id, s.start_time)

