# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import datetime
import os
import requests
from bs4 import BeautifulSoup as BS

class Wikipedia(object):
    """Gets knowledge from Wikipedia."""

    def __init__(self, locale='en'):
        self.host = "https://{}.wikipedia.org/".format(locale)

    def on_this_day(self):
        """Returns a list of event titles (as unicode string) today."""
        now = datetime.datetime.now()
        # Returns the full English representation of month
        month = now.strftime("%B")
        path = "wiki/" + month + "_" + str(now.day)
        url = os.path.join(self.host, path)
        # Makes the request and gets back the HTML
        res = requests.get(url)
        soup = BS(res.text)
        # There are Events, Births, Deaths, and Holidays and observances.
        # They are under unordered list <ul> but without any id so we must
        # assume the order index 1,2,3,4 belong to each.
        #TODO: Let's only do Events.
        uls = soup.find_all("ul")
        events = uls[1]
        summary = [li.text for li in events.findAll("li")]
        return summary
