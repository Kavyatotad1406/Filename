import sys
if len(sys.argv)<1:
    file=char(sys.argv[1])
    print("User provided filename:")
else:
    print("No input given-Default value is:")
    file=cartoon.img 

if(file=".img"):
    print("It's an image")
elif(file=".mp4"):
   print("It's a video")
elif(file=".doc"):
   print("It's a document")
else:
    print("Invalid Choice!")               
