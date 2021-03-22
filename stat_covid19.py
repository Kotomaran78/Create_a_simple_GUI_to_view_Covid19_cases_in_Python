import requests
import json


'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
'''




if __name__ == "__main__":
    # usa_info = requests.get('https://epidemic-stats.com/coronavirus/usa')
    # text = usa_info.text
    # line = text.split('\n')
    # i = 0
    # listdate = []
    # for val in line:
    #     if val == '        ]':
    #         i = 0

    #     if i == 1:
    #         a = val.replace(' ', '')
    #         b = a.replace("'", '')
    #         c = b.replace(',', '')
    #         if c != '':
    #             # print(c)
    #             listdate.append(c)

    #     if val == '        const date = [':
    #         i = 1
    # # print('listdate: ', listdate)

    # listdeth = []
    # for val in line:
    #     if val == '        ]':
    #         i = 0

    #     if i == 1:
    #         a = val.replace(' ', '')
    #         b = a.replace("'", '')
    #         c = b.replace(',', '')
    #         if c != '':
    #             # print(c)
    #             listdeth.append(int(c))

    #     if val == '        const deaths = [':
    #         i = 1
    # # print('listdeth: ', listdeth)

    # listinfected = []
    # for val in line:
    #     if val == '        ]':
    #         i = 0

    #     if i == 1:
    #         a = val.replace(' ', '')
    #         b = a.replace("'", '')
    #         c = b.replace(',', '')
    #         if c != '':
    #             # print(c)
    #             listinfected.append(int(c))

    #     if val == '        const infected = [':
    #         i = 1
    # # print('listinfected: ', listinfected)

    # listrecovered = []
    # for val in line:
    #     if val == '        ]':
    #         i = 0

    #     if i == 1:
    #         a = val.replace(' ', '')
    #         b = a.replace("'", '')
    #         c = b.replace(',', '')
    #         if c != '':
    #             # print(c)
    #             listrecovered.append(int(c))

    #     if val == '        const recovered = [':
    #         i = 1
    # # print('listrecovered: ', listrecovered)

    # print('date : deth : recovered : infected')
    # for n in range(len(listdate)):
    #     print(listdate[n],' : ',listdeth[n],' : ',listrecovered[n],' : ',listinfected[n])


    '''matlib
    # fig, ax = plt.subplots(figsize=(5, 3))
    # ax.stackplot(listdate, listdeth, labels=['Deth'])
    # ax.set_title('Combined debt growth over time')
    # ax.legend(loc='upper left')
    # ax.set_ylabel('Total debt')
    # fig.tight_layout()

    # ax = plt.subplots(figsize=(5, 3))
    # ax.stackplot(labels=['Deth'])
    # ax.set_title('Combined debt growth over time')
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # ax.grid(True, which='both')
    # ax.set_ylim(0, 20)
    # ax.set_xlim(0, 20)


    # plt.plot(listdate, listdeth)
    # plt.yticks(np.arange(0,int(listdeth[-1])+int(listdeth[-1])/8,int(listdeth[-1])/8))
    
    # ax.set_ylim([0, 100])
    # plt.plot(listdeth)
    # plt.show()

    # print(np.arange(0,int(listdeth[-1])+int(listdeth[-1])/8,int(listdeth[-1])/8))
    
    int_listdeth=[]
    for lin in listdeth:
        int_listdeth.append(int(lin))

    ax.plot(listdate, int_listdeth, color = 'r', linewidth = 3)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
    #  Устанавливаем интервал вспомогательных делений:
    # ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

    #  Тоже самое проделываем с делениями на оси "y":
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10000))
    # ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))

    ax.grid(which='major',
        color = 'k')

    ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

    plt.show()
    '''

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
