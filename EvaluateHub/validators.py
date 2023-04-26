def create_issue_if_not_empty (value,IssueManager,IssueManagerObject):
    if value.get('issue') != "" :
        IssueManager.objects.create(department= IssueManagerObject, **value)
