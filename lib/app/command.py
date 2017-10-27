class Command:
    def __init__(self, type_c, action, name, id):
        """
        type: Project, Task, Note, File
        action: add, del, start, end
        name: 'name'
        id: 'id'
        """
        self.type = type_c;
        self.action = action;
        
    def __call__(self):
        if(self.type == 'Project'):
            p = Project(self.name)
            p.action()
        if(self.type == 'Task')
            t = Task(self.name)
            t.action()
