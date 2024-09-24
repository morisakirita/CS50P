def main():
    file_name = input("File name: ").strip().lower()
    extension = get_extension(file_name)
    match extension:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


def get_extension(filen):
    extension = filen.split(".")
    return extension[-1]


main()
