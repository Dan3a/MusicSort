import audio_metadata, os
files=[]
folders=[]
path="INSERT FOLDER HERE"
# ['path', 'album', 'title']

for filename in os.listdir(path):
    f = os.path.join(path,filename)
    if os.path.isfile(f):
        metadata = audio_metadata.load(f) # Loads the metadata from the song
        album = metadata.tags['album']  # Isolates album name
        files.append((f,album[0],filename))
        
for directory in os.listdir(path):
    f = os.path.join(path,directory)
    if os.path.isdir(f):
        folders.append(f)


for file in files:
    if file[1] not in folders:
        toCreate = os.path.join(path, file[1])
        destinationFile = os.path.join(toCreate, file[2]) 
        try:
            os.mkdir(toCreate)
        except:
            pass
        folders.append(toCreate)
        os.rename(file[0], destinationFile)
        print(destinationFile)
    else:
        destinationFile = os.path.join(path, file[1], file[2])
        os.rename(file[0], destinationFile)
        print(destinationFile)
