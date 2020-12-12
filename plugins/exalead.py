"""
    This file is part of RetrieveEmail
    Copyright (C) 2020 @muneebwanee
    https://github.com/muneebwanee/RetrieveEmail
    
    RetrieveEmail - A tool to retrieve Domain email addresses from Search Engines.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.
"""

#config = None
app_retrieveemail = None


def search(domain, limit):
    url = "http://www.exalead.com/search/web/results/?q=%40{word}&elements_per_page=10&start_index={counter}" 
    app_retrieveemail.init_search(url, domain, limit, 0, 50, 'Exalead')
    app_retrieveemail.process()
    return app_retrieveemail.get_emails()


class Plugin:
    def __init__(self, app, conf):#
        global app_retrieveemail, config
        #config = conf
        app.register_plugin('exalead', {'search': search})
        app_retrieveemail = app
        