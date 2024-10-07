## 1. Prerequisities

- install Blender 2.93
- install [blender DDS importer](https://github.com/matyalatte/Blender-DDS-Addon/releases)
- install [G1M importer](https://github.com/SolidLink95/AOC_tools/releases)
- dump Age of Calamity romfs (you must use your game dump) - for best compatibility v1.3 with all dlcs is recommended
- use [this tutorial](https://gamebanana.com/tools/16914) to dump the games raw files 

## 2. Introduction

Only CharacterEditor models were tested. Use [this spreadsheet](https://docs.google.com/spreadsheets/d/1wkYA7XCw5sEmcxPcXl82rFFPJhzWtrnKAmc9ZHNxDXo/edit?gid=268849924#gid=268849924) to find the proper g1m file.

## 3. Importing


- Go to `path/to/raw/files/CharacterEditor/g1m`
- Copy the g1m file into the separate folder
- Open blender, click on `Active Tool and workspace settings`
![](https://raw.githubusercontent.com/SolidLink95/Age_of_Calamity_Datamining/main/tutorials/pngs/1.png)
- Choose the path to the game's raw files (`Dump path`)
- Go to `File -> Import -> 3DMigoto G1M raw buffers (.g1m)`
![](https://raw.githubusercontent.com/SolidLink95/Age_of_Calamity_Datamining/main/tutorials/pngs/2.png)
- Navigate to the folder with g1m file and click `Import`



