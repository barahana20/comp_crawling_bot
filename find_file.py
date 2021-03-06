import datetime
import glob
import os

def find_file_within_oneweek(file_name):
    timestamp = file_name[file_name.rfind('_')+1:file_name.index('.md')]
    timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H-%M")
    today = datetime.datetime.today()
    before_oneweek = today - datetime.timedelta(weeks=1)
    if timestamp < today and timestamp > before_oneweek:
        return True
    else:
        return False
def execute_oneweek():
    storage_path = '/home/barahana123/knu-cse-announcements-crawler/markdown'
    file_paths = glob.glob(os.path.join(storage_path, '*'))
    count = 1
    for file_path in file_paths:
        if find_file_within_oneweek(os.path.basename(file_path)):
            with open(file_path, 'r') as f:
                f_read = f.read()
                f_read = f_read.replace('\n\n', '\n')
                f_read = f_read[:f_read.index('\n목록')]
                with open('/home/barahana123/comp_crawling_bot/oneweek.txt', 'a') as g:
                    g.write(str(count)+'. '+f_read)
                    g.write('\n\n-------------------------------------------\n\n')
            count+=1
if __name__ == '__main__':
    with open('/home/barahana123/comp_crawling_bot/oneweek.txt', 'w') as g:
        pass
    execute_oneweek()
