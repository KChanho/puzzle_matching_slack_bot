import csv

# csv 생성
with open('./data/test.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerow(['ID', '이름', '지역', '날짜'])   # 열 제목

with open('./data/cancel.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerow(['ID', '이름'])   # 열 제목
    
with open('./data/result.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerow(['ID', '이름', '지역', '날짜'])   # 열 제목