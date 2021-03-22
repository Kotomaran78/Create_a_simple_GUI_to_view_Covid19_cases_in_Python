import requests
import json


if __name__ == "__main__":
    
    info_global = requests.get('https://epidemic-stats.com/coronavirus/')#Getting access to global statistics
    text_info_global = info_global.text#translating html to str
    line = text_info_global.split('\n')#we divide each line break line by line
    other_contry = {}#creating an empty dict
    i=0
    for val in line:#for each row in the 'line' variable
        space = 0
        marks = 0
        non = 0
        key = ''#creating an empty key
        value = ''#creating an empty value
        if val == '        ];':#if we meet the value we end parsing
            if i == 1:
                i = 0
                break
        
        if i == 1:#if i=1 start recording
            for simb in val:#for each character in the string
                if simb == "'":#if the symbol is ' then add 1
                    marks+=1#№ quotation marks
                if marks == 1:
                    if simb != "'":
                        if simb == " " and space == 0:
                            space = 1
                        else:
                            space = 1
                            if simb == "&":
                                non = 1
                            if non == 0:
                                key+=simb
                            if simb == ";":
                                non = 0
                if marks == 3:
                    if simb != "'":
                        value+=simb
                if marks == 4:
                    break
            v=0
            if key != '':#if the key has a value
                for ky in other_contry:
                    if key == ky:
                        v=1
                if v == 0:
                    other_contry[key]=value

        if val == '        var availableTags = [':#if we meet the value we start parsing
            i = 1

    data_covid={}
    globl = requests.get('https://epidemic-stats.com/coronavirus/')
    txt_globl = globl.text
    lne = txt_globl.split('\n')
    listdate = []
    n = 0
    for val in lne:
        if val == '        ]':
            if n == 1:
                n = 0
                break

        if n == 1:
            a = val.replace(' ', '')
            b = a.replace("'", '')
            c = b.replace(',', '')
            if c != '':
                # print(c)
                listdate.append(c)

        if val == '        const date_sum = [':
            n = 1
    listinfected = []
    for val in lne:
        if val == '        ]':
            if n == 1:
                n = 0
                break

        if n == 1:
            a = val.replace(' ', '')
            b = a.replace("'", '')
            c = b.replace(',', '')
            if c != '':
                # print(c)
                listinfected.append(int(c))

        if val == '        const infected_sum = [':
            n = 1

    listdeth = []
    for val in lne:
        if val == '        ]':
            if n == 1:
                n = 0
                break

        if n == 1:
            a = val.replace(' ', '')
            b = a.replace("'", '')
            c = b.replace(',', '')
            if c != '':
                # print(c)
                listdeth.append(int(c))

        if val == '        const deaths_sum = [':
            n = 1

    listrecovered = []
    for val in lne:
        if val == '        ]':
            if n == 1:
                n = 0
                break

        if n == 1:
            a = val.replace(' ', '')
            b = a.replace("'", '')
            c = b.replace(',', '')
            if c != '':
                # print(c)
                listrecovered.append(int(c))

        if val == '        const recover_sum = [':
            n = 1

    data_covid['Global']={'data' : listdate,'infected' : listinfected, 'deth' : listdeth, 'recovered' : listrecovered}



    for keys in other_contry:
        nfo = requests.get('https://epidemic-stats.com'+str(other_contry[keys]))
        if nfo.status_code == 200:
            text = nfo.text
            line = text.split('\n')
            listdate = []
            n = 0
            for val in line:
                if val == '        ]':
                    if n == 1:
                        n = 0
                        break

                if n == 1:
                    a = val.replace(' ', '')
                    b = a.replace("'", '')
                    c = b.replace(',', '')
                    if c != '':
                        # print(c)
                        listdate.append(c)

                if val == '        const date = [':
                    n = 1
            listinfected = []
            for val in line:
                if val == '        ]':
                    if n == 1:
                        n = 0
                        break

                if n == 1:
                    a = val.replace(' ', '')
                    b = a.replace("'", '')
                    c = b.replace(',', '')
                    if c != '':
                        # print(c)
                        listinfected.append(int(c))

                if val == '        const infected = [':
                    n = 1

            listdeth = []
            for val in line:
                if val == '        ]':
                    if n == 1:
                        n = 0
                        break

                if n == 1:
                    a = val.replace(' ', '')
                    b = a.replace("'", '')
                    c = b.replace(',', '')
                    if c != '':
                        # print(c)
                        listdeth.append(int(c))

                if val == '        const deaths = [':
                    n = 1

            listrecovered = []
            for val in line:
                if val == '        ]':
                    if n == 1:
                        n = 0
                        break

                if n == 1:
                    a = val.replace(' ', '')
                    b = a.replace("'", '')
                    c = b.replace(',', '')
                    if c != '':
                        # print(c)
                        listrecovered.append(int(c))

                if val == '        const recovered = [':
                    n = 1

            if listdate != []:
                data_covid[keys]={'data' : listdate,'infected' : listinfected, 'deth' : listdeth, 'recovered' : listrecovered}

    with open("data_covid.json", "w", encoding="utf-8") as file:
        json.dump(data_covid, file)
