monkey = {}


def process_file():
    file = open("../input.txt", "r")
    i = 0
    for line in file:
        if line != "\n":
            items = [int(i.strip()) for i in next(file).strip().split(":")[1].split(",")]
            operation = next(file).strip().split(": ")[1].split()
            test = int(next(file).strip().split()[-1])
            true = int(next(file).strip().split()[-1])
            false = int(next(file).strip().split()[-1])
            monkey[i] = {
                "items": items,
                "operation": operation,
                "test": test,
                "true": true,
                "false": false,
                "inspected": 0
            }
            i += 1
    file.close()


if __name__ == '__main__':
    process_file()
    period = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23
    for _round in range(10_000):
        for m in monkey:
            arg = monkey[m]["operation"][4]
            op = monkey[m]["operation"][3]
            divisible_by = monkey[m]["test"]
            if_true = monkey[m]["true"]
            if_false = monkey[m]["false"]
            if arg == "old":
                for i in range(0, len(monkey[m]["items"])):
                    item = monkey[m]["items"][i]
                    new_item = (item * item if op == "*" else item + item) % period
                    if new_item % divisible_by == 0:
                        monkey[if_true]["items"].append(new_item)
                    else:
                        monkey[if_false]["items"].append(new_item)
                    monkey[m]["inspected"] += 1
            else:
                arg = int(arg)
                for i in range(0, len(monkey[m]["items"])):
                    item = monkey[m]["items"][i]
                    new_item = (item * arg if op == "*" else item + arg) % period
                    if new_item % divisible_by == 0:
                        monkey[if_true]["items"].append(new_item)
                    else:
                        monkey[if_false]["items"].append(new_item)
                    monkey[m]["inspected"] += 1
            monkey[m]["items"] = []

    inspection_count = []
    for m in monkey:
        inspection_count.append(monkey[m]["inspected"])

    inspection_count.sort(reverse=True)
    monkey_business = inspection_count[0] * inspection_count[1]

    print(monkey_business)
