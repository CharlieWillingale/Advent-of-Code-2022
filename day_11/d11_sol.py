from utils import read_input
import re

# Load input
input = read_input('./day_11/input.txt')

#
# Part 1 solution
#

'''
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

'''

class Monkey:

    def __init__(self):
            
        self.items = []

        self.operation = ''
        self.test_condition = ''
        self.test_outcomes = {
            'True' : '',
            'False': ''
            }

        # to track most active monkey
        self.inspection_count = 0

    def add_items_list(self, items_list: list) -> None:

        for item in items_list:

            self.items.append(int(item))

    def add_item(self, item: int) -> None:

            self.items.append(item)

    def set_operation(self, operation: str) -> None:
        self.operation = operation

    def run_operation(self, old: int) -> int:
        return eval(self.operation)

    def set_test_condition(self, condition: str) -> None:
        self.test_condition = condition

    def run_test_condition(self, old:int) -> bool:
        return eval(self.test_condition)


    #  Expect form 'monkey_2.items.append(move_item)
    def set_true_outcome(self,true_outcome: str) -> None:
        self.test_outcomes['True'] = true_outcome
    
    def run_true_outcome(self, old:int) -> None:
        _ = self.items.pop(0)
        move_item = old
        eval(self.test_outcomes['True'])

    def set_false_outcome(self,false_outcome: str) -> None:
        self.test_outcomes['False'] = false_outcome

    def run_false_outcome(self, old:int) -> None:
        _ = self.items.pop(0)
        move_item = old
        eval(self.test_outcomes['False'])
    
    def run_test(self):

        if len(self.items) == 0:
            pass

        else:

            for i in range(0, len(self.items)):

                old = self.items[0]
                new = self.run_operation(old)
                # new = new // 3
                new = new % 26327730

                if self.run_test_condition(new):
                    self.run_true_outcome(new)
                else:
                    self.run_false_outcome(new)

                self.inspection_count += 1
        
monkey_0 = Monkey()
monkey_1 = Monkey()
monkey_2 = Monkey()
monkey_3 = Monkey()
# monkey_4 = Monkey()
# monkey_5 = Monkey()
# monkey_6 = Monkey()
# monkey_7 = Monkey()

monkeys = [monkey_0, monkey_1, monkey_2, monkey_3]#, monkey_4, monkey_5, monkey_6, monkey_7]
monkey_num = 0


# Setup for each monkey
for line in input:

    try:
        if line.strip()[0] == 'S':
            items = line.split(':')[1].strip().split(',')
            monkeys[monkey_num].add_items_list(items)

        elif line.strip()[0] == 'O':
            operation = line.split('=')[1]
            monkeys[monkey_num].set_operation(operation)

        elif line.strip()[0] == 'T':
            test = line.split(':')[1].strip().replace('divisible by', 'old %') + '== 0'
            monkeys[monkey_num].set_test_condition(test)

        elif line.strip().split()[1][0] == 't':
            true_outcome = line.strip().split(':')[1]
            true_outcome = true_outcome.replace(' throw to ','')
            true_outcome = true_outcome.replace(' ','_')
            true_outcome += '.items.append(move_item)'

            monkeys[monkey_num].set_true_outcome(true_outcome)
        
        elif line.strip().split()[1][0] == 'f':
            false_outcome = line.strip().split(':')[1]
            false_outcome = false_outcome.replace(' throw to ','')
            false_outcome = false_outcome.replace(' ','_')
            false_outcome += '.items.append(move_item)'

            monkeys[monkey_num].set_false_outcome(false_outcome)

    except IndexError:
        if line == '\n':
            monkey_num += 1
        else:
            pass


for _ in range(0,10_000):
    for monkey in monkeys:

        monkey.run_test()

for m, n in zip(monkeys, range(0,len(monkeys))):
    print('Monkey_'+str(n)+': ',m.inspection_count)

inspect_list = []
for monkey in monkeys:

    inspect_list.append(monkey.inspection_count)

inspect_list.sort()

monkey_business = inspect_list[-1] * inspect_list[-2]

print(monkey_business)