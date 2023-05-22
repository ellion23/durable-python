f = open('kept_u_waiting_huh.txt', 'r')
a = f.read()
for i in range(len(a)):
    if a[i] == ' ':
        if a[i+1] == ' ':
            if a[i+2] == ' ':
                if a[i+3] == ' ':
                    a[i] = "&#12288;"
                    a[i+1], a[i+2], a[i+3] = None


print(a)