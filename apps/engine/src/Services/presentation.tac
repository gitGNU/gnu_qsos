from twisted.application import service, internet
from nevow import appserver
from Services import homepage
from Engine import core
import os


application = service.Application ( "QSOS Engine" )
port        = 8080
repository  = '/absolute/path/to/repository'
res         = homepage.MainPage(repository)
site        = appserver.NevowSite ( res )
webService  = internet.TCPServer ( port, site )
webService.setServiceParent ( application )
