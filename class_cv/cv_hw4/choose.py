import os
import pdb
import csv

path = '/home/lysee13/class_cv/cv_hw4/yolov7/data/CityCam/Q2'
n=0
list_ = []

# with open('output_Q2.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)

#     for f in os.listdir(path):
#         if f.isdigit():
#             # pdb.set_trace()
#             for data in os.listdir(os.path.join(path,f)):
#                 if data.endswith('.txt'):
#                     n += 1
#                     temp = []
#                     file = open(os.path.join(path,f,data))
#                     n_2, n_5, n_7, n_else = 0, 0, 0, 0
#                     for line in file:
#                         if line[0] == '2':
#                             n_2 += 1
#                         elif line[0] == '5':
#                             n_5 += 1
#                         elif line[0] == '7':
#                             n_7 += 1
#                         # else:
#                         #     n_else += 1
                        
#                     writer.writerow([f,data,n_2,n_5,n_7,n_2+n_5+n_7])

list_q2 = []                    
with open('Q2_method2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        list_q2.append(row[0])
pdb.set_trace()
    


