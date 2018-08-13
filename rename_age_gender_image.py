import os
import sys
import shutil

def rename_age_gender_test_set(folder_path):
	dst_path = '{}_rename'.format(folder_path)
	for f_index, elem in enumerate(os.listdir(folder_path)):
		image_path =  '{}/{}'.format(folder_path, elem)

		if elem.find('female') >=0:
			gender = 0
		else:
			gender = 1
		age =  elem.split('_')[1]

		for i_index, image_name in enumerate(os.listdir(image_path)):
			if i_index < 6:
				dst_name = 'yong{}_age-{}_gender-{}_{}.jpg'.format(f_index, age, gender, i_index)
				src_image_path = "{}/{}".format(image_path, image_name)
				dst_image_path = '{}/{}/{}'.format(dst_path, elem, dst_name)
				if not os.path.exists('{}/{}'.format(dst_path, elem) ):
					os.makedirs('{}/{}'.format(dst_path, elem))
				shutil.copy(src_image_path, dst_image_path)

if __name__ == '__main__':
	folder_path = "/mnt/glusterfs/o2n/AgeGender/TestSet/Age_testset"
	rename_age_gender_test_set(folder_path)