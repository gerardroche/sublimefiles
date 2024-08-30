# COLOR SCHEME TEST "GruvboxDarkVim.sublime-color-scheme" SKIP IF NOT "Bash"

set -e
# ^ fg=#fb4934 fs=
#   ^^ fg=#fb4934 fs=

unset CDPATH
# ^ fg=#fb4934 fs=
#     ^ fg=#ebdbb2 fs=

abc="y"
# ^ fg=#ebdbb2 fs=
#  ^ fg=#fe8019 fs=
#   ^^^ fg=#b8bb26 fs=

x="$y"
# ^ fg=#b8bb26 fs=
#  ^ fg=#fe8019 fs=
#   ^ fg=#ebdbb2 fs=
#    ^ fg=#b8bb26 fs=

x="$(basename "$y")"
# ^ fg=#b8bb26 fs=
#  ^ fg=#fe8019 fs=
#   ^ fg=#83a598 fs=
#    ^^^^^^^^ fg=#fb4934 fs=
#             ^ fg=#b8bb26 fs=
#              ^  fg=#fe8019 fs=
#               ^ fg=#ebdbb2 fs=
#                ^ fg=#b8bb26 fs=
#                 ^ fg=#83a598 fs=
#                  ^ fg=#b8bb26 fs=

x="./${x#$HOME/}"
# ^^^ fg=#b8bb26 fs=
#    ^ fg=#fe8019 fs=
#     ^ fg=#83a598 fs=
#      ^ fg=#ebdbb2 fs=
#       ^ fg=#fb4934 fs=
#        ^ fg=#fe8019 fs=
#         ^^^^ fg=#ebdbb2 fs=
#             ^ fg=#ebdbb2 fs= build>=4090
#              ^ fg=#83a598 fs=
#               ^ fg=#b8bb26 fs=

a=${b%/} c=${d%.e}
# ^ fg=#fe8019 fs=
#  ^ fg=#83a598 fs=
#   ^ fg=#ebdbb2 fs=
#    ^ fg=#fb4934 fs= build>=4090
#     ^ fg=#ebdbb2 fs= build>=4090
#      ^ fg=#83a598 fs=
#        ^ fg=#ebdbb2 fs=
#         ^ fg=#fe8019 fs=
#          ^ fg=#fe8019 fs=
#           ^ fg=#83a598 fs=
#            ^ fg=#ebdbb2 fs=
#             ^ fg=#fb4934 fs=
#              ^^ fg=#ebdbb2 fs= build>=4090
#                ^ fg=#83a598 fs=

    func() {
#   ^ fg=#b8bb26 fs=
#       ^^ fg=#83a598 fs=
#          ^ fg=#83a598 fs=

        if [ -n "$x" ]; then
#       ^ fg=#fb4934 fs=
#          ^ fg=#fe8019 fs=
#            ^^ fg=#fb4934 fs=
#                    ^ fg=#fe8019 fs=
#               ^ fg=#b8bb26 fs=
#                ^ fg=#fe8019 fs=
#                 ^ fg=#ebdbb2 fs=
#                  ^ fg=#b8bb26 fs=
#                          ^ fg=#fb4934 fs=
            echo "hello"
#           ^ fg=#fb4934 fs=
        fi
#       ^ fg=#fb4934 fs=

        return
#       ^ fg=#fb4934 fs=
    }
#   ^ fg=#83a598 fs=

if [ "$#" = 0 ] || [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    cat <<USAGE
#       ^^ fg=#fe8019 fs=
#         ^ fg=#83a598 fs=
description
USAGE
# ^ fg=#83a598 fs=
    echo >&2 "lni: missing target operand"
#   ^ fg=#fb4934 fs=
#        ^ fg=#fe8019 fs=
#         ^ fg=#fe8019 fs=
#          ^ fg=#d3869b fs=
#            ^^ fg=#b8bb26 fs=

    exit 1
#   ^ fg=#fb4934 fs=
#        ^ fg=#d3869b fs=
fi
