label_list = ["label_train_col.txt", "label_train_geo.txt", "label_train_mixup.txt", "label_train_re.txt"]
logs = []

with open("label_train_combined.txt", "w", encoding="utf-8", newline="\n") as out_file:
    for file in label_list:
        with open(file, "r", encoding="utf-8") as in_file:
            lines = in_file.readlines()
            for line in lines:
                if line in logs:
                    continue
                else:
                    logs.append(line)
                    out_file.write(line)
