# COLOR SCHEME TEST "GruvboxDarkVim.sublime-color-scheme" "Python" # flake8: noqa

    #     whitespace
# ^ fg=#ebdbb2 bg=#282828 fs=

import os
# ^^^^ fg=#8ec07c fs=
#      ^^ fg=#ebdbb2 fs=

from path import os
# ^ fg=#8ec07c fs= build>=3154
#           ^ fg=#8ec07c fs= build>=3154

__all__
# ^^^^^ fg=#8ec07c fs=

__file__
# ^^^^^^ fg=#8ec07c fs=

__missing__
# ^^^^^^^^^ fg=#fe8019 fs= build>=3127

__bool__
# ^^^^^^ fg=#fe8019 fs= build>=3127

__debug__
# ^^^^^^^ fg=#d3869b fs= build>=3127

abc = 'x'
# ^ fg=#ebdbb2 fs=
#   ^ fg=#fe8019 fs=
#     ^^^ fg=#b8bb26 fs=

BC = 'x'
#^ fg=#d3869b fs= build>=3180

x = ABC
#   ^ fg=#d3869b fs= build>=3180

x = "_\x00_\xaa_\'_%s_"
#   ^^ fg=#b8bb26 fs=
#     ^^^^ fg=#fe8019 fs=
#         ^ fg=#b8bb26 fs=
#          ^^^^ fg=#fe8019 fs=
#              ^ fg=#b8bb26 fs=
#               ^^ fg=#fe8019 fs=
#                 ^ fg=#b8bb26 fs=
#                  ^^ fg=#d3869b fs=
#                    ^^ fg=#b8bb26 fs=

x = '_\m_\\m_'
#   ^^ fg=#b8bb26 fs=
#     ^^ fg=#ebdbb2 bg=#d3869b build>=3154
#       ^ fg=#b8bb26 fs=
#        ^^ fg=#fe8019 fs=
#          ^^^ fg=#b8bb26 fs=

x = b'x'
#   ^ fg=#83a598 fs=italic
#    ^^^ fg=#b8bb26 fs=

'ab'.upper()
# ^^ fg=#b8bb26 fs=
#   ^ fg=#ebdbb2 fs=
#    ^^^^^ fg=#ebdbb2 fs=
#         ^^ fg=#83a598 fs=

x = '|'.join(sorted(x))
#   ^^^ fg=#b8bb26 fs=
#      ^ fg=#ebdbb2 fs=
#       ^^^^ fg=#ebdbb2 fs=
#           ^ fg=#83a598 fs=
#            ^^^^^^ fg=#b8bb26 fs=
#                  ^ fg=#83a598 fs=
#                   ^ fg=#ebdbb2 fs=
#                    ^ fg=#83a598 fs=
#                     ^ fg=#83a598 fs=

x = f"{x}"
#   ^ fg=#83a598 fs=italic
#    ^ fg=#b8bb26 fs=
#     ^ fg=#83a598 fs=
#      ^ fg=#ebdbb2 fs=
#       ^ fg=#83a598 fs=
#        ^ fg=#b8bb26 fs=

def x():
# ^ fg=#fb4934 fs=
#   ^ fg=#ebdbb2 fs=
#    ^^^ fg=#83a598 fs=
    pass
#   ^ fg=#fb4934 fs=

def x():
    """x"""
#   ^^^^^^^ fg=#928374 fs=italic
    pass

def x():
    """
#   ^^^ fg=#928374 fs=italic
    x
#   ^ fg=#928374 fs=italic
    """
#   ^^^ fg=#928374 fs=italic
#   pass

def x():

    abc = 'x'
#   ^ fg=#ebdbb2 fs=
#       ^ fg=#fe8019 fs=
#         ^^^ fg=#b8bb26 fs=

    call(x, 'y', True, False)
#     ^^ fg=#ebdbb2 fs=
#       ^ fg=#83a598 fs=
#         ^ fg=#ebdbb2 fs=
#           ^^^ fg=#b8bb26 fs=
#              ^ fg=#ebdbb2 fs=
#                ^^^^ fg=#d3869b fs=
#                    ^ fg=#ebdbb2 fs=
#                      ^^^^^ fg=#d3869b fs=
#                           ^ fg=#83a598 fs=

    call(x=y)
#     ^^ fg=#ebdbb2 fs=
#       ^ fg=#83a598 fs=
#        ^ fg=#ebdbb2 fs=
#         ^ fg=#fe8019 fs=
#          ^ fg=#ebdbb2 fs=
#           ^ fg=#83a598 fs=

    if isinstance(var, list):
