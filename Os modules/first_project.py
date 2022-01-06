import os,shutil
# NOTE:we can write every extension inside tupple because we cannot change any data in tupple . tupple is very fast than list and set :
dict_extension={
    'audio_extension':('.mp3','.m4a','.wav','.flac'),
    'vedio_extension':('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'documents_extension':('.doc','.pdf','.txt','.csv','.py')
}
folderpath=input('Enter a folder path :')
def file_finder(folder_path,file_extension):
    files=[]
    for file in os.listdir(folderpath):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files
for extension_type,extension_tupple in dict_extension.items():
    folder_name=extension_type.split('_')[0]+'FILES'
    folder_path=os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath,extension_tupple):
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)

        shutil.move(item_path,item_new_path)
input()