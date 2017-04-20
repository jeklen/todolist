import  os.path
check = os.path.exists(r'C:\Users\zhang\Desktop\my-python\toDoList\toDoList-4\myconfig.cfg')
#if check == True:
#    print 'ok'
#else:
#    print 'not ok'
print check
path = os.path.dirname(__file__)
print path