#   ^^ fg=#fb4934 fs=
#      ^^^^^^^^^^ fg=#b8bb26 fs=
#                ^ fg=#83a598 fs=
#                 ^^^^ fg=#ebdbb2 fs=
#                      ^^^^ fg=#b8bb26 fs=
#                          ^^ fg=#83a598 fs=
        arr = []
#         ^ fg=#ebdbb2 fs=
#           ^ fg=#fe8019 fs=
#             ^^ fg=#83a598 fs=
        arr.append('x')
#         ^^ fg=#ebdbb2 fs=
#           ^^^^^^ fg=#ebdbb2 fs=
#                 ^ fg=#83a598 fs=
#                  ^^^ fg=#b8bb26 fs=
#                     ^ fg=#83a598 fs=
        arr.sort()
#         ^^ fg=#ebdbb2 fs=
#           ^^^^ fg=#ebdbb2 fs=
#               ^^ fg=#83a598 fs=

        if len(x):

            if len(x):


        if len(x):
#       ^^ fg=#fb4934 fs=
#          ^^^ fg=#b8bb26 fs=
#             ^ fg=#83a598 fs=
#              ^ fg=#ebdbb2 fs=
#               ^^ fg=#83a598 fs=
            print('Hi')
#             ^ fg=#b8bb26 fs=
#                ^ fg=#83a598 fs=
#                 ^^^^ fg=#b8bb26 fs=
#                     ^ fg=#83a598 fs=

    fmt = 'x={}'.format(s['y'])
#     ^ fg=#ebdbb2 fs=
#       ^ fg=#fe8019 fs=
#         ^^^ fg=#b8bb26 fs=
#            ^^ fg=#d3869b fs=
#              ^ fg=#b8bb26 fs=
#               ^ fg=#ebdbb2 fs=
#                ^^^^^^ fg=#ebdbb2 fs=
#                      ^ fg=#83a598 fs=
#                       ^  fg=#ebdbb2 fs=
#                        ^  fg=#83a598 fs=
#                         ^^^ fg=#b8bb26 fs=
#                            ^^ fg=#83a598 fs=

    x = u'x%s' % y
#       ^ fg=#83a598 fs=italic
#        ^^ fg=#b8bb26 fs=
#          ^^ fg=#d3869b fs=
#            ^ fg=#b8bb26 fs=
#              ^ fg=#fe8019 fs=
#                ^ fg=#ebdbb2 fs=

    x = "x {y} z".format(y=z)
#       ^^^ fg=#b8bb26 fs=
#          ^^^ fg=#d3869b fs=
#             ^^^ fg=#b8bb26 fs=
#                ^ fg=#ebdbb2 fs=
#                 ^^^^^^ fg=#ebdbb2 fs=
#                       ^ fg=#83a598 fs=
#                        ^ fg=#ebdbb2 fs=
#                         ^ fg=#fe8019 fs=
#                          ^ fg=#ebdbb2 fs=
#                           ^ fg=#83a598 fs=

    x = re.match('^.+\\.x$')
#       ^^^ fg=#ebdbb2 fs=
#          ^^^^^ fg=#ebdbb2 fs=
#               ^ fg=#83a598 fs=
#                ^^^^ fg=#b8bb26 fs=
#                    ^^ fg=#fe8019 fs= build>=3154
#                      ^^^^ fg=#b8bb26 fs=
#                          ^ fg=#83a598 fs=

@requires_x
# ^ fg=#b8bb26 fs=bold
def f_name(arg1='', arg2=0):
# ^ fg=#fb4934 fs=
#   ^ fg=#ebdbb2 fs=
#          ^ fg=#ebdbb2 fs=
#              ^ fg=#fe8019 fs=
#               ^^ fg=#b8bb26 fs=
#                 ^ fg=#ebdbb2 fs=
#                   ^ fg=#ebdbb2 fs=
#                       ^ fg=#fe8019 fs=
#                        ^ fg=#d3869b fs=

    if a > b: # x
#   ^^ fg=#fb4934 fs=
#      ^ fg=#ebdbb2 fs=
#        ^ fg=#fb4934 fs=
#          ^ fg=#ebdbb2 fs=
#           ^ fg=#83a598 fs=
#             ^^^ fg=#928374 fs=italic
        print 'a\'b'
#         ^ fg=#fb4934 fs=
#             ^^ fg=#b8bb26 fs=
#               ^^ fg=#fe8019 fs=
#                 ^^ fg=#b8bb26 fs=

    abc = d[0]
