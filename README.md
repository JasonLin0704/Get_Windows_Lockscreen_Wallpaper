# Get_Windows_Lockscreen_Wallpaper
A simple python script helps you get current lockscreen windows spotlight wallpaper.

## Note
Those image files on the lockscreen are saved under `'C:\Users\%UserName%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'`.\
We can view them as normal jpg files after changing their file extension into '.jpg'.

This script is purely to help locate these files, copy them, and convert them into JPG format. \
Before running the script, please check if two string variables are correct on your own pc: 
- `source_path`: where the original files are
- `target_path`: where you want to put those new files

Then it will create a folder called "wallpaper" as default for the pictures.
