## Absolum Fruit Fixer

There's a common problem in Absolum where playing in co-op mode (local or online) causes fruit rewards to not be given out correctly. These affect which Rituals you can play with, which can be a big bummer.

To solve this, I made a small python script that updates the fruit count in the save binary file that absolum uses.

I compiled this to a .exe (using pyinstaller) for ease of use. Feel free to use the included python script if you prefer as it works either way.

Note: This will update fruit on all save slots that match the given "old fruit count".

## How to Use

1. Exit steam in case the syncing interferes with modifying the files. I don't expect it to but you might as well.
2. Download this repo as a `.zip` file (<> Code -> Download ZIP).
3. Extract this zip on your computer so that you have access to the folder and its files.
4. Find your save files. Typically these are in `C:\Users\YourUsername\AppData\Local\Absolum_SaveGame_Steam` if you're on Windows. If you're on Linux or Mac, you'll have to find where those are for yourself. The files are called `Save.bin` and `Save.temp.bin`.
5. (Optional) Copy your old save files somewhere so you don't lose them. Though this code will preserve them in the `your_save_files` folder.
6. Copy your save files to the `your_save_files` folder in the Absolum-Fruit-Fixer folder that you got from extracting the zip.
7. Run the `fix_fruit.exe` (or in a shell `python fix_fruit.py` if you have python installed). Windows may give you a warning about the publisher being unknown because I'm just a random person so you'll have to tell windows it's okay to run if that's the case.
8. You will be prompted for your old fruit count and then for the fruit count you'd like instead. Enter these values and the script will run.
9. Copy the new `Save.bin` and `Save.temp.bin` from `patched_save_files` to the location of your existing save files and overwrite them.
10. You can now boot up Steam and launch Absolum. You're good to go. Note that Steam's cloud save will be out of sync (because you modified a file since last playing), so just click play instead of trying to sync. Otherwise the cloud save will overwrite what you just did.
11. If anything goes wrong (game won't boot or something), put your old saves back. Though I can't imagine why this would happen because we're just editing some bytes for the fruit count.

## Example

My save file has 0 fruit and I would like 10 fruit.

1. Double click the .exe.

![1](https://github.com/MartingaleCoda/Absolum-Fruit-Fixer/blob/main/demo/1.png)

2. I enter my current fruit count of 0.

![2](https://github.com/MartingaleCoda/Absolum-Fruit-Fixer/blob/main/demo/2.png)

3. I enter my desired fruit count of 10.

![3](https://github.com/MartingaleCoda/Absolum-Fruit-Fixer/blob/main/demo/3.png)

4. The output gives me some information about what it did.

![4](https://github.com/MartingaleCoda/Absolum-Fruit-Fixer/blob/main/demo/4.png)

5. I copy the save files from `patched_save_files` back to my starting folder, replacing my existing ones.

![4](https://github.com/MartingaleCoda/Absolum-Fruit-Fixer/blob/main/demo/5.png)

