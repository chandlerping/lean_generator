def generate(p):
    with open('./template.txt', 'rb') as f:
        lines = f.readlines()
        part_0 = lines[0:3]
        part_1 = lines[5:9]
        part_2 = lines[13:63]
        part_3 = lines[65:]

    lines_new_0 = []

    for i in range(1, p):
        lines_new_0.append("| r{}\n".format(str(i)).encode())

    lines_new_1 = []
    for j in range(1, p):
        for k in range(1, p):
            lines_new_1.append("| r{} r{} := r{}\n".format(str(j), str(k), str((j * k) % p)).encode())

    lines_new_2 = []
    for j in range(1, p):
        inv = pow(j, -1, p)
        lines_new_2.append("| r{} := r{}\n".format(str(j), str(inv)).encode())

    with open('target.txt', 'wb') as f:
        f.writelines(part_0 + lines_new_0 + part_1 + lines_new_1 + part_2 + lines_new_2 + part_3)


def main():
    generate(5)


if __name__ == "__main__":
    main()
