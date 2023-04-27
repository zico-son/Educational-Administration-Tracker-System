


def create_issue_if_not_empty (value,IssueManager,IssueManagerObject):
    if value.get('issue') != "" :
        IssueManager.objects.create(department= IssueManagerObject, **value)

def create_response_if_not_empty (value,ResponseManager,ResponseManagerObject):
    if value.get('response') != "" :
        ResponseManager.objects.create(department= ResponseManagerObject, **value)

def update_response_if_not_empty (value,ResponseManager,ResponseManagerObject):
    if value.get('response') != "" :
        ResponseManager.objects.update(department= ResponseManagerObject, **value)


def permission_exception_handler(request, role):
    try:
            return bool(request.user.role == role)
    except:
            return False