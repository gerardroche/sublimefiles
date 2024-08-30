// COLOR SCHEME TEST "GruvboxDarkVim.sublime-color-scheme" "JavaScript"

        // whitespace
// ^ fg=#ebdbb2 bg=#282828 fs=

    // x
//  ^^^^ fg=#928374 fs=italic
    /* x */
//  ^^^^^^^ fg=#928374 fs=italic
    /** x */
//  ^^^^^^^^ fg=#928374 fs=italic
    /*
//  ^^ fg=#928374 fs=italic
        x
//      ^ fg=#928374 fs=italic
    */
//  ^^ fg=#928374 fs=italic
    /**
     * x
     */
//   ^^ fg=#928374 fs=italic

function $x(block, cls) {
// ^ fg=#b8bb26 fs=bold
//       ^^ fg=#ebdbb2 fs=
//         ^ fg=#83a598 fs=
//          ^^^^^ fg=#ebdbb2 fs=
//               ^ fg=#ebdbb2 fs=
//                 ^^^ fg=#ebdbb2 fs=
//                    ^ fg=#83a598 fs=
//                      ^ fg=#83a598 fs=

    var x = 'ab';
    //^ fg=#fabd2f fs= build>=4168
    //  ^ fg=#ebdbb2 fs=
    //    ^ fg=#fe8019 fs=
    //      ^^^^ fg=#b8bb26 fs=
    //          ^ fg=#ebdbb2 fs=

    try {
    //^ fg=#fb4934 fs=

        if (cls.search(/\bno\-highlight\b/) != -1)
    //  ^ fg=#fb4934 fs=
        //      ^ fg=#ebdbb2 fs=
        //             ^ fg=#b8bb26 fs=
        //              ^^ fg=#fb4934 fs=
        //                ^^ fg=#b8bb26 fs=
        //                  ^^ fg=#fe8019 fs=
        //                    ^^^^^^^^^ fg=#b8bb26 fs=
        //                             ^^ fg=#fb4934 fs=
        //                               ^ fg=#b8bb26 fs=
        //                                ^ fg=#83a598 fs=
        //                                  ^^ fg=#fb4934 fs=
        //                                     ^ fg=#fe8019 fs= build>=4061
        //                                      ^ fg=#d3869b fs=

        return process(block, true, 0x0F) +
        // ^ fg=#fb4934 fs=
        //     ^ fg=#d3869b fs=
        //                    ^^^^ fg=#d3869b fs=
        //                          ^^^^ fg=#d3869b fs=
        //                                ^ fg=#fe8019 fs=
            `class="${cls}"`;
        //  ^^^^^^^^ fg=#b8bb26 fs=
        //          ^^ fg=#83a598 fs= build>=3127
        //            ^^^ fg=#ebdbb2 fs=
        //               ^ fg=#83a598 fs= build>=3127
        //                ^^ fg=#b8bb26 fs=
        //                  ^ fg=#ebdbb2 fs=

    } catch (e) {
    // ^ fg=#fb4934 fs=

    }

    for (var i = 0 / 2; i < classes.length; i++) {
    //^ fg=#fb4934 fs=
    //    ^ fg=#fabd2f fs= build>=4168
    //         ^ fg=#fe8019 fs=
    //           ^ fg=#d3869b fs=
    //             ^ fg=#fe8019 fs=
    //               ^ fg=#d3869b fs=
    //                    ^ fg=#fb4934 fs=
    //                                       ^^ fg=#fe8019 fs=

    if (checkCondition(classes[i]) === undefined)
//  ^ fg=#fb4934 fs=
    //  ^ fg=#ebdbb2 fs=
    //                             ^^^ fg=#fb4934 fs=
    //                                 ^ fg=#d3869b fs=
        console.log('undefined');
        // ^ fg=#b8bb26 fs=
        //      ^ fg=#b8bb26 fs=bold
        //          ^^ fg=#b8bb26 fs=
    }
}

export $initHighlight;
// ^ fg=#fb4934 fs=
//     ^ fg=#ebdbb2 fs=
//      ^ fg=#ebdbb2 fs=

class Foo extends React.Component {
// ^ fg=#fabd2f fs=
//    ^ fg=#ebdbb2 fs=
//        ^ fg=#fabd2f fs=
//                ^^^^^ fg=#ebdbb2 fs= build>=3157
//                     ^ fg=#ebdbb2 fs=
//                      ^^^^^^^^^ fg=#ebdbb2 fs=
//                                ^ fg=#83a598 fs=

    constructor()
    // ^ fg=#ebdbb2 fs=
    //         ^^ fg=#83a598 fs=
        {}
    //  ^^ fg=#83a598 fs=

    [foo.bar](arg) {
//  ^ fg=#83a598 fs=
//   ^^^ fg=#ebdbb2 fs= build>=3157
//      ^ fg=#ebdbb2 fs= build>=3157
//       ^^^ fg=#ebdbb2 fs= build>=3157
//          ^^ fg=#83a598 fs=
//            ^^^ fg=#ebdbb2 fs=
//               ^ fg=#83a598 fs=
//                 ^ fg=#83a598 fs=
    }
//  ^ fg=#83a598 fs=

    get x() {
    //^ fg=#83a598 fs=
    //  ^ fg=#ebdbb2 fs=
    //   ^^ fg=#83a598 fs=
        return this._foo;
        // ^ fg=#fb4934 fs=
        //     ^^^^ fg=#ebdbb2 fs=
        //         ^ fg=#ebdbb2 fs=
        //          ^^^^^ fg=#ebdbb2 fs=
    }

    static x(y) {}
    // ^ fg=#fabd2f fs= build>=3156
    //     ^ fg=#ebdbb2 fs=
    //      ^ fg=#83a598 fs=
    //       ^ fg=#ebdbb2 fs=
    //        ^ fg=#83a598 fs=
    //          ^^ fg=#83a598 fs=

    set (v) { return x; }
    //^ fg=#ebdbb2 fs=
    //  ^ fg=#83a598 fs=
    //   ^ fg=#ebdbb2 fs=
    //    ^ fg=#83a598 fs=
    //      ^ fg=#83a598 fs=
    //        ^ fg=#fb4934 fs=
    //               ^^ fg=#ebdbb2 fs=
    //                  ^ fg=#83a598 fs=
}
