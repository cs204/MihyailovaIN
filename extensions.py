def main():
    v = str(input("File name: "))
    v = v.split(".")
    v = v[1]
    if v == 'gif':
        print('image/gif')
    elif v == 'jpg':
        print('image/jpeg')
    elif v == 'jpeg':
        print('image/jpeg')
    elif v == 'png':
        print('image/png')
    elif v == 'pdf':
        print('application/pdf')
    elif v == 'txt':
        print('application/txt')
    elif v == 'jpeg':
        print('application/zip')
    else:
        print('application/octet-stream')


main()
