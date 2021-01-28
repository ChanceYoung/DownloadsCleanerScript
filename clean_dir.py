import os,shutil, datetime as dt
import sys
result_dict = {}
zipped_list = []
do_not_delete_list = []

download_dir=sys.argv[1]
dir_list = os.listdir(download_dir)
folder_names = ("Photos","Videos","TextFiles","Book","Docs","Zipped","Audio","ExeFiles","Extracted")
photos_extension = ("jpg", "JPEG", "jpeg","png","HEIC","svg","JPG","gif","GIF")
videos_extension = ("mp4", "ovi")
scripts_extension = ("py","sh","txt","md","log")
book_extension = ("pdf","mobi","epub","PDF")
doc_extension = ("doc","docx","xlsx","csv","odt")
archive_extension = ("gz", "zip","deb")
audio_extension = ("mp3", "wav")
apps_extension = ("exe","jar","msi")

for each in dir_list:
    if os.path.isfile(download_dir + each):
        file_src = str(download_dir+each)
        if file_src.endswith(photos_extension):
            result_dict.setdefault(folder_names[0], []).append(each)
        if file_src.endswith(videos_extension):
            result_dict.setdefault(folder_names[1],  []).append(each)
        if file_src.endswith(scripts_extension):
            result_dict.setdefault(folder_names[2],  []).append(each)
        if file_src.endswith(book_extension):
            result_dict.setdefault(folder_names[3], []).append(each)
        if file_src.endswith(doc_extension):
            result_dict.setdefault(folder_names[4], []).append(each)
        if file_src.endswith(archive_extension):
            zipped_list.append(each)
            result_dict.setdefault(folder_names[5], []).append(each)
        if file_src.endswith(audio_extension):
            result_dict.setdefault(folder_names[6], []).append(each)
        if file_src.endswith(apps_extension):
            result_dict.setdefault(folder_names[7], []).append(each)   

def extractedcheck():
    zipped_path = str(download_dir + folder_names[5] + '/')
    if os.path.lexists(zipped_path):
        for every in os.listdir(zipped_path):
            source = str(download_dir+every)
            zip_path = str(download_dir + folder_names[5] + '/' + every)
            extractedpath = os.path.splitext(source)[0]
            zip_path = os.path.splitext(zipped_path)[0]
            for each in dir_list:
                if os.path.isdir(download_dir + each):
                    file_src = str(download_dir + each)
                    if extractedpath == file_src:
                        result_dict.setdefault(folder_names[8],[]).append(each)
                    if extractedpath == zip_path:
                       result_dict.setdefault(folder_names[8],[]).append(each)
    else:
        for every in zipped_list:
            source = str(download_dir+every)
            zip_path = str(download_dir + folder_names[5] + '/' + every)
            extractedpath = os.path.splitext(source)[0]
            zip_path = os.path.splitext(zipped_path)[0]
            for each in dir_list:
                if os.path.isdir(download_dir + each):
                    file_src = str(download_dir + each)
                    if extractedpath == file_src:
                        result_dict.setdefault(folder_names[8],[]).append(each)
                    if extractedpath == zip_path:
                       result_dict.setdefault(folder_names[8],[]).append(each)


extractedcheck()
print(result_dict)

for key in result_dict: 
    new_dir = download_dir+key+'/'
    os.makedirs(new_dir, exist_ok=True)
    [shutil.move(download_dir+each, new_dir+each) for each in result_dict[key]]

for each in dir_list:
    if os.path.isdir(download_dir + each):
        dir_path = str(download_dir + each)
        if dir_path.endswith(folder_names[0]):
            do_not_delete_list.append(dir_path)
        if dir_path.endswith(folder_names[1]):
            do_not_delete_list.append(dir_path)
        if dir_path.endswith(folder_names[2]):
            do_not_delete_list.append(dir_path)
        if dir_path.endswith(folder_names[3]):
            do_not_delete_list.append(dir_path)
        if dir_path.endswith(folder_names[4]):
            do_not_delete_list.append(dir_path)
        if dir_path.endswith(folder_names[5]):
            do_not_delete_list.append(dir_path)
        if dir_path.endswith(folder_names[6]):
            do_not_delete_list.append(dir_path)
        if dir_path.endswith(folder_names[7]):
            do_not_delete_list.append(dir_path)
        if dir_path.endswith(folder_names[8]):
            do_not_delete_list.append(dir_path)
    elif os.path.isfile(download_dir + each):
        file_path = str(download_dir + each)
        if file_path.endswith("ini"):
            do_not_delete_list.append(file_path)

for each in dir_list:
    file_check = str(download_dir + each) 
    if file_check not in do_not_delete_list:
        if os.path.isfile(file_check):
            os.remove(file_check)
        elif os.path.isdir(file_check):
            shutil.rmtree(file_check)



   


