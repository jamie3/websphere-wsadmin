# websphere-wsadmin
Example on how to deploy an EAR to WebSphere Application Server using wsadmin

```
wsadmin.bat -lang jython -f deploy-was.py <Application Name> <EAR File>
```

Note: The application name must not contain spaces

```
wsadmin.bat -lang jython -f deploy-was.py "MyApplication" "C:/myApplication.ear"
```
