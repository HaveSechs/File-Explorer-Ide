import io
import os
import time
import contextlib


def key(obj):
    return int(obj.split()[0])


def get_name(name):
    line = ""
    name = name.split()

    for num in range(len(name)):
        if num != 0:
            line += name[num] + " "
    return line


def read_code():
    files = sorted(os.listdir("./coding"), key=key)
    code = ""

    for file in files:
        code += get_name(file).replace("[[", ":").replace("]]]]", "\t") + "\n"
    print(files)
    return code


def run_code(code):
    print(code)
    storage = {}

    with io.StringIO() as buffer, contextlib.redirect_stdout(buffer):
        try:
            exec(code, storage)
            result = buffer.getvalue()
            print("1")
        except Exception as e:
            result = str(e)
            print(e)
    print(result)
    return result.split("\n")


def write_result(result):
    files = os.listdir("./coding")
    start_result = len(files)

    print(result)

    for num in range(0, len(result) + 1):
        if num == 0:
            with open(f"./coding/{start_result + num + 1} ~= Result Begins =~", "w") as f:
                f.write("")
        else:
            if len(result[num - 1]) != 0:
                with open(f"./coding/{start_result + num + 1} {result[num - 1].replace('<', '').replace('>', '')}", "w") as f:
                    f.write("")


def clear_result():
    files = os.listdir("./coding")
    start_removing = False
    for file in files:

        name = get_name(file)
        # print(name)
        number = name.split()[0]

        if name == "~= Result Begins =~":
            start_removing = True

        if start_removing:
            os.remove(f"./coding/{number} {name}")


if __name__ == '__main__':
    print("Compiler is up")
    while True:
        files = os.listdir("./coding")

        if "DELETE TO RUN" not in files:
            clear_result()

            code = read_code()
            result = run_code(code)
            write_result(result)

            with open("./coding/DELETE TO RUN", "w") as f:
                f.write("")

        time.sleep(1)
