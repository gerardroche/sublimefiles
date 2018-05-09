import sublime_plugin


def profile_text():
    output = ""

    # TODO This is a mess.

    # Mean
    output += "Top 5 (Mean)\n"
    output += "------------\n"
    items = {}
    for event in sublime_plugin.profile.keys():
        for name, summary in sublime_plugin.profile[event].items():
            items['{0:6f}'.format(summary.sum / summary.count)] = {'name': name, 'event': event, 'mean': '{0:6f}'.format(summary.sum / summary.count)}
    count = 0
    for _, item in sorted(items.items(), reverse=True):
        output += "{0:<50} {1:<50} {2}\n".format(item['name'], item['event'], item['mean'])
        count += 1
        if count >= 5:
            break

    output += "\n"

    # Max
    output += "Top 5 (Max)\n"
    output += "-----------\n"
    items = {}
    for event in sublime_plugin.profile.keys():
        for name, summary in sublime_plugin.profile[event].items():
            items['{0:6f}'.format(summary.max)] = {'name': name, 'event': event, 'max': '{0:6f}'.format(summary.max)}
    count = 0
    for _, item in sorted(items.items(), reverse=True):
        output += "{0:<50} {1:<50} {2}\n".format(item['name'], item['event'], item['max'])
        count += 1
        if count >= 5:
            break
    output += "\n"

    # Hits
    output += "Top 5 (Hits)\n"
    output += "-----------\n"
    items = {}
    for event in sublime_plugin.profile.keys():
        for name, summary in sublime_plugin.profile[event].items():
            items[summary.count] = {'name': name, 'event': event, 'count': summary.count}
    count = 0
    for _, item in sorted(items.items(), reverse=True):
        output += "{0:<50} {1:<50} {2}\n".format(item['name'], item['event'], item['count'])
        count += 1
        if count >= 5:
            break
    output += "\n"

    # Table of Events
    output += "{0:<48} {1}       {2}        {3}      {4:>5}".format('', 'mean', 'max', 'total', 'hits')
    output += "\n"
    output += "{0:<48} {1}       {2}        {3}      {4:>5}".format('', '----', '---', '-----', '----')
    output += "\n"
    for event in sorted(sublime_plugin.profile.keys()):
        output += "{0}:\n".format(event)
        for name, summary in sublime_plugin.profile[event].items():
            output += "    {0:<45}".format(name)
            output += "{0:.6f}s  {1:.6f}s  {2:.6f}s  {3:>5}".format(
                summary.sum / summary.count, summary.max, summary.sum, summary.count)
            output += "\n"
        output += "\n"

    return output


class ProfilePluginsCommand(sublime_plugin.WindowCommand):
    def run_(self, edit_token, args):
        output = "This list shows how much time each plugin has taken to respond to each event:\n\n"
        output += profile_text()

        v = self.window.new_file()
        v.set_scratch(True)
        v.set_name('Plugin Event Profile')
        edit = v.begin_edit(edit_token, "")
        v.insert(edit, 0, output)
        v.end_edit(edit)
