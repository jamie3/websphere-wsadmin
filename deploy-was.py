import sys
import time

cell = AdminControl.getCell()
print "Cell = " + cell

appname = sys.argv[0]
print "App Name = " + appname

earfile = sys.argv[1]

appId = AdminConfig.getid("/Deployment:" + appname + "/")

if len(appId) > 0:
	print "Uninstalling " + appname
	AdminApp.uninstall(appname)
	AdminConfig.save()

options = '[[.* .* default_host]]'

AdminApp.install(earfile, '-appname "' + appname + '" -cell ' + cell + ' -MapWebModToVH ' + options)
AdminConfig.save()

print "Waiting for application to be ready"

isAppReady = AdminApp.isAppReady(appname)
count = 0


while (isAppReady == "false" and count < 60):
	time.sleep(1)
	isAppReady = AdminApp.isAppReady(appname)
	count = count + 1

isAppReady = AdminApp.isAppReady(appname)

if (isAppReady == "false"):
	print "ERROR: Application is not ready"
	sys.exit(1)


appManager = AdminControl.queryNames('cell=' + cell + ',type=ApplicationManager,process=server1,*')
print appManager

print "Starting application"
AdminControl.invoke(appManager, 'startApplication', '["' + appname + '"]')

print "Application is ready and started"
