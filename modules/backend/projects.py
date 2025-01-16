import os
from modules.tempsettings import TempSettings

def getProjects():
    path = TempSettings.get("path")
    folderProjects = os.path.join(path, "projects")

    projects = [f.replace(".py", "") for f in os.listdir(folderProjects) if (f.endswith(".py") and f != "base.py")]

    TempSettings.set("folderProjects", folderProjects)
    TempSettings.set("projects", projects)
    
    return projects