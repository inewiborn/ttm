class ProjectRepository:
    def __init__(self, db):
        self.db = db
        self.project_list = [
            {
                'id' : 1,
                'name' : 'Project 1',
                'dir' : ''
            },
            {
                'id' : 1,
                'name' : 'Project 2',
                'dir' : ''
            },
        ]

    def list(self):
        return self.project_list

    def add_project(project):
        self.project_list.append(
            {
                'id' : project.id(),
                'name' : project.name(),
                'dir' : project.dir()
            }
        )

    def new_project(name, project_dir):
        p = Project(name, project_dir)
        id = db.add_project(p)
        p.id = id
        self.add_poject(p)

