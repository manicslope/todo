from pprint import pprint
from datetime import datetime, timedelta


def parse_date(d):
    return datetime.strptime(d, '%Y-%m-%d')


def parse_recurrence(s):
    if s == '0':
        return None
    modifier = s[-1]
    time = int(s[:-1])
    if modifier == 'y':
        time *= 365
    return time


class Task():
    def __init__(self, row):
        self.object = row[0]
        self.name = row[1]
        self.last_date = parse_date(row[2])
        self.recurrence = parse_recurrence(row[3])
        self.mileage = int(row[4])
        self.mileage = None if self.mileage == 0 else self.mileage
        self.next_date = self.last_date + timedelta(days=self.recurrence) if self.recurrence else None


def main():
    with open('records.csv', 'r') as f:
        lines = f.readlines()
    columns = lines[0]
    rows = list(map(lambda x: x.split(','), lines[1:]))
    tasks = []
    for line in lines[1:]:
        lines = [l.strip() for l in line.split(',')]
        print(lines)
        tasks.append(Task(lines))
    for task in tasks:
        pprint(vars(task))


if __name__ == '__main__':
    main()