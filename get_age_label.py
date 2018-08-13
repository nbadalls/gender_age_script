#use to get age_label

import sys
import os

#use to process Age gender data set
def get_real_age_label2(input_list_file):
	f = open(input_list_file, 'r')
	data = f.read().splitlines()
	f.close()

	dst_real_label_path = input_list_file.replace('.txt', '_real_label.txt')
	fout = open(dst_real_label_path, 'w')

	for index , line in enumerate(data):
		folder_prefix = line.split('/')[-2]  #C397male_23_Glasses
		real_age = folder_prefix.split('_')[1].strip(' ')
		if folder_prefix.find('male') >=0 and folder_prefix.find('female') <0:
			gender_label = 1
		elif folder_prefix.find('female') >=0:
			gender_label = 0
		else:
			print(folder_prefix)

		fout.write('{} {} {}\n'.format(line, real_age, gender_label))
		if index % 100 == 0:
			 sys.stdout.write('{}/{}\r'.format(index, len(data)-1))
			 sys.stdout.flush()
	fout.close()

#use to process pingtai and hotel dataset
def get_real_age_label(input_list_file):
	f = open(input_list_file, 'r')
	data = f.read().splitlines()
	f.close()

	dst_real_label_path = input_list_file.replace('.txt', '_real_label.txt')
	fout = open(dst_real_label_path, 'w')

	for index , line in enumerate(data):
		image_name_prefix = line.split('/')[-1].split('.')[0]
		#for pingtia data
		real_age = 2016-int(image_name_prefix[6:10])
		#for Hotel data
		# image_name_prefix = image_name_prefix.split('_')[-1]
		# real_age = 2017-int(image_name_prefix[6:10])

		gender_label = line.split('/')[-2]

		fout.write('{} {} {}\n'.format(line, real_age, gender_label))
		if index % 100 == 0:
			 sys.stdout.write('{}/{}\r'.format(index, len(data)-1))
			 sys.stdout.flush()

	fout.close()

def  create_label_without_age_attribute(input_file_file):
	f = open(input_file_file, 'r')
	data = f.read().splitlines()
	f.close()

	dst_real_label_path = input_file_file.replace('.txt', '_softmax_label.txt')
	fout = open(dst_real_label_path, 'w')

	for index, line in enumerate(data):
		gender_label = line.split('/')[-2]
		softmax_age_label = -1
		fout.write('{} {} {}\n'.format(line, softmax_age_label, gender_label))
		if index % 100 == 0:
			 sys.stdout.write('{}/{}\r'.format(index, len(data)-1))
			 sys.stdout.flush()
	fout.close()



#use to create softmax label
#label defination:
#age                    gender
#0  -15  0            male     1 
#16-25  1            female   0
#26-35  2
#36-45  3
#46-55  4
#56-65  5
#rest    -1

age_divide_label = [
[0,15], [16,25], [26,35], [36,45],[46,55],[56,65]
]
def create_softmax_label(input_read_label_file):

	if input_read_label_file.find('_real_label.txt') <0:
		print "Please input real label file.."
		return 

	f = open(input_read_label_file, 'r')
	data = f.read().splitlines()
	f.close()


	dst_real_label_path = input_read_label_file.replace('_real_label.txt', '_softmax_label.txt')
	fout = open(dst_real_label_path, 'w')
	for index ,line in enumerate(data):
		line = line.strip('\n')
		# print(line.split(' '))

		#process some exceptions
		age_str = line.split(' ')[-2]
		if len(age_str) >2:
			real_age =  int(age_str[0:2])
		elif len(age_str) == 0:
			real_age = -1
		else:
			real_age =  int(age_str)
		gender_label = line.split(' ')[-1]
		image_path = line.split(' ')[0]
		if real_age > 65 or real_age <0:
			softmax_age_label = -1
		else:
			for label, elem in enumerate(age_divide_label):
				if real_age >= elem[0] and real_age <= elem[1]:
					softmax_age_label = label
		fout.write('{} {} {}\n'.format(image_path, softmax_age_label, gender_label))
		if index % 100 == 0:
			 sys.stdout.write('{}/{}\r'.format(index, len(data)-1))
			 sys.stdout.flush()
	fout.close()

