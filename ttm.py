# -*- coding: utf-8 -*-
import sys
from lib.orm.project_repository import *
from lib.model.project import *
from lib.model.task import *
from lib.app.config import *

c = Config(sys.path[0] + '/config.json')
c.db()
c.port()
p = Project()
p.name()
pr = ProjectRepository('db_object')
pl = pr.list()

for p in pl:
    print(p['name'])
