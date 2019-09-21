import json
import xlsxwriter
import re

workbook = xlsxwriter.Workbook('analisis.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write("A1", "#semanadeingenieria")
worksheet.write("B1", "#creadoresdeloimposible")

tweets = open("tweets.txt","w+")

def remove_emoji(string):
    emoji_pattern = re.compile("["
                       u"\U0001F600-\U0001F64F"  # emoticons
                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                       u"\U00002702-\U000027B0"
                       u"\U000024C2-\U0001F251"
                       u"\U0001f926-\U0001f937"
                       u"\u200d"
                       u"\u2640-\u2642"
                       u"\U0001f920" 
                       "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

with open('creadores.json') as f:
    dataCreadores = json.load(f)

with open('semanaingenieria.json') as k:
    dataSemanaIngenieria = json.load(k)


for statuses in dataCreadores['statuses']:
    status = remove_emoji(statuses['text'])
    tweets.write(status + "\n")
    print(status)

for statuses in dataSemanaIngenieria['statuses']:
    status = remove_emoji(statuses['text'])
    tweets.write(status + "\n")
    print(status)

contadorCreadores = 0
for statuses in dataCreadores['statuses']:
    # print(statuses['entities']['hashtags'])
    for hashtags in statuses['entities']['hashtags']:
        # print(hashtags['text'])
        contadorCreadores = contadorCreadores + 1
        worksheet.write(contadorCreadores, 1, hashtags['text'])


contadorSemanaIngenieria = 0
for statuses in dataSemanaIngenieria['statuses']:
    # print(statuses['entities']['hashtags'])
    for hashtags in statuses['entities']['hashtags']:
        # print(hashtags['text'])
        contadorSemanaIngenieria = contadorSemanaIngenieria + 1
        worksheet.write(contadorSemanaIngenieria, 0, hashtags['text'])

workbook.close()

# print("# de Hashtags: CreadoresDeLoImposible: " + str(contadorCreadores))

# print("# de Hashtags: SemanaIngenieria: " + str(contadorSemanaIngenieria))
