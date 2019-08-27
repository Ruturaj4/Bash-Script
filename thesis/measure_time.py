import os
import re
import subprocess
import json
from timeit import default_timer as timer
# from plotly import graph_objs as go
# import plotly
# plotly.offline.init_notebook_mode(connected=True)

total = 0
pwd = os.getcwd()
dic = {"000":{}, "001":{}}
ignore_files = {"basic-00089-min.c", "basic-00170-med.c", "basic-00181-min.c", "basic-00171-med.c", "basic-00159-med.c",
"basic-00161-med.c", "basic-00167-med.c", "basic-00169-med.c", "basic-00153-med.c", "basic-00160-med.c", "basic-00176-med.c",
"basic-00173-med.c", "basic-00168-med.c", "basic-00162-med.c", "basic-00165-med.c", "basic-00152-med.c", "basic-00157-med.c",
"basic-00154-med.c", "basic-00175-med.c", "basic-00155-med.c", "basic-00174-med.c", "basic-00163-med.c", "basic-00172-med.c",
"basic-00156-med.c", "basic-00158-med.c", "basic-00164-med.c", "basic-00166-med.c", "basic-00151-med.c"}

for dirpath, dirnames, filenames in os.walk(pwd):
    for file in filenames:
        if file in ignore_files:
            continue
        ext = os.path.splitext(file)[-1]
        name = os.path.splitext(file)[0]
        if os.path.splitext(file)[-1] == ".o":
            dic[dirpath.split("/")[-2]][dirpath.split("/")[-1]] = {}
            start = timer()
            returncode = subprocess.call([f"{os.path.join(dirpath, name) + '.o'}"], shell=False)
            end = timer()
            dic[dirpath.split("/")[-2]][dirpath.split("/")[-1]]["test1"] = end - start
            start = timer()
            returncode = subprocess.call(["/projects/zephyr/Ruturaj/pin-3.7-97619-g0d0c92f4f-gcc-linux/pin", "-t", "/projects/zephyr/Ruturaj/final_tool/obj-intel64/plain.so", "--", f"{os.path.join(dirpath, name) + '.o'}"], shell=False)
            end = timer()
            dic[dirpath.split("/")[-2]][dirpath.split("/")[-1]]["test2"] = end - start
            start = timer()
            returncode = subprocess.call(["/projects/zephyr/Ruturaj/pin-3.7-97619-g0d0c92f4f-gcc-linux/pin", "-t", "/projects/zephyr/Ruturaj/final_tool/obj-intel64/ajax.so", "--", f"{os.path.join(dirpath, name) + '.o'}", f"{os.path.join(dirpath, name) + '.text'}"], shell=False)
            end = timer()
            dic[dirpath.split("/")[-2]][dirpath.split("/")[-1]]["test3"] = end - start
    if total % 2 == 0:
        print(f"total: {total}")
    total += 1

test1 = [v["test1"] for k,v in dic["000"].items()]
test2 = [v["test2"] for k,v in dic["000"].items()]
test3 = [v["test3"] for k,v in dic["000"].items()]
random_x = [x for x in range(len(dic["000"]))]

fig = go.Figure()
fig.add_trace(go.Scatter(x=random_x, y=test1,
                    mode='lines',
                    name='lines'))
fig.add_trace(go.Scatter(x=random_x, y=test2,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=test3,
                    mode='markers', name='markers'))

# plotly.offline.iplot(fig)
