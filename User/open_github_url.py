import webbrowser
import re

from sublime_plugin import TextCommand


_GITHUB_USER_REPO_REGEX = re.compile('[a-zA-Z0-9-_]+\/[a-zA-Z0-9-_]+')


class OpenGithubUrlCommand(TextCommand):

    def run(self, edit, event):
        url = self.find_url(event)
        if url:
            webbrowser.open_new_tab(url)

    def is_visible(self, event):
        return self.find_url(event) is not None

    def find_url(self, event):
        pt = self.view.window_to_text((event["x"], event["y"]))
        line = self.view.line(pt)

        line.a = max(line.a, pt - 1024)
        line.b = min(line.b, pt + 1024)

        text = self.view.substr(line).strip()
        if not text:
            return None

        it = _GITHUB_USER_REPO_REGEX.findall(text)
        if it:
            for i in it:
                url = 'https://github.com/' + i
                return url

        return None

    def description(self, event):
        url = self.find_url(event)
        if url:
            if len(url) > 64:
                url = url[0:64] + "..."
            return "Open " + url

        return 'Open Github URL'

    def want_event(self):
        return True
