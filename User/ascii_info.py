import sublime
import sublime_plugin


class AsciiInfoCommand(sublime_plugin.TextCommand):
    """
    http://vimdoc.sourceforge.net/htmldoc/various.html#ga
    """

    def run(self, edit):

        def character_to_notation(character):
            """
            Convert a character to a key notation.
            Uses vim key notation.
            http://vimdoc.sourceforge.net/htmldoc/intro.html#key-notation
            """

            character_notation_map = {
                "\0": "Nul",
                " ": "Space",
                "\t": "Tab",
                "\n": "NL"
            }

            if character in character_notation_map:
                character = character_notation_map[character]

            return "<" + character + ">"

        for region in self.view.sel():

            c_str = self.view.substr(region.begin())
            c_ord = ord(c_str)
            c_hex = hex(c_ord)
            c_oct = oct(c_ord)
            c_not = self.character_to_notation(c_str)

            msg_template = "%7s %3s,  Hex %4s,  Octal %5s"

            return sublime.status_message(msg_template % (c_not, c_ord, c_hex, c_oct))
