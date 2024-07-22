<!-- COLOR SCHEME TEST "GruvboxDark.sublime-color-scheme" "Markdown" -->

# This is an <h1> tag
<!-- ^ fg=#b8bb26 fs=bold build>=3127 -->

## This is an <h2> tag
#^ fg=#b8bb26 fs= build>=3127
<!-- ^ fg=#b8bb26 fs=bold build>=3127 -->

### This is an <h3> tag
# ^ fg=#b8bb26 fs= build>=3127
<!-- ^ fg=#b8bb26 fs=bold build>=3127 -->

#### This is an <h4> tag
# ^ fg=#b8bb26 fs= build>=3127
<!-- ^ fg=#b8bb26 fs=bold build>=3127 -->

##### This is an <h5> tag
# ^ fg=#b8bb26 fs= build>=3127
<!--  ^ fg=#b8bb26 fs=bold build>=3127 -->

###### This is an <h6> tag
# ^ fg=#b8bb26 fs= build>=3127 -->
<!--   ^ fg=#b8bb26 fs=bold build>=3127 -->

### X ###
<!--  ^ fg=#b8bb26 fs= -->

# EMPHASIS

This is *italic text* and _so is this_.
<!-- ^^^ fg=#ebdbb2 fs= -->
<!--    ^ fg=#bdae93 fs=italic -->
<!--     ^^^^^^^^^^^ fg=#bdae93 fs=italic -->
<!--                ^ fg=#bdae93 fs=italic -->
<!--                 ^^^^^ fg=#ebdbb2 fs= -->
<!--                      ^ fg=#bdae93 fs=italic -->
<!--                       ^^^^^^^^^^ fg=#bdae93 fs=italic -->
<!--                                 ^ fg=#bdae93 fs=italic -->
<!--                                  ^ fg=#ebdbb2 fs= -->

This is **bold text** and __so is this__.
<!-- ^^^ fg=#ebdbb2 fs= -->
<!--    ^^ fg=#bdae93 fs=bold -->
<!--      ^^^^^^^^^ fg=#bdae93 fs=bold -->
<!--               ^^ fg=#bdae93 fs=bold -->
<!--                 ^^^^^ fg=#ebdbb2 fs= -->
<!--                      ^^ fg=#bdae93 fs=bold -->
<!--                        ^^^^^^^^^^ fg=#bdae93 fs=bold -->
<!--                                  ^^ fg=#bdae93 fs=bold -->
<!--                                    ^ fg=#ebdbb2 fs= -->

If you like *you **can** combine them*
<!-- ^^^^^^^ fg=#ebdbb2 fs= -->
<!--        ^ fg=#bdae93 fs=italic -->
<!--         ^^^^ fg=#bdae93 fs=italic -->
<!--             ^^ fg=#bdae93 fs=italic build>=4118 -->
<!--               ^^^ fg=#bdae93 fs=italic build>=4118 -->
<!--                  ^^ fg=#bdae93 fs=italic build>=4118 -->
<!--                    ^^^^^^^^^^^^^ fg=#bdae93 fs=italic -->
<!--                                 ^ fg=#bdae93 fs=italic -->

If you like **you *can* combine them**
<!-- ^^^^^^^ fg=#ebdbb2 fs= -->
<!--        ^^ fg=#bdae93 fs=bold -->
<!--          ^^^^ fg=#bdae93 fs=bold -->
<!--              ^ fg=#bdae93 fs=bold italic -->
<!--               ^^^ fg=#bdae93 fs=bold italic -->
<!--                  ^ fg=#bdae93 fs=bold italic -->
<!--                   ^^^^^^^^^^^^^ fg=#bdae93 fs=bold -->
<!--                                ^^ fg=#bdae93 fs=bold -->

*Abc [X](y)*
<!-- ^^^^ fs=italic -->
<!--     ^ fs=italic underline -->
<!--      ^ fs=italic -->

*Abc [X][1]*
<!-- ^^^^ fs=italic -->
<!--     ^ fs=italic underline -->
<!--      ^ fs=italic -->

**Ab [X](y)**
<!-- ^^^^ fs=bold -->
<!--     ^ fs=bold underline -->
<!--      ^ fs=bold -->

**Ab [X][1]**
<!-- ^^^^ fs=bold -->
<!--     ^ fs=bold underline -->
<!--      ^ fs=bold -->

# Images

.... ![Alt](url)
<!-- ^^ fg=#83a598 fs= -->
<!--   ^^^ fg=#ebdbb2 fs= -->
<!--      ^^ fg=#83a598 fs= -->
<!--        ^^^ fg=#d3869b fs=underline build>=4000 -->
<!--           ^ fg=#83a598 fs= -->

.... ![Alt][1]
<!-- ^^ fg=#83a598 fs= -->
<!--   ^^^ fg=#ebdbb2 fs= -->
<!--      ^^ fg=#83a598 fs= -->
<!--        ^ fg=#d3869b fs=underline build>=4134 -->
<!--         ^ fg=#83a598 fs= -->

