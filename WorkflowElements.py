class Workflow:
    def __init__(self, workflowname):
        archivable = True
        name = workflowname
        issues = []
        arguments = []

    def archive(self):#add something like dest_dir and/or even more + optional arguments ...
        if workflow.archivable == True:
            print"Archived the Workflow",workflow.name

    def delete(self):#needed?
        while True:
            user_input = raw_input("Do you really want to delete the workflow? (y/n)")
            if input == 'y':
                pass#delete it
                print"deleted."
                break
            elif input == 'n':
                print"aborted."
                break

    def merge(self, dest_workflow):
        pass

    def rename(self, new_name):
        pass

    def resolve_issue(self, issue):
        pass

    def report_issue(self, issue):
        pass

    def clarify_argument(self, argument):
        pass

    def initiate_argument(self, argument):
        pass


class Issue:
    def __init__(self):
        pass

    def delete():
        pass


class Argument:
    def __init__(self):
        pass

    def delete():
        pass
