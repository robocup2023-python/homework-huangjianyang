import xml.etree.ElementTree as ET
from multiprocessing import Pool
from multiprocessing import RLock
from concurrent.futures import ThreadPoolExecutor
import os
import time
import csv
def time_it(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('用时:{}秒'.format(end-start))
    return inner
def write(path, v):
    path=path+'.csv'
    dict_v={}
    for i in v:
        if i in dict_v:
            dict_v[i]+=1
        else:
            dict_v[i]=1
    with open(path,'w') as f:
        file=csv.writer(f)
        for i in dict_v.keys():
            w=[i,dict_v[i]]
            file.writerow(w)
        f.close()
        
def read(path_name):
    v=[]
    print(path_name)
    tree = ET.parse(path_name)
    root = tree.getroot()
    for line in root.iter(tag='w'):
        v.append(line.text)
    return v
def Process(file):
    all=[]
    pool = ThreadPoolExecutor(max_workers=5)
    for i in os.listdir(file):
        path=os.path.join(file,i)
        v = pool.submit(read, path)
        v=v.result()
        all.extend(v)
    return all

@time_it
def main():
    all=[]
    lock = RLock()
    file_name=['dem','news','aca','fic']
    t=[]
    po = Pool(4)
    for i in file_name:
        file=os.path.join('day14/Texts',i)
        res = po.apply_async(Process, (file,))
        all.extend(res.get())
    po.close()
    po.join()
    write('result',all)
if __name__ == '__main__':
    main()
