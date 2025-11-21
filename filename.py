import sys

# Jenkins does not pass arguments unless configured
# So first check if we *actually* received one
if len(sys.argv) > 1:
    file = sys.argv[1]
    print("User provided filename:")
else:
    print("No input given - Default value is:")
    file = "cartoon.img"

# Checking extension
if file.endswith(".img"):
    print("It's an image")
elif file.endswith(".mp4"):
    print("It's a video")
elif file.endswith(".doc"):
    print("It's a document")
else:
    print("Invalid Choice!")