[12345]: url
<!-- ^ fg=#ebdbb2 fs= build>=3150 -->
<!--  ^^ fg=#83a598 fs= -->
<!--     ^^^ fg=#d3869b fs=underline build>=4000 -->

# Links

https://github.com - automatic
<!-- ^^^^^^^^^^^^^ fg=#d3869b fs=underline build>=4000 -->
<!--              ^^^^^^^^^^^^ fg=#ebdbb2 fs= -->

..... [Alt](url)
<!--  ^ fg=#83a598 fs= -->
<!--   ^^^ fg=#ebdbb2 fs= -->
<!--      ^^ fg=#83a598 fs= -->
<!--        ^^^ fg=#d3869b fs=underline build>=4000 -->
<!--           ^ fg=#83a598 fs= -->

.... [Alt][1]
<!-- ^ fg=#83a598 fs= -->
<!--  ^^^ fg=#ebdbb2 fs= -->
<!--     ^^ fg=#83a598 fs= -->
<!--       ^ fg=#d3869b fs=underline build>=4134 -->
<!--        ^ fg=#83a598 fs= -->

.... [Alt][]
<!-- ^ fg=#83a598 fs= -->
<!--  ^^^ fg=#ebdbb2 fs= -->
<!--     ^^^ fg=#83a598 fs= -->

[12345]: url
<!-- ^ fg=#ebdbb2 fs= build>=3150 -->
<!--  ^^ fg=#83a598 fs= -->
<!--     ^^^ fg=#d3869b fs=underline build>=4000 -->

# [X](y)
# ^ fg=#83a598 fs=bold
#  ^ fg=#b8bb26 fs=bold
#   ^^ fg=#83a598 fs=bold
#     ^ fg=#d3869b fs=underline
#      ^ fg=#83a598 fs=bold

# [X][1]
# ^ fg=#83a598 fs=bold
#  ^ fg=#b8bb26 fs=bold
#   ^^ fg=#83a598 fs=bold
#     ^ fg=#d3869b fs=underline
#      ^ fg=#83a598 fs=bold

## [X](y)
#^ fg=#b8bb26 fs=
#  ^ fg=#83a598 fs=bold
#   ^ fg=#b8bb26 fs=bold
#    ^^ fg=#83a598 fs=bold
#      ^ fg=#d3869b fs=underline
#       ^ fg=#83a598 fs=bold

### [X](y)
#^^ fg=#b8bb26 fs=
#   ^ fg=#83a598 fs=bold
#    ^ fg=#b8bb26 fs=bold
#     ^^ fg=#83a598 fs=bold
#       ^ fg=#d3869b fs=underline
#        ^ fg=#83a598 fs=bold

Firstname Lname <name@example.com>
<!-- ^^^^ fg=#ebdbb2 fs= -->
<!--      ^^^^^ fg=#ebdbb2 fs= -->
<!--            ^ fg=#83a598 fs= -->
<!--             ^^^^^^^^^^^^^^^^ fg=#d3869b fs=underline build>=4000 -->
<!--                             ^ fg=#83a598 fs= -->

# Blockquotes

As Kanye West said:

  > We're living the future so
  > the present is our past.
# ^ fg=#ebdbb2 fs= -->
<!-- ^^^^^^^^^^^^^^^^^^^^^^^ fg=#ebdbb2 fs= -->

# Lists

Unordered

* Item 1
* Item 2
  * Item 2a
# ^ fg=#83a598 fs= -->
#   ^ fg=#ebdbb2 fs= -->
  * Item 2b
# ^ fg=#83a598 fs= -->
#   ^ fg=#ebdbb2 fs= -->

Ordered

1. Item 1
2. Item 2
3. Item 3
   * Item 3a
#  ^ fg=#83a598 fs= -->
#    ^ fg=#ebdbb2 fs= -->
   * Item 3b
#  ^ fg=#83a598 fs= -->
#    ^ fg=#ebdbb2 fs= -->

  1. item 1
# ^ fg=#83a598 fs= -->
  2. item 2

# Escapes

.... \*x\\y\.z
<!-- ^^ fg=#fe8019 fs= -->
<!--   ^ fg=#ebdbb2 fs= -->
<!--    ^^ fg=#fe8019 fs= -->
<!--      ^ fg=#ebdbb2 fs= -->
<!--       ^^ fg=#fe8019 fs= -->
<!--         ^ fg=#ebdbb2 fs= -->

# Entities

.... &nbsp; . &copy;
<!-- ^^^^^^ fg=#fe8019 fs= -->
<!--          ^^^^^^ fg=#fe8019 fs= -->

.... &#35;
<!-- ^^^^^ fg=#fe8019 fs= -->

.... &MadeUpEntity;
<!-- ^^^^^^^^^^^^^^ fg=#fe8019 fs= -->

# Inline code

