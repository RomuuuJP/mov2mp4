import os

def getFilesList(path):
    fileList = set()
    for root, dirs, files in os.walk(path):
        for filespath in files:
            path.append(os.path.join(root, filespath))
    return path

def getMovFiles():
    cur_path = os.getcwd()
    ret = getFilesList(cur_path)
    listSpicalpath = set()
    for i in ret:
        # change to any types by changing ".MOV" to other type :-)
        if os.path.splitext(i)[1] == ".MOV":
            listSpicalpath.add(os.path.splitext(i)[0])
    return listSpicalpath

mov_list = getMovFiles()
for mov in mov_list:
    cmd = f"ffmpeg.exe -i {mov}.MOV -vcodec libx264 {mov}.MP4" # x264 encode by CPU. It's a hard job, but not that hard :-)
    #print(cmd)
    os.system(cmd)