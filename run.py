# coding=utf-8
#!/usr/bin/env python
import os
import shutil

ABSPATH = os.path.abspath('.')  # 获取当前的绝对地址
# TARGETPATH = ['C:/Users/ubuyg/Documents/jiaobenlaren/target/target1', 'C:/Users/ubuyg/Documents/jiaobenlaren/target/target2', 'C:/Users/ubuyg/Documents/jiaobenlaren/target/target3']  # 目标地址，存放模拟器中电报文件夹的位置，以列表形式存放
# TARGETPATH.sort()
TARGET_NUMBER = 10  # 每个模拟器文件夹存放的电报文件夹个数
DIRNUMBERS = 3  # 指定目标文件夹数量，通常是将打开的模拟器的数量


def getPhonelist(abspath):
    PHONELIST = os.listdir(os.path.join(abspath, 'source'))
    PHONELIST.sort()
    return PHONELIST


def makeDir(abspath):
    '''若源文件夹、归档文件夹和临时文件夹不存在，则创建'''
    if os.path.exists(os.path.join(ABSPATH, 'source')):
        pass
    else:
        os.mkdir(os.path.join(abspath, 'source'))
    if os.path.exists(os.path.join(abspath, 'file')):
        pass
    else:
        os.mkdir(os.path.join(abspath, 'file'))
    if os.path.exists(os.path.join(abspath, 'current')):
        pass
    else:
        os.mkdir(os.path.join(abspath, 'current'))


def fileExist(path):
    '''检测目标文件夹是否为空，不为空则清空'''
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else: 
        os.makedirs(path)


def clearDir(path):
    for line in path:
        fileExist(line)
  
def getTargetPath(abspath):
    '''从文本文件中获取目标文件夹'''
    targetDir = []
    if os.path.exists(os.path.join(abspath, 'targetPath.txt')) != True:
        with open(os.path.join(abspath, 'targetPath.txt'), 'a') as f:
            f.write('')
    else:
        with open(os.path.join(abspath, 'targetPath.txt'), 'r') as r:
            for line in r.readlines():
                targetDir.append(line.strip())
    targetDir.sort()
    return targetDir


def doCopyAndMove(phonelist, abspath):
    '''从电报文件夹列表中获取一个，并将该文件夹存放到临时文件夹和归档文件夹，并在临时文件夹中创建文本文件记录'''
    DIRNAME = phonelist.pop()
    dirName_str = str(DIRNAME)
    print(dirName_str)
    ABSPATH_CUR = os.path.join(os.path.join(abspath, 'source/'), DIRNAME)
    MOVE_PATH = os.path.join(abspath, 'file/', DIRNAME)
    shutil.copytree(ABSPATH_CUR, os.path.join(abspath, 'current/', DIRNAME))
    shutil.move(ABSPATH_CUR, MOVE_PATH)
    with open(os.path.join(abspath, 'current/', 'file.txt'), 'a') as fil:
        fil.write(dirName_str + '----2222\n')


def doMoveToTarDirs(targetpath, abspath):
    '''将临时文件夹中的所有文件移动到目标文件夹'''
    targetDir = targetpath.pop()
    print(targetDir)
    for list in os.listdir(os.path.join(abspath, 'current/')):
        absfilepath = os.path.join(abspath, 'current/', list)
        shutil.move(absfilepath, targetDir)


def doCount(targetNumber, phonelist, targetpath, abspath, dirNumbers):
    '''将指定数量的目标文件夹内移动指定的电报文件夹'''
    for i in range(dirNumbers):
        if len(phonelist) >= targetNumber:
            for numbers in range(targetNumber):
                doCopyAndMove(phonelist, abspath)
            doMoveToTarDirs(targetpath, abspath)
        else:
            print('数量不足')
            return


if __name__ == '__main__':
    makeDir(ABSPATH)
    TARGETPATH = getTargetPath(ABSPATH)
    PHONELIST = getPhonelist(ABSPATH)
    clearDir(TARGETPATH)
    doCount(TARGET_NUMBER, PHONELIST, TARGETPATH, ABSPATH, DIRNUMBERS)
    input('Press Enter')