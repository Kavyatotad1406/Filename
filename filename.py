import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
    print("User provided filename:", file)
else:
    print("No input given - Default value is:")
    file = "cartoon.img"
    print("Filename:", file)

if file.endswith(".img"):
    print("It's an image ->", file)
elif file.endswith(".mp4"):
    print("It's a video ->", file)
elif file.endswith(".doc"):
    print("It's a document ->", file)
else:
    print("Invalid Choice! ->", file)
