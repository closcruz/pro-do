# Prototype ToDo app for personal use
# By: Carlos Cruz Ramos
# Ver. 0.09

import datetime as dt


class Pad:
    """Object that contains data structure in which tasks are stored to form a complete ToDo list
    Takes in a string as a name and optionally a date to server as a deadline for the whole tasks incuded in this list"""

    _ids = []   # List that will contain all ids to check for uniqueness

    # Override __new__ to check to see if length of title is short enough to create the class.
    def __new__(cls, title, ids):  # Figure out how to check and keep track of id's for uniqueness
        if len(title) < 40 and ids not in Pad._ids:
            return super(Pad, cls).__new__(cls)
        else:
            raise ValueError("Please enter title with less than 40 characters and unique id.")

    def __init__(self, title, ids):
        self.title = title
        self.due = None
        self.todo = {}        # Dictionary that will contain task index with its corresponding Todo object
        self.tot_tasks = 0    # Keeps track of the total number of task in a
        self.idx = ids
        Pad._ids.append(ids)

    @property
    def name(self):
        """'Name' property of Pad."""
        print("Getting title of pad: {}".format(self.title))
        return self.title

    @name.setter
    def name(self, name):
        print("Setting new title as: {}".format(name))
        self.title = name

    @name.deleter
    def name(self):
        print("Deleting current title: {}".format(self.title))
        del self.title

    @property
    def duedate(self):
        """'Due' property of Pad"""
        yr = self.due.year
        mt = self.due.month
        day = self.due.day
        print("Getting due date of Pad: {}-{}-{}".format(day, mt, yr))
        return self.due

    @duedate.setter
    def duedate(self, tpldate):
        yr, mt, day = tpldate
        print("Setting new due date of Pad for: {}-{}-{}".format(day, mt, yr))
        self.due = dt.datetime(yr, mt, day)

    @duedate.deleter
    def duedate(self):
        del self.due

    @property
    def tasks(self):
        """Handles aspects of tasks in Pad"""
        print("Here are the tasks of this Pad: {}".format(self.todo))
        return self.todo

    @tasks.setter
    def tasks(self, newtask):
        try:
            key, task = newtask
        except ValueError:
            raise ValueError("Enter a tuple with task id and task")
        else:
            self.todo[key] = task
            self.tot_tasks += 1

    @property
    def checkid(self):
        """Handles checking for ids; debugging purpose"""
        print("Here are the ids of all Pad objects: {}".format(self._ids))

# Adding object to a dict works and can call stuff by dict[ind].foo


class Todo:
    """Object that will contain all aspects of a task such as the status of the task, the details, date due/time left"""

    def __init__(self, name):
        self._codes = {'o': 'Incomplete', '-': 'In Progress', 'x': 'Complete'}
        self.code = 'o'        # Represents status of a task, whether it is incomplete, in progress or completed (o/-/x)
        self.detail = name
        self.due = None
        self.timeleft = None

    def __repr__(self):
        return "{} | {} | {}".format(self._codes[self.code], self.detail, self.due)

    @property
    def status(self):
        """'Status' property of a task"""
        print("Current status: {}".format(self._codes[self.code]))
        return self.code

    @status.setter
    def status(self, newstat):
        if newstat not in self._codes:
            raise KeyError("Not a valid status symbol")

        print("Changing status of task: {}".format(self._codes[newstat]))
        self.code = newstat

    @property
    def task(self):
        print("Task of this object is: {}".format(self.detail))
        return self.detail

    @task.setter
    def task(self, newtask):
        print("Task is now: {}".format(newtask))
        self.detail = newtask

    @task.deleter
    def task(self):
        print("Deleting task: {}".format(self.detail))
        del self.detail

    @property
    def taskdue(self):
        """Due date property of a task"""
        yr = self.due.year
        mt = self.due.month
        day = self.due.day
        print("This task is due {}-{}-{}".format(day, mt, yr))
        return self.due

    @taskdue.setter
    def taskdue(self, newdue):
        yr, mt, day = newdue
        print("Setting new due date for {}-{}-{}".format(day, mt, yr))
        self.due = dt.datetime(yr, mt, day)

    @property
    def daysleft(self):
        """Time left property of a task"""
        print("Time left for this task is {} days".format(self.due.days))
        return self.due.days

    def calctimeleft(self):
        today = dt.datetime.today()
        self.due = self.due - today

def main():
    # print("Making a Pad object with 'Work' as title.")
    # p = Pad("Work")
    # p.name = "Project"
    # print(p.name)
    # p.due = "May"
    # print(p.due)
    # p.tasks = ((1, 'Eat'))
    # p.tasks
    # print(type(p.todo))
    # print(p.tot_tasks)

    # t = Todo()
    # t.status
    # t.status = '-'
    # # t.status = 'c'
    # t.task
    # t.task = "sleep"

    # print(t)  # Testing __repr__ of Todo obj

    print("Now testing combining Pad and Todo object")
    proj1 = Pad("Prodo project", 'px1')  # Creat Pad with task related to prodo python proj
    proj1.name                    # Retrieves name as sanity check
    proj1.duedate = (2018, 6, 7)  # Sets due date to June 7th 2018
    proj1.duedate
    proj1.checkid

    time = Todo("Implement time keeping aspect of Pad and Todo")  # Create a Todo object that holds a task and its status
    time.task                                                     # Name of task sanity check
    time.status                                                   # Status sanity check
    time.taskdue = (2018, 6, 7)
    time.calctimeleft()
    time.daysleft

    proj1.tasks = (1, time)   # adds the time instance of Todo into the Pad dictionary of tasks
    proj1.tasks                 # Checks to see how it is represented

    # proj2 = Pad("I am a long title length")   # len = 24
    # proj2.name

    # projx = Pad("not unique id", 'px1')
    # projx.checkidS
    projy = Pad("Unique pad with unique id", 'py1')
    projy.checkid

main()