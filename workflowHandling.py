def addWorkflow():
    pass

def archiveWorkflow(workflow):
    if workflow.archivable == True:
        print"Archived the Workflow",workflow.name

def deleteWorkflow(workflow):
    while True:
        user_input = raw_input("Do you really want to delete the workflow? (y/n)")
        if input == 'y':
            pass#delete it
            print"deleted."
            break
        elif input == 'n':
            print"aborted."
            break

def mergeWorkflow(src_workflow, dest_workflow):
    pass

def renameWorkflow(workflow, new name):

def resolveFlaw():
    pass

def reportIssue():
    pass

def clarifyArgument():
    pass

def initiateDiscussion():
    pass
