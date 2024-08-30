// COLOR SCHEME TEST "GruvboxDarkVim.sublime-color-scheme" "Go"

package examples
// ^ fg=#fb4934 fs= build>=4140
//      ^ fg=#ebdbb2 fs= build>=4081

import (
// ^ fg=#8ec07c fs=
//     ^ fg=#83a598 fs=
    "x"
//  ^^^ fg=#b8bb26 fs=
    )
//  ^ fg=#83a598 fs=

import "x"
// ^ fg=#8ec07c fs=
//     ^^^ fg=#b8bb26 fs=

var valid int = 0
//^ fg=#fb4934 fs=
//  ^ fg=#ebdbb2 fs=
//        ^ fg=#fabd2f fs=
//            ^ fg=#fe8019 fs=
//              ^ fg=#d3869b fs=

var var1, var2, var3
//  ^ fg=#ebdbb2 fs=
//      ^ fg=#ebdbb2 fs=
//        ^ fg=#ebdbb2 fs=
//            ^ fg=#ebdbb2 fs=
//              ^ fg=#ebdbb2 fs=

var1 := 1
//   ^^ fg=#fe8019 fs=
//      ^ fg=#d3869b fs=

var1, var2 := imported.Vals
// ^ fg=#ebdbb2 fs=
//  ^ fg=#ebdbb2 fs=
//    ^ fg=#ebdbb2 fs=
//         ^^ fg=#fe8019 fs=
//            ^ fg=#ebdbb2 fs=
//                    ^ fg=#ebdbb2 fs=
//                     ^ fg=#ebdbb2 fs=

type myStruct struct {
// ^ fg=#fb4934 fs=
//   ^ fg=#ebdbb2 fs=
//            ^ fg=#fb4934 fs=
//                   ^ fg=#83a598 fs=
    FirstFunc   func(arg string)
    // ^ fg=#ebdbb2 fs=
    //          ^ fg=#fb4934 fs=
    //              ^ fg=#83a598 fs=
    //               ^ fg=#ebdbb2 fs=
    //                   ^ fg=#fabd2f fs=
    //                         ^ fg=#83a598 fs=

    SecondFunc  func(arg interface{})
    // ^ fg=#ebdbb2 fs=
    //          ^ fg=#fb4934 fs=
    //              ^ fg=#83a598 fs=
    //               ^ fg=#ebdbb2 fs=
    //                   ^ fg=#fabd2f fs=
    //                            ^^ fg=#83a598 fs=
    //                              ^ fg=#83a598 fs=
}

const (
// ^ fg=#fabd2f fs=
//    ^ fg=#83a598 fs=
    graveAccentString = `hi %s and %[1]s`
    //  ^ fg=#d3869b fs= build>=3177
    //                ^ fg=#fe8019 fs=
    //                  ^^^^ fg=#b8bb26 fs=
    //                      ^^ fg=#d3869b fs=
    //                        ^^^^^ fg=#b8bb26 fs=
    //                             ^^^^^ fg=#d3869b fs= build>=3189
    //                                  ^ fg=#b8bb26 fs=
    normalString = "hi %q and %[1]s"
    // ^ fg=#d3869b fs= build>=3177
    //           ^ fg=#fe8019 fs=
    //             ^^^^ fg=#b8bb26 fs=
    //                 ^^ fg=#d3869b fs=
    //                   ^^^^^ fg=#b8bb26 fs=
    //                        ^^^^^ fg=#d3869b fs= build>=3189
    //                             ^ fg=#b8bb26 fs=
    dynamicFieldWidths = "abc %[1]*.[2]*f %*.*f"
    // ^ fg=#d3869b fs= build>=3177
    //                 ^ fg=#fe8019 fs=
    //                   ^^^^ fg=#b8bb26 fs=
    //                        ^^^^^^^^^^^ fg=#b8bb26 fs= build>=3177
    //                                    ^^^^^ fg=#d3869b fs= build>=4118
    //                                         ^ fg=#b8bb26 fs=
)

func () {
// ^ fg=#fb4934 fs=
//   ^^ fg=#83a598 fs=
//      ^ fg=#83a598 fs=
    Label:
//  ^ fg=#ebdbb2 fs= build>=3177
//       ^ fg=#ebdbb2 fs=
}
