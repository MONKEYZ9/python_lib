# LV3 : csv / CSV 파일을 불러와주세요.
# step3.csv

# 결과
# ['Keyword', 'New Users', 'Entered Checkout (Goal 4 Completions)']
# ['+hoodies', '1,072', '0']
# ['+hoody', '990', '1']
# ['Google Merchandise Store', '459', '126']
# ['+sweatshirt', '566', '2']
# ['youtuber merch', '345', '2']
# ['+tumbler', '276', '1']
# ['(not set)', '123', '34']
# ['hoodies', '247', '0']
# ['+youtube +merchandise', '203', '0']
# ['Google Apparel', '110', '21']
# ['+youtubers +merch', '128', '0']
# ['+youtuber +merch', '120', '0']

from csv import reader as r
with open('C://Users\mingzzang\Desktop\step3.csv', 'r') as csv_file:

    csv_reader = r(csv_file)
    for i in csv_reader:
        print(i)

    # line = csv_file.readlines()
    # for i in range(13):
    #     for i2 in line:

    #     arr.append(line[i])
    #     print(arr)
    #     arr=[]