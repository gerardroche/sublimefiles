// COLOR SCHEME TEST "GruvboxDark.sublime-color-scheme" "C#"

using System;
// ^ fg=#8ec07c fs=
//    ^ fg=#ebdbb2 fs=
using System.Windows.Forms;
// ^ fg=#8ec07c fs=
//    ^^^^^^^^^^^^^^^^^^^^^ fg=#ebdbb2 fs=

class Program
// ^ fg=#fabd2f fs= build>=3127
//    ^ fg=#ebdbb2 fs=
{
    const double PI = 3.14;
    // ^ fg=#fabd2f fs=
    //    ^ fg=#83a598 fs=
    //           ^^ fg=#ebdbb2 fs=
    //              ^ fg=#fe8019 fs=
    //                ^^^^ fg=#d3869b fs=
    //                    ^ fg=#ebdbb2 fs=

    public int X;
    // ^ fg=#fabd2f fs=
    //     ^ fg=#83a598 fs=
    //         ^^ fg=#ebdbb2 fs=

    int x = 37;
    //^ fg=#83a598 fs=
    //  ^ fg=#ebdbb2 fs=
    //    ^ fg=#fe8019 fs=
    //      ^^ fg=#d3869b fs=
    //        ^ fg=#ebdbb2 fs=

    int[] x(int y) {return x + y;}
    //^ fg=#83a598 fs=
    // ^^ fg=#83a598 fs=
    //    ^ fg=#ebdbb2 fs=
    //     ^ fg=#83a598 fs=
    //      ^^^ fg=#83a598 fs=
    //          ^ fg=#ebdbb2 fs=
    //           ^ fg=#83a598 fs=
    //             ^ fg=#83a598 fs=
    //              ^^^^^^ fg=#fb4934 fs=
    //                     ^ fg=#ebdbb2 fs=
    //                       ^ fg=#fb4934 fs= build>=3127
    //                         ^ fg=#ebdbb2 fs=
    //                          ^ fg=#ebdbb2 fs=
    //                           ^ fg=#83a598 fs=

    abcd () {
    // ^ fg=#ebdbb2 fs=
    }

    X (string x) : base () {
    //^^^^^^^ fg=#83a598 fs=
    //        ^ fg=#ebdbb2 fs=
        Console.WriteLine("ab");
        // ^^^^^ fg=#ebdbb2 fs=
        //      ^^^^^^^^^ fg=#ebdbb2 fs= build>=3127
        //               ^ fg=#83a598 fs=
        //                ^^^^ fg=#b8bb26 fs=
        //                    ^ fg=#83a598 fs=
    }

    void x([Usage("ab")] int x, int y)
    // ^ fg=#83a598 fs=
    //   ^ fg=#ebdbb2 fs=
    //    ^        fg=#83a598 fs=
    //     ^ fg=#83a598 fs= build>=4168
    //      ^^^^^ fg=#b8bb26 fs=bold
    //           ^ fg=#83a598 fs=
    //            ^^^^ fg=#b8bb26 fs=
    //                ^ fg=#83a598 fs=
    //                 ^ fg=#83a598 fs= build>=4168
    //                   ^^^ fg=#83a598 fs=
    //                       ^ fg=#ebdbb2 fs=
    //                        ^ fg=#ebdbb2 fs=
    //                          ^^^ fg=#83a598 fs=
    //                              ^ fg=#ebdbb2 fs=
    //                               ^ fg=#83a598 fs=

    static void Main(string[] x)
    // ^ fg=#ebdbb2 bg=#fb4934 fs= build>=3154
    //     ^ fg=#83a598 fs=
    //          ^ fg=#ebdbb2 fs=
    //              ^ fg=#83a598 fs=
    //               ^^^^^^ fg=#83a598 fs=
    //                     ^^ fg=#83a598 fs= build>=3127
    //                        ^ fg=#ebdbb2 fs=
    //                         ^ fg=#83a598 fs=
    {
    }
}

string verbatim = @"ab "" cd";
// ^ fg=#83a598 fs=
//     ^^^^^^^^ fg=#ebdbb2 fs=
//              ^ fg=#fe8019 fs= build>=3127
//                ^^^^ fg=#b8bb26 fs=
//                     ^^ fg=#fe8019 fs=
//                        ^^^ fg=#b8bb26 fs=
//                           ^ fg=#ebdbb2 fs=

public class GenericList<T>
// ^ fg=#fabd2f fs=
//     ^ fg=#fabd2f fs= build>=3127
//           ^ fg=#ebdbb2 fs=
//                      ^ fg=#ebdbb2 fs=
//                       ^ fg=#b8bb26 fs= build>=3127
//                        ^ fg=#ebdbb2 fs=
{
    void Add(T i) { }
    // ^ fg=#83a598 fs=
    //   ^^^ fg=#ebdbb2 fs=
    //      ^ fg=#83a598 fs=
    //       ^ fg=#b8bb26 fs=
    //         ^ fg=#ebdbb2 fs=
    //          ^ fg=#83a598 fs=
}

class InheritingSomething: IYourInterface {
// ^ fg=#fabd2f fs= build>=3127
//    ^^^^^^^^^^^^^^^^^^^ fg=#ebdbb2 fs=
//                       ^ fg=#fe8019 fs=
//                         ^^^^^^^^^^^^^^ fg=#ebdbb2 fs= build>=3127
//                                        ^ fg=#83a598 fs=
}

class WithGeneric<T1, T2> where T1: IEnumerable<T2> {}
// ^ fg=#fabd2f fs= build>=3127
//   ^ fg=#ebdbb2 fs=
//    ^^^^^^^^^^^ fg=#ebdbb2 fs=
//               ^ fg=#ebdbb2 fs=
//                ^^ fg=#b8bb26 fs= build>=3127
//                  ^ fg=#fe8019 fs=
//                    ^^ fg=#b8bb26 fs= build>=3127
//                      ^ fg=#ebdbb2 fs=
//                                ^ fg=#fe8019 fs= build>=3127
//                                  ^^^^^^^^^^^ fg=#ebdbb2 fs= build>=3127
//                                             ^ fg=#ebdbb2 fs=
//                                              ^^ fg=#b8bb26 fs=
//                                                ^^ fg=#ebdbb2 fs=
//                                                  ^^ fg=#83a598 fs=
