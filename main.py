from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import requests
import re

## Multiple start and end variables to accomodate break/gap in roll number sequence.
r_start1 = 0
r_end1   = 0
r_start2 = 0
r_end2   = 0

res_p = {}
res_f = {}
res_w = {}
pratio = 0
main_list = [['RANK', 'NAME', 'SGPA']]

## For my Osmanian juniors, copy the live link, replace index.php with generate_results.php
## The link would be of this format:
## http://ip-addr/result_month_year/xx/generate_result.php

purl = 'http://202.63.117.72/result_dec_2023/31/generate_result.php'
f_path = f'Output\\cse\\Files'
report_path = f'Output\\cse\\Sem_report.pdf'


def main1():
    for hn in range (r_start1, r_end1 + 1):
        payload = {
            'htno' : hn,
            'submit' : 'SUBMIT'
        }

        fn1 = '\\' + str(hn) + ".html"
        fn = f_path + fn1

        s = requests.Session()
        r = s.post(purl, data = payload)

        with open('temp.html', 'w', encoding='utf-8') as file:
                file.write(r.text)

        with open('temp.html', 'r') as fr:
                lines = fr.readlines()
                ptr = 1

                with open(fn, 'w') as fw:
                    for line in lines:
                        
                        if ptr != 67 and ptr != 71 and ptr != 75 and ptr != 93:
                            fw.write(line)
                        ptr += 1 

def main2():
    for i in range(r_start1, r_end1 + 1):
        fn1 =   '\\' + str(i) + ".html"
        fl = f_path + fn1

        with open(fl, 'r') as file:
            tmp = file.read()
            name = re.findall(r'&nbsp;(.*?)<', tmp)[2]
            rn = re.findall(r'&nbsp;(.*?)<', tmp)[1]

            sgpa = re.findall(r'19">(.*?)<', tmp)[1]

            if (sgpa != '-'):
                    if (re.findall(r'"style19">&nbsp;(.*?)<', tmp)[0] == '-'):
                            sgpa = 'fail'
                    else:
                        sgpa = float("{:.2f}".format(float(re.findall(r'"style19">&nbsp;(.*?)<', tmp)[0])))
            else:
                sgpa = 'withheld'

        if (sgpa == 'fail'):
            res_f[name] = sgpa
        elif (sgpa == 'withheld'):
            res_w[name] = sgpa
        else:
            res_p[name] = sgpa

res_p = dict(sorted(res_p.items(), key=lambda x:x[1], reverse = True))

pratio = str(float("{:.2f}".format(len(res_p)/72))*100) + '%'

avg = 0

for key, value in res_p.items():
    avg = avg + float(value)

avg = float("{:.3f}".format( avg/(len(res_p)) ))



def pdf_rawd():
    for key, value in res_p.items():
        sub_list = [list(res_p.keys()).index(key)+1, key, value]
        main_list.append(sub_list)

pdf_rawd()

def build_report(main_list):
    pdf = SimpleDocTemplate(report_path, pagesize=letter)

    data = main_list

    table = Table(data, colWidths=[15*mm, 90*mm, 30*mm])

    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey), ('INNERGRID', (0, 0), (-1, -1), 0.70, colors.black), ('BOX', (0, 0), (-1, -1), 0.70, colors.black), ('ALIGN', (0,0), (-1,-1), 'CENTRE')])
    table.setStyle(style)

    elements = []
    elements.append(table)

    gap = [[' '], [' '], [' ']]
    table3 = Table(gap, colWidths=[30*mm, 30*mm])
    style2 = TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTRE')])
    table3.setStyle(style2)

    elements.append(table3)

    pdf.build(elements)

# uncomment the following 3 function calls
#main1()
#main2()
#build_report(main_list)

#print(res_p)
#print(res_f.keys())
#print(res_w)
