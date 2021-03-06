# -*- coding: utf-8 -*-
import xlrd
import os
from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq
from Bio.SeqUtils import GC

def change_special(str):
    str2 = ''
    for character in str:
        if character == '®':
            R = """&#174;"""
            str2 = str2 + R
        elif character == '<':
            left = """&lt;"""
            str2 = str2 + left
        elif character == '<':
            right = """&gt;"""
            str2 = str2 + right
        else:
            str2 = str2 + character
    return str2


def makeHTML(list_a,A,B,C,D,E,F,G,H,I,J,b):
    tag = list_a[0]
    No = int(list_a[1])

    for p2 in range(len(A)):
        A[p2] = change_special(A[p2])



    for p1 in range(1,len(A)):
        C[p1]=len(B[p1])
        myseq = Seq(B[p1])
        Tm = mt.Tm_NN(myseq, nn_table=mt.DNA_NN1)
        D[p1]= round(Tm)
        E[p1] = round(GC(B[p1]))





    li = [A,B,C,D,E,F,G,H,I,J]
    for x in range(len(li)):
        if len(li[x]) == 0:
            X = x
            break
    li = li[0:X]

    if No <10:
        No = "00{0}".format(No)

    elif No >9 and No <100:
        No = "0{0}".format(No)

    str1 = """<!-- Table Generated by TableMaker.py Author: OHAD -->
<h2 id = "{0}">{0}</h2>
<table>
<tr>""".format(tag)
    for y in range(len(li)):
        str2 = """<th>{0}</th>""".format(li[y][0])
        str1 = str1 + str2

    str3 = """</tr>"""
    str4 = """<tr>"""
    s1 = """<tr>"""
    s2 = """</tr>"""

    str = str1 + str3
    for t in range(1, b-1):
        for z in range(X):
            str5 = """<td>{0}</td>""".format((li[z][t]))
            s1 = s1 + str5
        s1 = s1 + s2
        str = str + s1
        s1 = str4

    str5 = """</table>
    <!-- Table end -->
    """
    str = str + str5
    now = os.getcwd()

    flag_win32 = False
    try:
        os.uname()
    except AttributeError:
        flag_win32 = True
    if flag_win32:
        path = os.path.join(now,'html\\No{0}_{1}_primerPy.txt'.format(No,tag))
    else:
        path = os.path.join(now, 'Block/PrimerList.txt'.format(No, tag))

    f = open(path, 'w')
    f.write(str)
    f.close()

def makestr(list_a,A,B,C,D,E,F,G,H,I,J,b):
    tag = list_a[0]
    No = int(list_a[1])

    for p2 in range(len(A)):
        A[p2] = change_special(A[p2])

    li = [A,B,C,D,E,F,G,H,I,J]
    for x in range(len(li)):
        if len(li[x]) == 0:
            X = x
            break
    li = li[0:X]

    if No <10:
        No = "00{0}".format(No)

    elif No >9 and No <100:
        No = "0{0}".format(No)

    str1 = """<!-- Table Generated by TableMaker.py Author: OHAD -->
<h2 id = "{0}">{0}</h2>
<table>
<tr>""".format(tag)
    for y in range(len(li)):
        str2 = """<th>{0}</th>""".format(li[y][0])
        str1 = str1 + str2

    str3 = """</tr>"""
    str4 = """<tr>"""
    s1 = """<tr>"""
    s2 = """</tr>"""

    str = str1 + str3
    for t in range(1,b-1):
        for z in range(X):
            str5 = """<td>{0}</td>""".format((li[z][t]))
            s1 = s1 + str5
        s1 = s1 + s2
        str = str + s1
        s1 = str4
    str5 = """
</table>
<!-- Table end -->
"""
    str = str + str5
    return str

book = xlrd.open_workbook('primer_list_2017.xlsx')
sentense = """"""
#どこのシートまで記入されているかを判定
for i in range(book.nsheets): #i = sheet_numbers
    sheet = book.sheet_by_index(i)
    if sheet.ncols == 1 and sheet.nrows ==5:
        num = i
        break

#excel fileから値を取得
for l in range(1):
    sheet = book.sheet_by_index(l)
    list_a = []
    for row in range(0, 2):  # 0~5指定だということに注意　つまりセルの1~6
        list_a.append(sheet.cell(row, 1).value)
    list_A = []
    list_B = []
    list_C = []
    list_D = []
    list_E = []
    list_F = []
    list_G = []
    list_H = []
    list_I = []
    list_J = []

    for row in range(5, sheet.nrows):
        try:
            list_A.append(sheet.cell(row,0).value)
            list_B.append(sheet.cell(row,1).value)
            list_C.append(sheet.cell(row,2).value)
            list_D.append(sheet.cell(row,3).value)
            list_E.append(sheet.cell(row, 4).value)
            list_F.append(sheet.cell(row, 5).value)
            list_G.append(sheet.cell(row, 6).value)
            list_H.append(sheet.cell(row, 7).value)
            list_I.append(sheet.cell(row, 8).value)
            list_J.append(sheet.cell(row, 9).value)
        except:
            pass


    for b in range(0,len(list_B)):
        if list_A[b] == '':
            list_A[b]=list_A[b-1]

        elif list_A[b] == 'end':
            break
    try:
        for a in range(b):
            if list_B[a] =='':
                list_B[a] = list_B[a-1]

        for c in range(b):
            if list_C[c] == '':
                list_C[c]=list_C[c-1]

        for d in range(b):
            if list_D[d] == '':
                list_D[d]=list_D[d-1]

        for e in range(b):
            if list_E[e] == '':
                list_E[e] = list_E[e - 1]

        for f in range(b):
            if list_F[f] == '':
                list_F[f] = list_F[f - 1]

        for g in range(b):
            if list_G[g] == '':
                list_G[g] = list_G[g - 1]

        for h in range(b):
            if list_H[h] == '':
                list_H[h] = list_H[h - 1]

        for ii in range(b):
            if list_I[ii] == '':
                list_I[ii] = list_I[ii - 1]

        for j in range(b):
            if list_J[j] == '':
                list_J[j] = list_J[j - 1]
    except:
        pass

    try:
        list_A = list_A[0:b]
        list_B = list_B[0:b]
        list_C = list_C[0:b]
        list_D = list_D[0:b]
        list_E = list_E[0:b]
        list_F = list_F[0:b]
        list_G = list_G[0:b]
        list_H = list_H[0:b]
        list_I = list_I[0:b]
        list_J = list_J[0:b]
    except:
        pass

   #txt fileへの出力
    makeHTML(list_a,list_A,list_B,list_C,list_D,list_E,list_F,list_G,list_H,list_I,list_J,b)
    str = makestr(list_a,list_A,list_B,list_C,list_D,list_E,list_F,list_G,list_H,list_I,list_J,b)
    sentense = sentense + str


