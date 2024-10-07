import json
import sys
import hashlib
import os
from pathlib import Path


def look_for_dye():
    dye1 = b'\xb0\x08\x91\xfb' #b00891fb
    dye2 = b'\xfb\x91\x08\b0' #b00891fb
    p = Path(r"J:\AOC\_extracted_1_3")
    res = {}
    i=0
    exts = [".png",".dds",".g1t",".xml",".txt",".json",".dae",".fbx"]
    for file in p.rglob("*"):
        i+=1
        if i > 0 and i%10000==0:
            print(i)
        isskip = False
        for ext in exts:
            if file.name.lower().endswith(ext):
                isskip = True
                break
        if not file.is_file() or isskip:
            continue
        data = file.read_bytes()
        if dye1 in data or dye2 in data:
            print(str(file))
    

def map_dds_to_md5():
    #1DDF4002DCAB1C181A8F1B67AA209679
    p = Path(r"J:\AOC\_extracted_1_3\MaterialEditor\g1t")
    files = p.rglob("*.dds")
    res = {}
    i=0
    for file in files:
        x = str(Path(file).parent.stem.replace("_files", ""))
        if x in res:
            continue
        i+=1
        if i > 0 and i%1000==0:
            print(i)
        if i%10000==0:
            with open(r"J:\AOC\_extracted_1_3\MaterialEditor\g1t_dds_hashes.json", "w") as f:
                f.write(json.dumps(res, indent=4, sort_keys=True))
        with open(file, "rb") as f:
            HASH = hashlib.md5(f.read()).hexdigest().upper()
        res[x] = HASH
    
    with open(r"J:\AOC\_extracted_1_3\MaterialEditor\g1t_dds_hashes.json", "w") as f:
        f.write(json.dumps(res, indent=4, sort_keys=True))
    


def main():
    p = r"E:\Downloads\AoC Model Analysis - Batch Import.csv"
    with open(p, "r") as f:
        data = f.readlines()[1:]
    p1 = "G1M_to_G1T_pairs.json"
    p2 = "G1M_to_G1T_pairs1.json"
    with open(p1, "r") as f:
        res = json.load(f)

        
    for line in data:
        x = [e for e in line.split(",") if e]
        if len(x) < 2 or len(x[0]) != 8:
            continue
        if x[0] not in res:
            res[x[0]] = {}
        res[x[0]]["name"] = x[1]
    
    with open(p2, "w") as f:
        f.write(json.dumps(res, indent=4, sort_keys=True))
#look_for_dye()

p = "G1M_to_G1T_pairs.json"
with open(p, "r") as f:
    lines = f.readlines()

data = [e for e in lines if not (e.startswith("<<") or e.startswith(">>") or e.startswith("=="))]
with open("G1M_to_G1T_pairs1.json", "w") as f:
    for line in data:
        if "name" in line:
            line = line.replace("\n","") + ",\n"
        f.write(line)
        