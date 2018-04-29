# Prototype ToDo app for personal use
# By: Carlos Cruz Ramos
# Ver. 0.01

class Pad():
  """Object that contains data structure in which tasks are stored to form a complete ToDo list
  Takes in a string as a name and optionally a date to server as a deadline for the whole tasks incuded in this list"""
  
  def __new__(cls, title):
  	if len(title) > 20:
  		return super(Pad, cls).__new__(cls)
  	else:
  		return ValueError

  def __init__(self, title):
    self.title = title    # Later, check for a certain length limit and also if a string was entered
    self.due = None
    self.todo = {}        # Dictionary that will contain task index with its corresponding Todo object            
    self.tot_tasks = 0    # Keeps track of the total number of task in a Pad

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
    """'Due' propert of Pad"""
    print("Getting due date of Pad: {}".format(self.due))
    return self.due

  @duedate.setter
  def duedate(self, date):
    print("Setting new due date of Pad for: {}".format(date))
    self.due = date

  @duedate.deleter
  def duedate(self):
    del self.duedate

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

# Adding object to a dict works and can call stuff by dict[ind].foo

class Todo():
  """Object that will contain all aspects of a task such as the status of the task, the details, date due/time left"""

  def __init__(self, name):
    self._codes = {'o': 'Incomplete', '-': 'In Progress', 'x': 'Complete'}
    self.code = 'o'        # Represents status of a task, whether it is incomplete, in progress or completed (o/-/x)
    self.detail = name
    self.due = None

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

  def changeDue(self, newdate):
    # Ability to change the deadline of the task.   
    pass

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
  proj1 = Pad("Prodo project")  # Creat Pad with task related to prodo python proj
  proj1.name                    # Retrieves name as sanity check
  proj1.duedate = "May"         # Sets due date to May (in future will allow due date set at creation)

  time = Todo("Implement time keeping aspect of Pad and Todo")  # Create a Todo object that holds a task and its status
  time.task                                                     # Name of task sanity check
  time.status                                                   # Status sanity check

  proj1.tasks = ((1, time))   # adds the time instance of Todo into the Pad dictionary of tasks
  proj1.tasks                 # Checks to see how it is represented

main()