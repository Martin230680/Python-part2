# TODO здесь писать код
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.push((task, priority))

    def remove_task(self, task):
        temp_stack1 = Stack()
        flag_removed = False
        print(f'Удалить задачу: {task}\n')
        while not self.tasks.is_empty():
            current_task = self.tasks.pop()

            if current_task[0] != task:
                temp_stack1.push(current_task)
            else:
                flag_removed = True

        while not temp_stack1.is_empty():
            self.tasks.push(temp_stack1.pop())

        if not flag_removed:
            print("Task not found.")

    def __str__(self):
        temp_stack = Stack()
        sorted_tasks = Stack()
        result = ""

        while not self.tasks.is_empty():
            tmp = self.tasks.pop()
            if tmp not in temp_stack.stack:
                temp_stack.push(tmp)

        sorted_tasks.stack = sorted(temp_stack.stack, reverse=True, key=lambda x: x[1])
        while not sorted_tasks.is_empty():
            task, priority = sorted_tasks.pop()
            self.tasks.push((task, priority))

            result += f"{priority} - {task}\n"

        return result


manager = TaskManager()

manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)

print(manager)
manager.remove_task("помыть посуду")
print(manager)
manager.remove_task("поесть")
print(manager)