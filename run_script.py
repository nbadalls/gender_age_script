#run gender script

import get_age_label



def get_Hotel_PingTai_real_label():
	input_file = "/mnt/glusterfs/o2n/AgeGender/Train_Patches/image_list/singe_folder_list/PingTai_GE0_list.txt"
	get_age_label.get_real_age_label(input_file)

def get_Age_Gender_real_label():
	input_file = "/mnt/glusterfs/o2n/AgeGender/Train_Patches/image_list/singe_folder_list/Age_Sex_Data_clean_GE0_list.txt"
	get_age_label.get_real_age_label2(input_file)

def get_label_only_has_gender_attribute():
	input_file = "/mnt/glusterfs/o2n/AgeGender/Train_Patches/image_list/singe_folder_list/Business_distract_collection-2018-08-09_GE0_list.txt"
	get_age_label.create_label_without_age_attribute(input_file)	

def transform_realage_to_softmax_label():
	input_read_label_file = "/mnt/glusterfs/o2n/AgeGender/Train_Patches/image_list/singe_folder_list/Age_Sex_Data_clean_GE0_list_real_label.txt"
	get_age_label.create_softmax_label(input_read_label_file)



if __name__ == '__main__':
	# get_Hotel_PingTai_real_label()
	# get_Age_Gender_real_label()
	# get_label_only_has_gender_attribute()
	transform_realage_to_softmax_label()