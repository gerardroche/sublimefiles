// COLOR SCHEME TEST "GruvboxDark.sublime-color-scheme" "C"

        // whitespace
// ^ fg=#ebdbb2 bg=#282828 fs=

    // x
//  ^^^^ fg=#928374 fs=italic

#include <windows.h>
// ^ fg=#8ec07c fs=
//       ^^^^^^^^^^^ fg=#b8bb26 fs=

#define UNICODE
// ^ fg=#8ec07c fs=
//      ^ fg=#ebdbb2 fs=

#define CONST0 1 // x
// ^ fg=#8ec07c fs=
//      ^^^^^^ fg=#ebdbb2 fs=
//             ^ fg=#d3869b fs=
//               ^^^^ fg=#928374 fs=italic

bool x = true;
// ^ fg=#83a598 fs=
//   ^ fg=#ebdbb2 fs=
//     ^ fg=#fe8019 fs=
//       ^^^^ fg=#d3869b fs=
//           ^ fg=#ebdbb2 fs=

int x() {}
//^ fg=#83a598 fs=
//  ^ fg=#ebdbb2 fs=
//   ^^ fg=#83a598 fs=
//      ^^ fg=#83a598 fs=

typedef int myint;
// ^ fg=#fabd2f fs=
//      ^ fg=#83a598 fs=
//          ^ fg=#ebdbb2 fs=
//               ^ fg=#ebdbb2 fs=

typedef struct mystruct {
// ^ fg=#fabd2f fs=
//      ^ fg=#fabd2f fs=
//             ^ fg=#ebdbb2 fs= build>=4118
//                      ^ fg=#83a598 fs=
    } mystruct;
//  ^ fg=#83a598 fs=
//    ^ fg=#ebdbb2 fs=
//            ^ fg=#ebdbb2 fs=

struct point
// ^ fg=#fabd2f fs=
//     ^ fg=#ebdbb2 fs=
{
    int x;
//  ^ fg=#83a598 fs=
//      ^ fg=#ebdbb2 fs=
//       ^ fg=#ebdbb2 fs=
    int y;
//  ^ fg=#83a598 fs=
//      ^ fg=#ebdbb2 fs=
//       ^ fg=#ebdbb2 fs=
}

struct foo **alloc_foo();
// ^ fg=#fabd2f fs=
//     ^ fg=#ebdbb2 fs=
//         ^^ fg=#fb4934 fs=
//           ^ fg=#ebdbb2 fs=
//                    ^^ fg=#83a598 fs=

scanf("%ms %as %*[, ]", &buf);
// ^ fg=#ebdbb2 fs=
//   ^ fg=#83a598 fs=
//    ^ fg=#b8bb26 fs=
//     ^^^ fg=#d3869b fs=
//         ^^^ fg=#d3869b fs=
//             ^^^^^^ fg=#d3869b fs=
//                   ^ fg=#b8bb26 fs=
//                    ^^ fg=#ebdbb2 fs=
//                      ^ fg=#fb4934 fs=
//                       ^^^ fg=#ebdbb2 fs=
//                          ^ fg=#83a598 fs=


