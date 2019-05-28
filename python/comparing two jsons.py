import gzip
import json
import shutil
#
# with gzip.open('t.json.gz',mode='rb') as myfile:
#     object=myfile.read()
#     print(object)

tf=open("today.json.gz_out").read()
yf=open("yesterday.json.gz_out").read()

today_file=json.dumps(tf,sort_keys=True)
yester_day=json.dumps(yf,sort_keys=True)
print(today_file==yester_day)