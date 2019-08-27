import os
import re
import subprocess
import json

bad = r"/\*\s*BAD\s*\*/"
# ok = r"/\*\s*OK\s*\*/"

passed = 0
total = 0
pwd = os.getcwd()
dic = {"total":[], "passed":[]}
ignore_files = {"basic-00089-min.c", "basic-00170-med.c", "basic-00181-min.c", "basic-00171-med.c", "basic-00159-med.c",
"basic-00161-med.c", "basic-00167-med.c", "basic-00169-med.c", "basic-00153-med.c", "basic-00160-med.c", "basic-00176-med.c",
"basic-00173-med.c", "basic-00168-med.c", "basic-00162-med.c", "basic-00165-med.c", "basic-00152-med.c", "basic-00157-med.c",
"basic-00154-med.c", "basic-00175-med.c", "basic-00155-med.c", "basic-00174-med.c", "basic-00163-med.c", "basic-00172-med.c",
"basic-00156-med.c", "basic-00158-med.c", "basic-00164-med.c", "basic-00166-med.c", "basic-00151-med.c"}

for dirpath, dirnames, filenames in os.walk(pwd):
    dic["total"].append("/".join(dirpath.split("/")[-2:]))
    for file in filenames:
        if file in ignore_files:
            continue
        ext = os.path.splitext(file)[-1]
        name = os.path.splitext(file)[0]
        # if os.path.splitext(file)[-1] == ".c":
        #     os.system(f"gcc -g {os.path.join(dirpath, file)} -o {os.path.join(dirpath, name) + '.o'}")
        filetype = None
        if os.path.splitext(file)[-1] == ".c":
            with open(os.path.join(dirpath, file), "r") as f:
                matches = re.search(bad, f.read())
                if matches is not None:
                    filetype = "bad"
                else:
                    filetype = "ok"
            if filetype:
                returncode = subprocess.call(["/projects/zephyr/Ruturaj/pin-3.7-97619-g0d0c92f4f-gcc-linux/pin", "-t", "/projects/zephyr/Ruturaj/final_tool/obj-intel64/ajax.so", "--", f"{os.path.join(dirpath, name) + '.o'}", f"{os.path.join(dirpath, name) + '.text'}"], shell=False)
                if filetype == "bad" and returncode == 1:
                    dic["passed"].append("/".join(dirpath.split("/")[-2:]))
                    passed += 1
                elif filetype == "ok" and returncode == 0:
                    dic["passed"].append("/".join(dirpath.split("/")[-2:]))
                    passed += 1
    if total % 2 == 0:
        print(f"{passed}/{total}")
    total += 1
print(f"Total passed: {passed} out of {total}")

print(len(dic["total"]))
print(len(dic["passed"]))

with open("tests.json", "w") as f:
    json.dump(dic, f)
