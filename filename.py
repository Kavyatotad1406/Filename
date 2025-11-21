import sys

# If user provides argument, use it; else use default filename
if len(sys.argv) > 1:
    file = sys.argv[1]
    print("User provided filename:", file)
else:
    print("No input given - Default value is used:")
    file = "cartoon.img"

# Check file extension
if file.endswith(".img"):
    print("It's an image")
elif file.endswith(".mp4"):
    print("It's a video")
elif file.endswith(".doc"):
    print("It's a document")
else:
    print("Invalid Choice!")
