# ===========================================================================
# eXe
# Copyright 2010 Ivo Benner, University of Applied Sciences in Giessen, Germany
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# ===========================================================================

"""
The EStudyHandler handles all javascript events for all eStudy forms
"""

from exe import globals as G

class EStudyHandler:
    """
    The EStudyHandler handles all javascript events for all eStudy forms
    """
    def sendLoginError(self, client, errormsg):
        script  = u'eStudyWin.document.getElementById("errormsg").style.color = "red"\n'
        script += u'eStudyWin.document.getElementById("errormsg").innerHTML = "%s"' % errormsg
        client.sendScript(script)
        
    def sendLoginNotice(self, client, notice):
        script  = u'eStudyWin.document.getElementById("errormsg").style.color = "black"\n'
        script += u'eStudyWin.document.getElementById("errormsg").innerHTML = "%s"' % notice
        client.sendScript(script)
        
    def handleLogin(self, client, username, password):
        """
        Handles a login request from the eStudy login form
        """
        if username == "Test1" and password == "exe":
            self.sendLoginNotice(client, "Logging in. Please wait!")
            #client.sendScript(u'eStudyWin.location = "about:blank"')
            #client.sendScript(u'eStudyWin.resizeTo(600,600)')
        else:
            self.sendLoginError(client, "Wrong username or password !")
