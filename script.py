import os

username = os.getenv('UserName')
source_path = os.path.join(r'C:\Users', username, r'AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')
target_path = os.path.join(r'C:\Users', username, r'Desktop')
target_dir = os.path.join(target_path, 'wallpaper')

def init_target_dir() -> None:
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)

def rename_to_jpg() -> None:
    for file_name in os.listdir(source_path):
        root, ext = os.path.splitext(file_name)
        if ext != '.jpg':
            old_file_path = os.path.join(source_path, file_name)
            new_file_path = os.path.join(target_dir, file_name + '.jpg')
            os.system('copy {} {}'.format(old_file_path, new_file_path))

if __name__ == '__main__':
    init_target_dir()
    rename_to_jpg()
