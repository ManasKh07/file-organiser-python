import os 
import shutil

inputfolder="Python"
count=0
typesoffile={
     ".pdf":"pdf",
     ".txt":"txt",
     ".jpg":"jpg",
     ".png":"png",
     ".jpeg":"jpeg"
}
for files in typesoffile.values():
    os.makedirs(os.path.join(inputfolder,files),exist_ok=True)

for file in sorted(os.listdir(inputfolder)):
     src=os.path.join(inputfolder,file)
     if os.path.isdir(src):
          continue
     ext = os.path.splitext(file.lower())[1]
     if ext not in typesoffile.keys():
          continue
     for extension,destination in typesoffile.items():
          
               destinations=os.path.join(inputfolder,destination,file)
               shutil.move(src,destinations)
               count+=1
               break
          
print("Done")
print(f"\n No of files moved {count}")
