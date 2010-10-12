# ===========================================================================
# eXe
# Copyright 2004-2006, University of Auckland
# Copyright 2006-2007 eXe Project, New Zealand Tertiary Education Commission
# Copyright 2010 Ivo Benner, Univerity of Applied Sciences Giessen
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
The EStudyPage is responsible for exporting/uploading content to the eStudy platform
"""

import logging
from twisted.web.resource      import Resource
from exe.webui                 import common
from exe.webui.renderable      import RenderableResource

log = logging.getLogger(__name__)


class EStudyPage(RenderableResource):
    """
    The EStudyPage is responsible for exporting/uploading content to the eStudy platform
    """
    name = 'preferences'

    def __init__(self, parent):
        """
        Initialize
        """
        RenderableResource.__init__(self, parent)
        
    def getChild(self, name, request):
        """
        Try and find the child for the name given
        """
        if name == "":
            return self
        else:
            return Resource.getChild(self, name, request)


    def render_GET(self, request):
        """Render the page"""
        log.debug("render_GET")
        
        this_package = None

        
        # Rendering
        html  = common.docType()
        html += u"<html xmlns=\"http://www.w3.org/1999/xhtml\">\n"
        html += u"<head>\n"
        html += u"<style type=\"text/css\">\n"
        html += u"@import url(/css/exe.css);\n"
        html += u'@import url(/style/base.css);\n'
        html += u"@import url(/style/standardwhite/content.css);\n"
        html += u"@import url(/css/estudylogin.css);\n"
        html += u"</style>\n"
        html += u"<title> eStudy - Login</title>\n"
        html += u"<meta http-equiv=\"content-type\" content=\"text/html; "
        html += u" charset=UTF-8\"></meta>\n";
        html += u"</head>\n"
        html += u"<body>\n"
        html += u"<div id=\"estudylogo\"></div> \n"
        html += u"<div id=\"main\"> \n"
        html += u"<form method=\"post\" action=\"\" "
        html += u"id=\"contentForm\" >"
        #html += u"Username:<br/>"
        html += common.formField('textInput', this_package, _(u"Username"),
                                 'username')
        html += common.formField('password', this_package, _(u"Password"),
                                 'password')
        html += u"<div id=\"editorButtons\"> \n"     
        html += u"<br/>" 
        html += common.button("ok", _("OK"), enabled=True,
                _class="button",)
        html += common.button("cancel", _("Cancel"), enabled=True,
                _class="button", onClick="window.close()")
        html += u"</div>\n"
        html += u"</div>\n"
        html += u"<br/></form>\n"
        html += u"</body>\n"
        html += u"</html>\n"
        return html.encode('utf8')


    def render_POST(self, request):
        """
        function replaced by nevow_clientToServerEvent to avoid POST message
        """
        log.debug("render_POST " + repr(request.args))
        
        # should not be invoked, but if it is... refresh
        html  = common.docType()
        html += u"<html xmlns=\"http://www.w3.org/1999/xhtml\">\n"
        html += u"<head></head>\n"
        html += u"<body onload=\"opener.location.reload(); "
        html += u"self.close();\"></body>\n"
        html += u"</html>\n"
        return html.encode('utf8')
