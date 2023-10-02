import sublime_plugin


class FoldAllCssClasses(sublime_plugin.TextCommand):

    def run(self, edit):
        selector = "text.html.vue meta.tag meta.attribute-with-value.class.html meta.string.html string.quoted.double.html - punctuation"  # noqa: E501
        selectors = self.view.find_by_selector(selector)
        self.view.fold(selectors)
