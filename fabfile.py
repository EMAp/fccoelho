from fabric.api import *


def make():
    local('make html')
    
def deploy():
    local('git add *')
#    local('mv -f html/* .')
    local('git commit -a -m "updated"')
    local('git push')
    
