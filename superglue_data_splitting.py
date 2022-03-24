import os
import random
import shutil

# TASK_DEV_SIZES = {"boolq": 500, "cb": 50, "copa": 50, "multirc": 50, "record": 7500, "rte": 250, "wic": 100, "wsc": 50}
TASK_DEV_SIZES = {"BoolQ": 500, "CB": 50, "COPA": 50, "MultiRC": 50, "ReCoRD": 7500, "RTE": 250, "WiC": 100, "WSC": 50}


def file_len(fname):
    count = 0
    with open(fname) as file:
        for line in file:
            if not line:
                break
            else:
                count += 1
        return count


if __name__ == "__main__":
    for task_name, size in TASK_DEV_SIZES.items():
        try:
            os.makedirs(os.path.join("split_data", task_name.lower()))
        except FileExistsError:
            pass
        train_file_path = os.path.join("data", task_name, "train.jsonl")
        test_file_path = os.path.join("data", task_name, "val.jsonl")
        new_train_file_path = os.path.join("split_data", task_name.lower(), "train.jsonl")
        dev_file_path = os.path.join("split_data", task_name.lower(), "val.jsonl")
        new_test_file_path = os.path.join("split_data", task_name.lower(), "test.jsonl")
        total_lines = file_len(train_file_path)
        print(f"{task_name}: {size} out of {total_lines}")
        indexes = list(range(total_lines))
        dev_indices = random.sample(indexes, size)
        with open(train_file_path, encoding="utf8") as f, open(new_train_file_path, 'w', encoding="utf8") as g, open(
                dev_file_path, 'w', encoding="utf8") as h:
            for i, line in enumerate(f):
                if i in dev_indices:
                    h.write(line)
                else:
                    g.write(line)
        shutil.copy(test_file_path, new_test_file_path)
