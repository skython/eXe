# ===========================================================================
# eXe
# Copyright 2004-2005, University of Auckland
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
This module is for the common HTML used in all webpages.
"""

import logging
import gettext

log = logging.getLogger(__name__)
_   = gettext.gettext


def header():
    # TODO we need to split out the Javascript in here!!!
    """Generates the common header XHTML"""
    html  = "<?xml version=\"1.0\" encoding=\"iso-8859-1\"?>\n"
    html += "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" "
    html += " \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n"
    html += "<html xmlns=\"http://www.w3.org/1999/xhtml\">\n"
    html += "<head>\n"
    html += "<style type=\"text/css\">\n"
    html += "@import url(/css/main.css);"
    html += "@import url(/css/controlpanel.css);"
    html += "@import url(/css/editing.css);</style>\n"
    html += "<script language=\"JavaScript\" src=\"/scripts/common.js\">"
    html += "</script>\n"
    html += "<script language=\"JavaScript\" src=\"/scripts/control_panel.js\">"
    html += "</script>\n"
    html += "<script language=\"JavaScript\" src=\"/scripts/fckeditor.js\">"
    html += "</script>\n"
    html += "<script language=\"JavaScript\" src=\"/scripts/libot_drag.js\">"
    html += "</script>\n" 
    html += "<title>"+_("eXe")+"</title>\n"
    html += "<meta http-equiv=\"content-type\" content=\"text/html; "
    html += " charset=UTF-8\"></meta>\n";
    html += "</head>\n"
    return html

def banner(): 
    """Generates the common page banner XHTML"""
    html  = "<body onLoad=\"initTabs();\">\n"
    html += "<div id=\"main\">\n"
    return html

def footer():
    """Generates the common page footer XHTML"""
    html  = "</div></body></html>\n"
    return html
    
def hiddenField(name, value=""):
    """Adds a hidden field to a form"""
    html  = "<input type=\"hidden\" name=\"%s\" " % name
    html += "value=\"%s\" />\n" % value
    return html

def textInput(name, value=""):
    """Adds a text input to a form"""
    html  = "<input type=\"text\" name=\"%s\" " % name
    html += "value=\"%s\"" % value
    html += " size=\"40\" />\n" 
    return html

def textArea(name, value=""):
    """Adds a text area to a form"""
    html  = "<fieldset class=\"fieldset\"><textarea name=\"%s\" " % name
    html += "class=\"textfield\">%s" % value
    html += "</textarea></fieldset><br />" 
    return html

def richTextArea(name, value="", width="100%", height=100):
    html  = "<script type=\"text/javascript\">\n"
    html += "<!--\n"
    html += "    var editor = new FCKeditor('"+name+"', '"
    html += str(width)+"', '"+str(height)+"', 'Armadillo', '"+value+"');\n"
    html += "    editor.BasePath = '/scripts/';\n"
    html += "    editor.Config['CustomConfigurationsPath'] ="
    html += " '/scripts/armadillo.js';\n"
    html += "    editor.Create();\n"
    html += "//-->\n"
    html += "</script>\n"
    return html
        
def submitButton(name, value, enabled=True):
    """Adds a submit button to a form"""
    html  = "<input type=\"submit\" name=\"%s\" " % name
    html += "value=\"%s\" " % value
    if not enabled:
        html += " disabled"
    html += "/>\n"
    return html

def submitLink(action, object_, value, class_=""):
    """
    Adds a link which will trigger the javascript needed to
    post a form with the action and object passed in the args
    """
    html  = "<a "
    if class_ != "":
        html += "class=\""+class_+"\" "
    html += "href=\"#\" onclick=\"submitLink('" + action
    html += "', '" + object_ + "');\" >"
    html += value
    html += "</a>\n"
    return html

def submitImage(action, object_, imageFile, title=""):
    """
    Adds an image link which will trigger the javascript needed to
    post a form with the action and object passed in the args
    """
    html  = "<a "
    if title != "":
        html += "title=\""+title+"\" "
    html += " href=\"#\" onclick=\"submitLink('" + action
    html += "', '" + object_ + "');\" >"
    html += image(imageFile)
    html += "</a>\n"
    return html

def image(imageFile):
    """returns the XHTML for an image"""
    html  = "<img src=\"/images/"+imageFile+"\" "
    html += " align=\"middle\" border=\"0\" />"
    return html

def select(action, object_, options, selection=None):
    """Adds a dropdown selection to a form"""
    html  = "<select onchange=\"submitLink('" + action
    html += "', '" + object_ + "');\" "
    html += "name=\""+action+object_+"\" >"

    for option, value in options:
        if selection == option:
            selected = "selected"
        else:
            selected = ""

        html += " <option value=\""+value+"\""+selected+">"
        html += option
        html += "</option>\n"

    html += "</select>\n"
    return html

def option(name, checked, value):
    """Add a option input"""
    chkStr = ""
    if checked:
        chkStr = "checked"
        
    html  = '<input type = "radio" name = "'+name+'"'
    html += ' value="'+value+'" '
    html += chkStr+' />\n'
    return html
    
# ===========================================================================

if __name__ == "__main__":
    print header()
    print banner()
    print textInput("text")
    print textArea("area")
    print submitButton("ok", "OK")
    print footer()