I think you should use an `<addr>` element here instead.
<!--                  ^^^^ fg=#ebdbb2 bg=#282828 fs= -->
<!--                      ^ fg=#83a598 bg=#282828 fs= -->
<!--                       ^^^^^^ fg=#8ec07c bg=#282828 fs= -->
<!--                             ^ fg=#83a598 bg=#282828 fs= -->
<!--                              ^^^ fg=#ebdbb2 bg=#282828 fs= -->

# Syntax highlighting

Here's an example of how you can use syntax highlighting with GitHub Flavored Markdown:

```javascript
#^^ fg=#83a598 bg=#282828 fs= build>=3127 -->
#  ^^^^^^^^^^ fg=#83a598 bg=#282828 fs= build>=3127
function x() {}
<!-- ^^^ fg=#b8bb26 bg=#282828 fs=bold build>=3184 -->
```
#^^ fg=#83a598 bg=#282828 fs= build>=3127 -->

You can also simply indent your code by four spaces:

    function x() {
    # ^^^^^^^^^^^^^ fg=#8ec07c bg=#282828 fs= -->
    }
#^^^^ fg=#8ec07c bg=#282828 fs= build>=3127 -->

Here's an example of Python code without syntax highlighting:

    def foo():
    # ^^^^^^^^ fg=#8ec07c bg=#282828 fs= build>=3127 -->
      if not bar:
        return True

# Task Lists

- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
- [x] <del>tags</del> support
  <!--^ fg=#83a598 fs= -->
  <!-- ^^^ fg=#b8bb26 fs= build>=3127 -->
  <!--    ^ fg=#83a598 fs= -->
  <!--     ^^^^ fg=#ebdbb2 fs= -->
  <!--         ^^ fg=#83a598 fs= -->
  <!--           ^^^ fg=#b8bb26 fs= build>=3127 -->
  <!--              ^ fg=#83a598 fs= -->
  <!--               ^^^^^^^^ fg=#ebdbb2 fs= -->
- [x] **formatting** *support*
  <!--^^ fg=#bdae93 fs=bold -->
  <!--  ^^^^^^^^^^ fg=#bdae93 fs=bold -->
  <!--            ^^ fg=#bdae93 fs=bold -->
  <!--              ^ fg=#ebdbb2 fs= -->
  <!--               ^ fg=#bdae93 fs=italic -->
  <!--                ^^^^^^^ fg=#bdae93 fs=italic -->
  <!--                       ^ fg=#bdae93 fs=italic -->
- [x] @mentions, #refs, [links]()
  <!-- ^^^^^^^^^^^^^^^^^ fg=#ebdbb2 fs= -->
  <!--                  ^ fg=#83a598 fs= build>=3158 -->
  <!--                   ^^^^^ fg=#ebdbb2 fs= build>=3158 -->
  <!--                        ^^^ fg=#83a598 fs= build>=3158 -->

If you include a task list in the first comment of an Issue, you will get a handy progress indicator in your issue list. It also works in Pull Requests!

# Tables

You can create tables by assembling a list of words and dividing them with hyphens - (for the first row), and then separating each column with a pipe |:

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

# Line breaks

***
#^^ fg=#bdae93 bg=#282828 fs=

---
#^^ fg=#bdae93 bg=#282828 fs=

___
#^^ fg=#bdae93 bg=#282828 fs=

# SHA references

Any reference to a commit’s SHA-1 hash will be automatically converted into a link to that commit on GitHub.

16c999e8c71134401a78d4d46435517b2271d6ac
mojombo@16c999e8c71134401a78d4d46435517b2271d6ac
mojombo/github-flavored-markdown@16c999e8c71134401a78d4d46435517b2271d6ac

# Issue references within a repository

Any number that refers to an Issue or Pull Request will be automatically converted into a link.

#1
mojombo#1
mojombo/github-flavored-markdown#1

# Username @mentions

Typing an @ symbol, followed by a username, will notify that person to come and view the comment. This is called an “@mention”, because you’re mentioning the individual. You can also @mention teams within an organization.
<!-- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ fg=#ebdbb2 fs= -->

# Automatic linking for URLs

Any URL (like http://www.github.com/) will be automatically converted into a clickable link.
<!-- ^^^^^^^^^ fg=#ebdbb2 fs= -->
<!--          ^^^^^^^^^^^^^^^^^^^^^^ fg=#d3869b fs=underline build>=4000 -->
<!--                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ fg=#ebdbb2 fs= build>=3142 -->

# Strikethrough

Any word wrapped with two tildes (like ~~this~~) will appear crossed out.
<!-- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ fg=#ebdbb2 fs= -->
<!--                                     ^^^^ fg=#bdae93 fs= build>=3157 -->
<!--                                           ^^^^^^^^^^^^ fg=#ebdbb2 fs= -->
<!--                                   ^^ fg=#bdae93 fs= build>=3157 -->
<!--                                         ^^ fg=#bdae93 fs= build>=3157 -->

* [#945](https://github.com/gerardroche/sublime-monokai-free/issues/945): Text
<!--         ^^^^^ fg=#d3869b fs=underline build>=4000 -->
<!--^^ fg=#ebdbb2 fs= build>=4000 -->
