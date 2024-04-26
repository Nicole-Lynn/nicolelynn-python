# Prompt the user for the name of a file and then output that file’s media type

f_name = input("File name: ").lower().strip()

if ".gif" in f_name:
    print("image/gif")

elif (".jpg") in f_name or ("jpeg") in f_name:
    print("image/jpeg")

elif ".png" in f_name:
    print("image/png")

elif ".pdf" in f_name:
    print("application/pdf")

elif ".txt" in f_name:
    print("text/plain")

elif ".zip" in f_name:
    print("application/zip")

else:
    print("application/octet-stream")


