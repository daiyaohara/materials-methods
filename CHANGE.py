# coding: UTF-8
import os
import codecs

def OS():
    try:
        os.uname()
    except AttributeError:
        flag_win32 = True
    if flag_win32:
        return('Windows')
    else:
        return('Linux')

def open_file(path_from_pwd):
    now = os.getcwd()
    path = os.path.join(now,path_from_pwd)
    print(path)
    f = open(path,'r').read()
    return (f)

def get_file_name_from_path(path):
    num = path.rfind('/')
    file_name = path[num+1:len(path)]
    num2 = file_name.rfind('.')
    file_name2 = file_name[0:num2]
    return (file_name2)

def insert_block_to_html(Target_file_path, block_file_path, block_name):
    f = open_file(Target_file_path)
    num = f.find(block_name)
    num2 = len(block_name)
    f1 = open_file(block_file_path)
    new_doc = ''
    new_doc =f[0:num-1] + f1 + f[num+num2:len(f)]
    block_file_path_name = get_file_name_from_path(block_file_path)
    Target_file_path_name = get_file_name_from_path(Target_file_path)
    new_doc_name = """{0}_{1}.html""".format(Target_file_path_name,block_file_path_name)
    f2 = open(new_doc_name, 'w')
    f2.write(new_doc)
    f2.close()



insert_block_to_html('Wiki2017/2017materials&methods.html','html/No001_Primer List.txt','<!--Block_primer.py-->')