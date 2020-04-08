rows =3
cpu_count = 8

split_num_list = []


def return_step(rows, cpu_count):
    if rows % cpu_count == 0:
        step = int(rows / cpu_count)
    else:
        diff = (rows % cpu_count)
        print(diff)
        modified_rows = rows - diff
        print(modified_rows)
        step = int(modified_rows / cpu_count)
    return step


step=return_step(rows, cpu_count)

for i in range(step, rows, step):
    split_num_list.append(i)

print(split_num_list)
