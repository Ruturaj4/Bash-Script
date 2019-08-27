import os

pwd = os.getcwd()
for dirpath, dirnames, filenames in os.walk(pwd):
    for file in filenames:
        ext = os.path.splitext(file)[-1]
        name = os.path.splitext(file)[0]
        # if os.path.splitext(file)[-1] == ".c":
        #     os.system(f"gcc -g {os.path.join(dirpath, file)} -o {os.path.join(dirpath, name) + '.o'}")
        if os.path.splitext(file)[-1] == ".o":
            os.system(f"/projects/zephyr/Ruturaj/ghidra_github/gidhra_build/ghidra_9.0.3-DEV/support/analyzeHeadless /projects/zephyr/Ruturaj/ghidra_learning/ TEST1 -import {os.path.join(dirpath, file)} -postscript /projects/zephyr/Ruturaj/ghidra_github/gidhra_build/ghidra_9.0.3-DEV/support/test3.py -deleteproject")