int main(int argc, char **argv) {
//  ^ fg=#ebdbb2 fs=
//      ^ fg=#83a598 fs=
//       ^^^ fg=#83a598 fs=
//           ^ fg=#ebdbb2 fs=
//               ^ fg=#ebdbb2 fs=
//                 ^ fg=#83a598 fs=
//                      ^^ fg=#fb4934 fs=
//                        ^ fg=#ebdbb2 fs=
//                            ^ fg=#83a598 fs=
//                              ^ fg=#83a598 fs=

    int speed = 0, speed1 = 0, speed2 = 0;
    //^ fg=#83a598 fs=
    //  ^ fg=#ebdbb2 fs=
    //        ^ fg=#fe8019 fs=
    //          ^ fg=#d3869b fs=
    //           ^ fg=#ebdbb2 fs=
    //             ^ fg=#ebdbb2 fs=
    //                    ^ fg=#fe8019 fs=
    //                      ^ fg=#d3869b fs=
    //                       ^ fg=#ebdbb2 fs=
    //                         ^ fg=#ebdbb2 fs=
    //                                ^ fg=#fe8019 fs=
    //                                  ^ fg=#d3869b fs=
    //                                   ^ fg=#ebdbb2 fs=

    printf("Set Mouse Speed by Maverick\n");
    // ^ fg=#b8bb26 fs=bold
    //     ^^ fg=#b8bb26 fs=
    //                                 ^^ fg=#fe8019 fs=
    //                                   ^ fg=#b8bb26 fs=

    SystemParametersInfo(SPI_GETMOUSESPEED, 0, &speed, 0);
    // ^ fg=#ebdbb2 fs=
    //                  ^ fg=#83a598 fs=
    //                   ^ fg=#ebdbb2 fs=
    //                                      ^ fg=#d3869b fs=
    //                                       ^ fg=#ebdbb2 fs=
    //                                         ^ fg=#fb4934 fs=
    //                                          ^ fg=#ebdbb2 fs=
    //                                                 ^ fg=#d3869b fs=
    //                                                  ^ fg=#83a598 fs=

    printf("Current speed: %2d\n", speed);
    // ^ fg=#b8bb26 fs=bold
    //     ^^ fg=#b8bb26 fs=
    //                     ^^^ fg=#d3869b fs=
    //                        ^^ fg=#fe8019 fs=
    //                          ^ fg=#b8bb26 fs=

    if (argc == 1) return 0;
//  ^ fg=#fb4934 fs=
    //       ^^ fg=#fb4934 fs=
    //          ^ fg=#d3869b fs=
    //             ^ fg=#fb4934 fs=
    //                    ^ fg=#d3869b fs=

    if (argc >= 2) sscanf(argv[1], "%d", &speed1);
//  ^ fg=#fb4934 fs=
    //       ^^ fg=#fb4934 fs=
    //          ^ fg=#d3869b fs=
    //             ^ fg=#b8bb26 fs=bold
    //                         ^ fg=#d3869b fs=
    //                              ^^ fg=#d3869b fs=

    if (argc >= 3) sscanf(argv[2], "%d", &speed2);
//  ^ fg=#fb4934 fs=
    //       ^^ fg=#fb4934 fs=
    //          ^ fg=#d3869b fs=
    //             ^ fg=#b8bb26 fs=bold
    //                         ^ fg=#d3869b fs=
    //                              ^^ fg=#d3869b fs=

    if (argc == 2) // set speed to first value
//  ^ fg=#fb4934 fs=
    //       ^^ fg=#fb4934 fs=
    //          ^ fg=#d3869b fs=
        speed = speed1;
        //    ^ fg=#fe8019 fs=
    else if (speed == speed1 || speed == speed2) // alternate
    // ^ fg=#fb4934 fs=
    //   ^ fg=#fb4934 fs=
    //             ^^ fg=#fb4934 fs=
    //                       ^^ fg=#fe8019 fs=
    //                                ^^ fg=#fb4934 fs=
        speed = speed1 + speed2 - speed;
        //    ^ fg=#fe8019 fs=
        //             ^ fg=#fe8019 fs=
        //                      ^ fg=#fe8019 fs=
    else
    // ^ fg=#fb4934 fs=
        speed = speed1;  // start with first value

    SystemParametersInfo(SPI_SETMOUSESPEED, 0,  speed, 0);
    // ^ fg=#ebdbb2 fs=
    //                                      ^ fg=#d3869b fs=
    //                                                 ^ fg=#d3869b fs=

    SystemParametersInfo(SPI_GETMOUSESPEED, 0, &speed, 0);
    // ^ fg=#ebdbb2 fs=
    //                                      ^ fg=#d3869b fs=
    //                                                 ^ fg=#d3869b fs=

    printf("New speed: %2d\n", speed);
    // ^ fg=#b8bb26 fs=bold
    //     ^^ fg=#b8bb26 fs=
    //                 ^^^ fg=#d3869b fs=
    //                    ^^ fg=#fe8019 fs=
    //                      ^ fg=#b8bb26 fs=

    return 0;
    // ^ fg=#fb4934 fs=
    //     ^ fg=#d3869b fs=
}

int foo(int a, float b[])
//      ^ fg=#83a598 fs=
//          ^ fg=#ebdbb2 fs=
//           ^ fg=#ebdbb2 fs=
//             ^ fg=#83a598 fs=
//                   ^ fg=#ebdbb2 fs=
//                    ^^ fg=#83a598 fs=
//                      ^ fg=#83a598 fs=
{
    myClass *result;
    // ^ fg=#ebdbb2 fs=
    //      ^ fg=#fb4934 fs=
    //       ^ fg=#ebdbb2 fs=
    //             ^ fg=#ebdbb2 fs=

    result->kk = func(val);
    // ^ fg=#ebdbb2 fs=
    //    ^^ fg=#fabd2f fs= build>=3154
    //      ^^ fg=#ebdbb2 fs=
    //         ^ fg=#fe8019 fs=
    //           ^ fg=#ebdbb2 fs=
    //               ^ fg=#83a598 fs=
    //                ^ fg=#ebdbb2 fs=
    //                   ^ fg=#83a598 fs=

    if (result == 0) {
    // ^ fg=#83a598 fs=
    //  ^ fg=#ebdbb2 fs=
    //         ^^ fg=#fb4934 fs=
    //            ^ fg=#d3869b fs=
    //             ^ fg=#83a598 fs=
        return 0;
        // ^ fg=#fb4934 fs=
        //     ^ fg=#d3869b fs=
        //      ^ fg=#ebdbb2 fs=
#if CROSS_SCOPE_MACRO
//^ fg=#8ec07c fs=
//  ^ fg=#ebdbb2 fs=
    } else if (result > 0) {
    // ^ fg=#fb4934 fs=
    //     ^ fg=#fb4934 fs=
        return 1;
#endif
// ^ fg=#8ec07c fs=
    }
}
