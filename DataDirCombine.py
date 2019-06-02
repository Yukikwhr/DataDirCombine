from pathlib import Path
import sys
args = sys.argv

targetDir = Path(args[1])
if len(args) != 3:
    print("Mismatch number of args")
    sys.exit()

targetList = list(targetDir.glob("*.csv"))
if len(targetList) == 0:
    fw = open(args[2], 'a')
    fw.close()
else:
    for target in targetList:
        fr = open(target, 'r')
        lines = fr.readlines()
        fr.close()
        with open(args[2], 'a') as fw:
            for line in lines:
                fw.writelines(line)
