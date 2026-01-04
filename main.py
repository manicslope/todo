from pprint import pprint
from datetime import datetime, timedelta


def parse_date(d):
    return datetime.strptime(d, '%Y-%m-%d')


def parse_recurrence(s):
    if s == '0':
        return None
    modifier = s[-1]
    time = int(s[:-1])
    modifiers = {
        'y': 365,
        'w': 7,
    }
    return time * modifiers[modifier]


class Task():
    def __init__(self, row):
        self.object = row[0]
        self.name = row[1]
        self.last_date = parse_date(row[2])
        self.recurrence = parse_recurrence(row[3])
        self.mileage = int(row[4])
        self.mileage = None if self.mileage == 0 else self.mileage

    def next_date(self, last_date, recurrence):
        return last_date + timedelta(days=recurrence) if recurrence else None
        


def main():
    with open('records.csv', 'r') as f:
        lines = f.readlines()
    tasks = []
    for line in lines[1:]:
        lines = [l.strip() for l in line.split(',')]
        # print(lines)
        tasks.append(Task(lines))
    for task in tasks:
        next_date = task.next_date(task.last_date, task.recurrence)
        if next_date:
            print(f'Next date for {task.object} {task.name}: {next_date}')
        # pprint(vars(task))


if __name__ == '__main__':
    main()