#     ^ fg=#ebdbb2 fs=
#       ^ fg=#fe8019 fs=
#         ^ fg=#ebdbb2 fs=
#          ^ fg=#83a598 fs=
#           ^ fg=#d3869b fs=
#            ^ fg=#83a598 fs=

    abc.d(e)
#     ^^ fg=#ebdbb2 fs=
#       ^ fg=#ebdbb2 fs=
#        ^ fg=#83a598 fs=
#         ^  fg=#ebdbb2 fs=
#          ^  fg=#83a598 fs=

    return None
#     ^ fg=#fb4934 fs=
#          ^ fg=#fabd2f fs=

class X():
# ^ fg=#fb4934 fs=
#     ^ fg=#ebdbb2 fs=
#      ^^^ fg=#83a598 fs=
    pass
#   ^ fg=#fb4934 fs=


class X(Y):
#   ^ fg=#fb4934 fs=
#     ^ fg=#ebdbb2 fs=
#      ^ fg=#83a598 fs=
#       ^ fg=#ebdbb2 fs=
#        ^^ fg=#83a598 fs=

    def __init__(self):
#     ^ fg=#fb4934 fs=
#       ^^^^^^^^ fg=#fe8019 fs=
#               ^ fg=#83a598 fs=
#                ^^^^ fg=#ebdbb2 fs=
#                    ^^ fg=#83a598 fs=
        self.x = 123
#         ^ fg=#fabd2f fs=
#           ^ fg=#ebdbb2 fs=
#            ^ fg=#ebdbb2 fs=
#              ^ fg=#fe8019 fs=
#                ^^^ fg=#d3869b fs=

        self.x()
#         ^ fg=#fabd2f fs=
#           ^ fg=#ebdbb2 fs=
#            ^ fg=#ebdbb2 fs=
#             ^^ fg=#83a598 fs=

        self.x.y()
#         ^ fg=#fabd2f fs=
#           ^ fg=#ebdbb2 fs=
#            ^ fg=#ebdbb2 fs=
#             ^ fg=#ebdbb2 fs=
#              ^ fg=#ebdbb2 fs=
#               ^^ fg=#83a598 fs=

        abc(y)
#         ^ fg=#ebdbb2 fs=
#          ^ fg=#83a598 fs=
#           ^  fg=#ebdbb2 fs=
#            ^  fg=#83a598 fs=

    def __str__(self)
#     ^ fg=#fb4934 fs=
#       ^^^^^^^ fg=#fe8019 fs=
#              ^ fg=#83a598 fs=
#               ^^^^ fg=#ebdbb2 fs=
#                   ^ fg=#83a598 fs=
        return 'x'

    def z(self, a, b):
#     ^ fg=#fb4934 fs=
#       ^ fg=#ebdbb2 fs=
#        ^ fg=#83a598 fs=
#         ^^^^ fg=#ebdbb2 fs=
#             ^ fg=#ebdbb2 fs=
#               ^ fg=#ebdbb2 fs=
#                ^ fg=#ebdbb2 fs=
#                  ^ fg=#ebdbb2 fs=
#                   ^^ fg=#83a598 fs=
        if a == b:
#       ^^ fg=#fb4934 fs=
#          ^ fg=#ebdbb2 fs=
#            ^^ fg=#fb4934 fs=
#               ^ fg=#ebdbb2 fs=
#                ^ fg=#83a598 fs=
            if fcall(a, b):
#           ^^ fg=#fb4934 fs=
#              ^^^^^ fg=#ebdbb2 fs=
#                   ^ fg=#83a598 fs=
#                    ^^ fg=#ebdbb2 fs=
#                       ^ fg=#ebdbb2 fs=
#                        ^^ fg=#83a598 fs=
                return True
#                    ^ fg=#fb4934 fs=
#                      ^^^^ fg=#d3869b fs=

        return None
#            ^ fg=#fb4934 fs=
#              ^^^^ fg=#fabd2f fs=

    @zyx
#   ^ fg=#83a598 fs= build>=4168
#    ^^^ fg=#b8bb26 fs=bold build>=3127
    def x(self):
        pass


>>> msg = '''interpreter
#^ fg=#fe8019 fs=
# ^ fg=#fb4934 fs=
#   ^^^ fg=#ebdbb2 fs=
#       ^ fg=#fe8019 fs=
#         ^^^^^^^^^^^^^^ fg=#b8bb26 fs=
... prompt'''
# ^^^^^^^^^^^ fg=#b8bb26 fs=
