import re

import sublime_plugin


# https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
def _convert_camelcase_to_underscore(word):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', word)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


# https://stackoverflow.com/questions/4303492/how-can-i-simplify-this-conversion-from-underscore-to-camelcase-in-python
def _convert_underscore_to_camelcase(word):
    r = []
    for x in word.split('_'):
        if len(x) > 0:
            if len(x) > 1:
                r.append(x[0].upper() + x[1:])
            else:
                r.append(x[0].upper())

    return ''.join(r)


class RefactorTestCodingStandardFixerCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.run_command('refactor_test_class_underscore_to_camelcase')
        self.view.run_command('refactor_test_function_camelcase_to_underscore')


class RefactorTestClassUnderscoreToCamelcaseCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        done = False
        while not done:
            done = True
            for region in self.view.find_by_selector('entity.name.class'):
                class_name = self.view.substr(region)
                if class_name.startswith('Test'):
                    new_class_name = _convert_underscore_to_camelcase(class_name)
                    if new_class_name != class_name:
                        print("Refactor: test class '{}' -> '{}'".format(class_name, new_class_name))
                        self.view.replace(edit, region, new_class_name)
                        done = False


class RefactorTestFunctionCamelcaseToUnderscoreCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        done = False
        while not done:
            done = True
            for region in self.view.find_by_selector('entity.name.function'):
                function_name = self.view.substr(region)
                if function_name.startswith('test'):
                    new_function_name = _convert_camelcase_to_underscore(function_name)
                    if new_function_name != function_name:
                        print("Refactor: test function '{}' -> '{}'".format(function_name, new_function_name))
                        self.view.replace(edit, region, new_function_name)
                        done = False
