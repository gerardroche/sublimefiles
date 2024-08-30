<?php // COLOR SCHEME TEST "GruvboxDarkVim.sublime-color-scheme" "PHP"

        //
// ^ fg=#ebdbb2 bg=#282828 fs=

// comment
// ^ fg=#928374 fs=italic
/* comment */
// ^ fg=#928374 fs=italic
/**
 * comment
// ^ fg=#928374 fs=italic
 */

declare(strict_types=1);
// ^ fg=#fabd2f fs=
//     ^ fg=#83a598 fs=
//      ^^^^^^^^^^^^ fg=#ebdbb2 fs=
//                  ^ fg=#fe8019 fs=
//                   ^ fg=#d3869b fs=
//                    ^ fg=#83a598 fs=
//                     ^ fg=#ebdbb2 fs=

namespace A;
// ^ fg=#fabd2f fs=
//        ^ fg=#ebdbb2 fs=
//         ^ fg=#ebdbb2 fs=

namespace A\B\C;
// ^ fg=#fabd2f fs=
//        ^^^^^ fg=#ebdbb2 fs=
//             ^ fg=#ebdbb2 fs=

use A;
//^ fg=#8ec07c fs=
// ^ fg=#ebdbb2 fs=
//  ^ fg=#ebdbb2 fs=
//   ^ fg=#ebdbb2 fs=

use Countable;
//  ^ fg=#d3869b fs=

use UserDefined;
//  ^ fg=#ebdbb2 fs=

use A\B\C;
//^ fg=#8ec07c fs=
//  ^^^^ fg=#ebdbb2 fs= build>=4148
//      ^ fg=#ebdbb2 fs=
//       ^ fg=#ebdbb2 fs=

use A\B\Exception;
//      ^ fg=#d3869b fs=

use A\B\UserDefined2;
//      ^ fg=#ebdbb2 fs=

use A\B\C as B;
//^ fg=#8ec07c fs=
//  ^^^^ fg=#ebdbb2 fs= build>=4148
//      ^ fg=#ebdbb2 fs=
//        ^^ fg=#fb4934 fs=
//           ^ fg=#ebdbb2 fs=
//            ^ fg=#ebdbb2 fs=

use function a;
//^ fg=#8ec07c fs=
//  ^^^^^^^^ fg=#8ec07c fs= build>=4143
//           ^ fg=#ebdbb2 fs=
//            ^ fg=#ebdbb2 fs=

use function a\b\c;
//^ fg=#8ec07c fs=
//  ^^^^^^^^ fg=#8ec07c fs= build>=4143
//           ^^^^ fg=#ebdbb2 fs= build>=4148
//               ^ fg=#ebdbb2 fs=
//                ^ fg=#ebdbb2 fs=

use function a\b\c as b;
//^ fg=#8ec07c fs=
//  ^^^^^^^^ fg=#8ec07c fs= build>=4143
//           ^^^^ fg=#ebdbb2 fs= build>=4148
//                ^ fg=#ebdbb2 fs=
//                 ^^ fg=#fb4934 fs=
//                    ^ fg=#ebdbb2 fs=
//                     ^ fg=#ebdbb2 fs=

use const A;
//^ fg=#8ec07c fs=
//  ^^^^^ fg=#fb4934 fs= build>=4143
//        ^ fg=#ebdbb2 fs=
//         ^ fg=#ebdbb2 fs=

use const A\B\C;
//^ fg=#8ec07c fs=
//  ^^^^^ fg=#fb4934 fs= build>=4143
//        ^^^^ fg=#ebdbb2 fs= build>=4148
//            ^ fg=#ebdbb2 fs=
//             ^ fg=#ebdbb2 fs=

use const A\B\C as X;
//^ fg=#8ec07c fs=
//  ^^^^^ fg=#fb4934 fs= build>=4143
//        ^^^^ fg=#ebdbb2 fs= build>=4148
//            ^ fg=#ebdbb2 fs=
//              ^^ fg=#fb4934 fs=
//                 ^ fg=#ebdbb2 fs=
//                  ^ fg=#ebdbb2 fs=

const B = 1;
// ^ fg=#fb4934 fs=
//    ^ fg=#ebdbb2 fs=
//      ^ fg=#fe8019 fs=
//        ^ fg=#d3869b fs=
//         ^ fg=#ebdbb2 fs=

require_once 'x.y';
// ^ fg=#8ec07c fs=
//          ^ fg=#ebdbb2 fs=
//           ^^^^^ fg=#b8bb26 fs=
//                ^ fg=#ebdbb2 fs=

function x() {}
// ^ fg=#8ec07c fs= build>=4143
//       ^ fg=#ebdbb2 fs=
//        ^^ fg=#83a598 fs=
//           ^^ fg=#83a598 fs=

interface x {}
// ^ fg=#fabd2f fs= build>=4143
//       ^ fg=#ebdbb2 fs=
//        ^ fg=#ebdbb2 fs=
//          ^^ fg=#83a598 fs=

trait x {}
// ^ fg=#fabd2f fs= build>=4143
//    ^ fg=#ebdbb2 fs=
//      ^^ fg=#83a598 fs=

class x {}
// ^ fg=#fabd2f fs= build>=4143
//    ^ fg=#ebdbb2 fs=
//      ^^ fg=#83a598 fs=

final class x {}
// ^ fg=#fabd2f fs=
//    ^ fg=#fabd2f fs= build>=4143
//         ^ fg=#ebdbb2 fs=
//            ^^ fg=#83a598 fs=

abstract class x {}
// ^ fg=#fabd2f fs=
//       ^ fg=#fabd2f fs= build>=4143
//             ^ fg=#ebdbb2 fs=
//               ^^ fg=#83a598 fs=

class x extends y {}
// ^ fg=#fabd2f fs= build>=4143
//    ^ fg=#ebdbb2 fs=
//      ^ fg=#fabd2f fs=
//              ^ fg=#ebdbb2 fs= build>=4168
//                ^^ fg=#83a598 fs=

class x implements y {}
// ^ fg=#fabd2f fs= build>=4143
//    ^ fg=#ebdbb2 fs=
//      ^ fg=#fabd2f fs=
//                 ^ fg=#ebdbb2 fs= build>=4168
//                   ^^ fg=#83a598 fs=

class x extends y implements z {}
// ^ fg=#fabd2f fs= build>=4143
//    ^ fg=#ebdbb2 fs=
//      ^ fg=#fabd2f fs=
//              ^ fg=#ebdbb2 fs= build>=4168
//                ^ fg=#fabd2f fs=
//                           ^ fg=#ebdbb2 fs= build>=4168
//                             ^^ fg=#83a598 fs=

class x extends stdClass implements Countable {}
// ^ fg=#fabd2f fs= build>=4143
//    ^ fg=#ebdbb2 fs=
//      ^ fg=#fabd2f fs=
//              ^ fg=#d3869b fs=
//                       ^ fg=#fabd2f fs=
//                                  ^ fg=#d3869b fs=
//                                            ^^ fg=#83a598 fs=

class x extends /* */ \a\b implements \c\d {}
// ^ fg=#fabd2f fs= build>=4143
//    ^ fg=#ebdbb2 fs=
//      ^ fg=#fabd2f fs=
//              ^^^^^ fg=#928374 fs=italic
//                    ^^^^ fg=#ebdbb2 fs= build>=4168
//                         ^ fg=#fabd2f fs=
//                                    ^^^^ fg=#ebdbb2 fs= build>=4168
//                                         ^^ fg=#83a598 fs=

function d($a = array(), $b = "x") {}
// ^ fg=#8ec07c fs= build>=4143
//       ^ fg=#ebdbb2 fs=
//        ^ fg=#83a598 fs=
//         ^ fg=#fe8019 fs=
//          ^ fg=#ebdbb2 fs=
//            ^ fg=#fe8019 fs=
//              ^ fg=#b8bb26 fs=bold
//                   ^^ fg=#83a598 fs=
//                     ^ fg=#ebdbb2 fs=
//                       ^ fg=#fe8019 fs=
//                        ^ fg=#ebdbb2 fs=
//                          ^ fg=#fe8019 fs=
//                            ^^^ fg=#b8bb26 fs=
//                               ^ fg=#83a598 fs=
//                                 ^^ fg=#83a598 fs=

function e($a = []) {}
//              ^^ fg=#83a598 fs=

function f(array $a = [], $b = "x") {}
//         ^^^^^ fg=#fabd2f fs=

function g(array $a = [1, 2, 3, 4],  $b = "x") {}
//                    ^ fg=#83a598 fs=
//                     ^ fg=#d3869b fs=
//                      ^ fg=#ebdbb2 fs=
//                        ^ fg=#d3869b fs=
//                         ^ fg=#ebdbb2 fs=
//                           ^ fg=#d3869b fs=
//                            ^ fg=#ebdbb2 fs=
//                              ^ fg=#d3869b fs=
//                               ^ fg=#83a598 fs=

function h(array $a = null, $b = "x") {}
//                    ^^^^ fg=#fabd2f fs=

function i(&$x) {}
//       ^ fg=#ebdbb2 fs=
//        ^ fg=#83a598 fs=
//         ^ fg=#fe8019 fs=
//          ^ fg=#fe8019 fs=
//           ^ fg=#ebdbb2 fs=
//            ^ fg=#83a598 fs=
//              ^^ fg=#83a598 fs=

function j(X $c) {}
//       ^ fg=#ebdbb2 fs=
//        ^ fg=#83a598 fs=
//         ^ fg=#ebdbb2 fs=
//           ^ fg=#fe8019 fs=
//            ^ fg=#ebdbb2 fs=
//             ^ fg=#83a598 fs=

function k(Countable $c) {}
//       ^ fg=#ebdbb2 fs=
//        ^ fg=#83a598 fs=
//         ^ fg=#d3869b fs=
//                   ^ fg=#fe8019 fs=
//                    ^ fg=#ebdbb2 fs=
//                     ^ fg=#83a598 fs=
//                       ^^ fg=#83a598 fs=

function l(int $a, string $b, bool $c, float $d) {}
//       ^ fg=#ebdbb2 fs=
//        ^ fg=#83a598 fs=
//         ^^^ fg=#fabd2f fs=
//             ^ fg=#fe8019 fs=
//              ^ fg=#ebdbb2 fs=
//               ^ fg=#ebdbb2 fs=
//                 ^^^^^^ fg=#fabd2f fs=
//                        ^ fg=#fe8019 fs=
//                         ^ fg=#ebdbb2 fs=
//                          ^ fg=#ebdbb2 fs=
//                            ^^^^ fg=#fabd2f fs=
//                                 ^ fg=#fe8019 fs=
//                                  ^ fg=#ebdbb2 fs=
//                                   ^ fg=#ebdbb2 fs=
//                                     ^^^^^ fg=#fabd2f fs=
//                                           ^ fg=#fe8019 fs=
//                                            ^ fg=#ebdbb2 fs=
//                                             ^ fg=#83a598 fs=
//                                               ^^ fg=#83a598 fs=

function l2(int|float|array $p) {}
//          ^ fg=#fabd2f fs= build>=4140
//             ^ fg=#fe8019 fs= build>=4140
//              ^ fg=#fabd2f fs= build>=4140
//                   ^ fg=#fe8019 fs= build>=4140
//                    ^ fg=#fabd2f fs= build>=4140

function l3(): float {}
//             ^ fg=#fabd2f fs= build>=4140

function l4(): int|float|array {}
//             ^ fg=#fabd2f fs= build>=4140
//                ^ fg=#fe8019 fs= build>=4140
//                 ^ fg=#fabd2f fs= build>=4140
//                      ^ fg=#fe8019 fs= build>=4140
//                       ^ fg=#fabd2f fs= build>=4140

function m(...$x) {}
//       ^ fg=#ebdbb2 fs=
//        ^ fg=#83a598 fs=
//         ^^^ fg=#fe8019 fs= build>=4061
//            ^ fg=#fe8019 fs=
//             ^ fg=#ebdbb2 fs=
//              ^ fg=#83a598 fs=

function n(
    //    ^ fg=#83a598 fs=
        $a,
    //  ^ fg=#fe8019 fs=
    //   ^ fg=#ebdbb2 fs=
    //    ^ fg=#ebdbb2 fs=
        $b
    //  ^ fg=#fe8019 fs=
    //   ^ fg=#ebdbb2 fs=
        ){}
    //  ^^^ fg=#83a598 fs=


function o(): X {}
// ^^^^^ fg=#8ec07c fs= build>=4143
//       ^ fg=#ebdbb2 fs=
//        ^^ fg=#83a598 fs=
//          ^ fg=#fe8019 fs=
//            ^ fg=#ebdbb2 fs=
//              ^^ fg=#83a598 fs=

function p(): Countable {}
//       ^ fg=#ebdbb2 fs=
//        ^^ fg=#83a598 fs=
//          ^ fg=#fe8019 fs=
//            ^^^^^^^^^ fg=#d3869b fs=

$abc = function() {};
// ^ fg=#ebdbb2 fs=
//   ^ fg=#fe8019 fs=
//     ^^^^^^^^ fg=#8ec07c fs= build>=4143
//             ^^ fg=#83a598 fs=
//                ^^ fg=#83a598 fs=
//                  ^ fg=#ebdbb2 fs=

$x = function(N $c) use ($a, $b) {};
//   ^ fg=#8ec07c fs= build>=4143
//           ^ fg=#83a598 fs=
//            ^ fg=#ebdbb2 fs=
//              ^ fg=#fe8019 fs=
//               ^ fg=#ebdbb2 fs=
//                ^ fg=#83a598 fs=
//                  ^^^ fg=#8ec07c fs=
//                      ^ fg=#83a598 fs=
//                       ^ fg=#fe8019 fs=
//                        ^ fg=#ebdbb2 fs=
//                         ^ fg=#ebdbb2 fs=
//                           ^ fg=#fe8019 fs=
//                            ^ fg=#ebdbb2 fs=
//                             ^ fg=#83a598 fs=
//                               ^^ fg=#83a598 fs=
//                                 ^ fg=#ebdbb2 fs=

$abc->y(function (A $a, B $b) {
// ^ fg=#ebdbb2 fs=
//  ^^ fg=#fabd2f fs=
//    ^ fg=#ebdbb2 fs=
//     ^ fg=#83a598 fs=
//      ^^^^^^^^ fg=#8ec07c fs= build>=4143
//               ^ fg=#83a598 fs=
//                ^ fg=#ebdbb2 fs=
//                  ^ fg=#fe8019 fs=
//                   ^ fg=#ebdbb2 fs=
//                    ^ fg=#ebdbb2 fs=
//                      ^ fg=#ebdbb2 fs=
//                        ^ fg=#fe8019 fs=
//                         ^ fg=#ebdbb2 fs=
//                          ^ fg=#83a598 fs=
//                            ^ fg=#83a598 fs=
    $c = $a->b('c');
//  ^ fg=#fe8019 fs=
//   ^ fg=#ebdbb2 fs=
//     ^ fg=#fe8019 fs=
//       ^ fg=#fe8019 fs=
//        ^ fg=#ebdbb2 fs=
//         ^^ fg=#fabd2f fs=
//           ^ fg=#ebdbb2 fs=
//            ^ fg=#83a598 fs=
//             ^^^ fg=#b8bb26 fs=
//                ^ fg=#83a598 fs=
//                 ^ fg=#ebdbb2 fs=
    $b->c("d $c");
//  ^ fg=#fe8019 fs=
//   ^ fg=#ebdbb2 fs=
//    ^^ fg=#fabd2f fs=
//      ^ fg=#ebdbb2 fs=
//       ^ fg=#83a598 fs=
//        ^^ fg=#b8bb26 fs=
//           ^ fg=#fe8019 fs=
//            ^ fg=#ebdbb2 fs=
//             ^ fg=#b8bb26 fs=
//              ^ fg=#83a598 fs=
//               ^ fg=#ebdbb2 fs=
    });
//  ^^ fg=#83a598 fs=
//    ^ fg=#ebdbb2 fs=

    \defined('SIGINT');
//  ^ fg=#ebdbb2 fs=
//   ^ fg=#b8bb26 fs=bold

if (isset($x) && is_callable($x)) {
//  ^^^^^ fg=#fe8019 fs=
//       ^ fg=#83a598 fs=
//        ^ fg=#fe8019 fs=
//         ^ fg=#ebdbb2 fs=
//          ^ fg=#83a598 fs=
//            ^^ fg=#fe8019 fs=
//               ^^^^^^^^^^^ fg=#b8bb26 fs=bold
//                          ^ fg=#83a598 fs=
//                           ^ fg=#fe8019 fs=
//                            ^ fg=#ebdbb2 fs=
//                             ^ fg=#83a598 fs=
//                              ^ fg=#83a598 fs=
//                                ^ fg=#83a598 fs=

    if ((29 - 10 + 2) * 2 > 4.2) {}
    // ^^ fg=#83a598 fs=
    //   ^^ fg=#d3869b fs=
    //      ^ fg=#fe8019 fs=
    //        ^^ fg=#d3869b fs=
    //           ^ fg=#fe8019 fs=
    //             ^ fg=#d3869b fs=
    //              ^ fg=#83a598 fs=
    //                ^ fg=#fe8019 fs=
    //                  ^ fg=#d3869b fs=
    //                    ^ fg=#fb4934 fs=
    //                      ^^^ fg=#d3869b fs=
    //                         ^ fg=#83a598 fs=
    //                           ^^ fg=#83a598 fs=

    $x = true | false | null;
    // ^ fg=#fe8019 fs=
    //  ^ fg=#ebdbb2 fs=
    //   ^^^^ fg=#d3869b fs=
    //        ^ fg=#fe8019 fs=
    //          ^^^^^ fg=#d3869b fs=
    //                ^ fg=#fe8019 fs=
    //                  ^^^^ fg=#fabd2f fs=
    //                      ^ fg=#ebdbb2 fs=

    $x = 0123 & 0x1A && 0b11111111 / 1.2 + 1.2e3 + 7E-10;
    //   ^^^^ fg=#d3869b fs=
    //        ^ fg=#fe8019 fs=
    //          ^^^^ fg=#d3869b fs=
    //               ^^ fg=#fe8019 fs=
    //                  ^^^^^^^^^^ fg=#d3869b fs=
    //                             ^ fg=#fe8019 fs=
    //                               ^^^ fg=#d3869b fs=
    //                                   ^ fg=#fe8019 fs=
    //                                     ^^^^^ fg=#d3869b fs=
    //                                           ^ fg=#fe8019 fs=
    //                                             ^^^^^ fg=#d3869b fs=
    //                                                  ^ fg=#ebdbb2 fs=

    $x = 014;  // Non-prefix octal literal
    //   ^^^ fg=#d3869b fs= build>=4140
    $x = 0o14; // Prefixed octal literal
    //   ^^^^ fg=#d3869b fs= build>=4140

    print("a\t\nb" . 'ab');
    // ^^ fg=#fe8019 fs=
    //   ^ fg=#83a598 fs=
    //    ^^ fg=#b8bb26 fs=
    //      ^^^^ fg=#fe8019 fs=
    //          ^^ fg=#b8bb26 fs=
    //             ^ fg=#fe8019 fs=
    //               ^^^^ fg=#b8bb26 fs=
    //                   ^ fg=#83a598 fs=
    //                    ^ fg=#ebdbb2 fs=

    $x = "_\n_\\n_\m_\\m_";
    //   ^^ fg=#b8bb26 fs=
    //     ^^ fg=#fe8019 fs=
    //       ^ fg=#b8bb26 fs=
    //        ^^ fg=#fe8019 fs=
    //          ^^^^^ fg=#b8bb26 fs=
    //               ^^ fg=#fe8019 fs=
    //                 ^^^ fg=#b8bb26 fs=
    //                    ^ fg=#ebdbb2 fs=

    user_defined();
    // ^^^^^^^^^ fg=#ebdbb2 fs=
    //          ^^ fg=#83a598 fs=
    //            ^ fg=#ebdbb2 fs=

    phpversion();
    // ^^^^^^^ fg=#b8bb26 fs=bold
    //        ^^ fg=#83a598 fs=
    //          ^ fg=#ebdbb2 fs=

    error_reporting(E_ALL);
    // ^^^^^^^^^^^^ fg=#b8bb26 fs=bold
    //             ^ fg=#83a598 fs=
    //              ^^^^^ fg=#d3869b fs=
    //                   ^ fg=#83a598 fs=
    //                    ^ fg=#ebdbb2 fs=

    $x();
//  ^ fg=#fe8019 fs=
//   ^ fg=#ebdbb2 fs=
//    ^ fg=#83a598 fs=
//     ^ fg=#83a598 fs=

    $x = $y($a, $b);
    //   ^ fg=#fe8019 fs=
    //    ^ fg=#ebdbb2 fs=
    //     ^ fg=#83a598 fs=
    //      ^ fg=#fe8019 fs=
    //       ^ fg=#ebdbb2 fs=
    //          ^ fg=#fe8019 fs=
    //           ^ fg=#ebdbb2 fs=
    //            ^ fg=#83a598 fs=

    $x = array();
    //   ^ fg=#b8bb26 fs=bold
    //        ^^ fg=#83a598 fs=
    //          ^ fg=#ebdbb2 fs=

    $x = [];
    //   ^^ fg=#83a598 fs=
    //     ^ fg=#ebdbb2 fs=

    $x = array(
    //   ^ fg=#b8bb26 fs=bold
    //        ^ fg=#83a598 fs=
        "x" => "y",
    //  ^^^ fg=#b8bb26 fs=
    //      ^^ fg=#fe8019 fs=
    //         ^^^ fg=#b8bb26 fs=
    //            ^ fg=#ebdbb2 fs=
        [
    //  ^ fg=#83a598 fs=
            "x" => "y",
    //      ^^^ fg=#b8bb26 fs=
    //          ^^ fg=#fe8019 fs=
    //             ^^^ fg=#b8bb26 fs=
    //                ^ fg=#ebdbb2 fs=
        ]
    //  ^ fg=#83a598 fs=
    );
//  ^ fg=#83a598 fs=
//   ^ fg=#ebdbb2 fs=

    $x = array_merge([
    //   ^^^^^^^^^^^ fg=#b8bb26 fs=bold
    //              ^ fg=#83a598 fs=
    //               ^ fg=#83a598 fs=
        'a' => 'b',
    //  ^^^ fg=#b8bb26 fs=
    //      ^^ fg=#fe8019 fs=
    //         ^^^ fg=#b8bb26 fs=
    //            ^ fg=#ebdbb2 fs=
        'c' => 42
    //  ^^^ fg=#b8bb26 fs=
    //      ^^ fg=#fe8019 fs=
    //         ^^ fg=#d3869b fs=
    ]);
//  ^^ fg=#83a598 fs=
//    ^ fg=#ebdbb2 fs=

        $argv['x']; $argc;
    //  ^ fg=#fe8019 fs=
    //   ^ fg=#ebdbb2 fs=
    //       ^ fg=#83a598 fs=
    //        ^^^ fg=#b8bb26 fs=
    //           ^ fg=#83a598 fs=
    //            ^ fg=#ebdbb2 fs=
    //              ^ fg=#fe8019 fs=
    //               ^ fg=#ebdbb2 fs=
    //                   ^ fg=#ebdbb2 fs=

        $_FILES; $_ENV; $GLOBALS;
    //  ^ fg=#fe8019 fs=
    //   ^ fg=#ebdbb2 fs=
    //         ^ fg=#ebdbb2 fs=
    //           ^ fg=#fe8019 fs=
    //            ^ fg=#ebdbb2 fs=
    //                ^ fg=#ebdbb2 fs=
    //                  ^ fg=#fe8019 fs=
    //                   ^ fg=#ebdbb2 fs=
    //                          ^ fg=#ebdbb2 fs=

        $_SERVER['DOCUMENT_ROOT'];
    //  ^ fg=#fe8019 fs=
    //   ^^ fg=#ebdbb2 fs=
    //          ^ fg=#83a598 fs=
    //           ^^^^^^^^^^^^^^^ fg=#b8bb26 fs=
    //                          ^ fg=#83a598 fs=

        $_GET['x']; $_POST['x']; $_COOKIE['x']; $_SESSION['x']; $_REQUEST['x'];
    //  ^ fg=#fe8019 fs=
    //   ^^ fg=#ebdbb2 fs=
    //       ^ fg=#83a598 fs=
    //        ^^^ fg=#b8bb26 fs=
    //           ^ fg=#83a598 fs=
    //            ^ fg=#ebdbb2 fs=
    //              ^ fg=#fe8019 fs=
    //               ^^^^^ fg=#ebdbb2 fs=
    //                    ^ fg=#83a598 fs=
    //                     ^^^ fg=#b8bb26 fs=
    //                        ^ fg=#83a598 fs=
    //                         ^ fg=#ebdbb2 fs=
    //                           ^ fg=#fe8019 fs=
    //                            ^^^^^^^ fg=#ebdbb2 fs=
    //                                   ^ fg=#83a598 fs=
    //                                    ^^^ fg=#b8bb26 fs=
    //                                       ^ fg=#83a598 fs=
    //                                        ^ fg=#ebdbb2 fs=
    //                                          ^ fg=#fe8019 fs=
    //                                           ^^^^^^^^ fg=#ebdbb2 fs=
    //                                                   ^ fg=#83a598 fs=
    //                                                    ^^^ fg=#b8bb26 fs=
    //                                                       ^ fg=#83a598 fs=
    //                                                        ^ fg=#ebdbb2 fs=
    //                                                          ^ fg=#fe8019 fs=
    //                                                           ^^^^^^^^ fg=#ebdbb2 fs=
    //                                                                   ^ fg=#83a598 fs=
    //                                                                    ^^^ fg=#b8bb26 fs=
    //                                                                       ^ fg=#83a598 fs=
    //                                                                        ^ fg=#ebdbb2 fs=

    $x = __FILE__ . PHP_VERSION . XYZ;
    //   ^^^^^^^^ fg=#d3869b fs=
    //            ^ fg=#fe8019 fs=
    //              ^^^^^^^^^^^ fg=#d3869b fs=
    //                          ^ fg=#fe8019 fs=
    //                            ^^^ fg=#ebdbb2 fs=
    //                               ^ fg=#ebdbb2 fs=

    echo X[1];
    //   ^ fg=#ebdbb2 fs=
    //    ^ fg=#83a598 fs=
    //     ^ fg=#d3869b fs=
    //      ^ fg=#83a598 fs=
    //       ^ fg=#ebdbb2 fs=

    echo $var['x'][1];
    // ^ fg=#fe8019 fs=
    //   ^ fg=#fe8019 fs=
    //    ^^^ fg=#ebdbb2 fs=
    //       ^ fg=#83a598 fs=
    //        ^^^ fg=#b8bb26 fs=
    //           ^^ fg=#83a598 fs=
    //             ^ fg=#d3869b fs=
    //              ^ fg=#83a598 fs=
    //               ^ fg=#ebdbb2 fs=


    $unpacking = [...$arr1, 'c' => 'd'];
    //            ^^^ fg=#fe8019 fs= build>=4140

    $x = (int) (integer) $x;
    //   ^ fg=#83a598 fs=
    //    ^ fg=#fabd2f fs=
    //       ^ fg=#83a598 fs=
    //         ^ fg=#83a598 fs=
    //           ^ fg=#fabd2f fs=
    //                 ^ fg=#83a598 fs=

    $x = (bool) (boolean) $y;
    //   ^ fg=#83a598 fs=
    //    ^ fg=#fabd2f fs=
    //        ^ fg=#83a598 fs=
    //          ^ fg=#83a598 fs=
    //           ^ fg=#fabd2f fs=
    //                  ^ fg=#83a598 fs=

    $x = (float) (double) (real) $y;
    //   ^ fg=#83a598 fs=
    //    ^ fg=#fabd2f fs=
    //         ^ fg=#83a598 fs=
    //           ^ fg=#83a598 fs=
    //            ^ fg=#fabd2f fs=
    //                  ^ fg=#83a598 fs=
    //                    ^ fg=#83a598 fs=
    //                     ^ fg=#fabd2f fs=
    //                         ^ fg=#83a598 fs=

    $x = (string) $y;
    //   ^ fg=#83a598 fs=
    //    ^ fg=#fabd2f fs=
    //          ^ fg=#83a598 fs=

    $x = (array) $y;
    //   ^ fg=#83a598 fs=
    //    ^ fg=#fabd2f fs=
    //         ^ fg=#83a598 fs=

    $x = (object) $y;
    //   ^ fg=#83a598 fs=
    //    ^ fg=#fabd2f fs=
    //          ^ fg=#83a598 fs=

    $x = (unset) $y;
    //   ^ fg=#83a598 fs=
    //    ^ fg=#fabd2f fs=
    //         ^ fg=#83a598 fs=

    $x = new stdClass();
    //   ^ fg=#8ec07c fs=
    //       ^ fg=#d3869b fs=
    //               ^^ fg=#83a598 fs=

    $x = new N();
    //   ^ fg=#8ec07c fs=
    //       ^ fg=#ebdbb2 fs=
    //        ^^ fg=#83a598 fs=

    $x = new Exception();
    //   ^ fg=#8ec07c fs=
    //       ^ fg=#d3869b fs=

    $x = new A\B\C();
    //   ^ fg=#8ec07c fs=
    //       ^^^^ fg=#ebdbb2 fs= build>=4148
    //           ^ fg=#ebdbb2 fs=
    //            ^^ fg=#83a598 fs=

    $x = new A\B\Exception();
    //       ^^^^ fg=#ebdbb2 fs= build>=4148
    //           ^ fg=#d3869b fs=

    $x = new A\B\Countable();
    //       ^^^^ fg=#ebdbb2 fs= build>=4148
    //           ^ fg=#d3869b fs=

    $x = new A\B\UserDefined();
    //       ^^^^ fg=#ebdbb2 fs= build>=4148
    //           ^ fg=#ebdbb2 fs=

    $x = new A\B\C(
    //       ^^^^ fg=#ebdbb2 fs= build>=4134
    //           ^ fg=#ebdbb2 fs= build>=4134
        $a,
        $b
    );

    clone $obj;
    // ^ fg=#8ec07c fs= build>=4134
    //    ^ fg=#fe8019 fs=
    //     ^fg=#ebdbb2 fs=

    var_dump($x instanceof X);
    //      ^ fg=#83a598 fs=
    //       ^ fg=#fe8019 fs=
    //        ^ fg=#ebdbb2 fs=
    //          ^^^^^^^^^^ fg=#fb4934 fs=
    //                     ^ fg=#ebdbb2 fs=
    //                      ^ fg=#83a598 fs=

    var_dump($x instanceof X\Y\Z);
    //                     ^^^^ fg=#ebdbb2 fs= build>=4148
    //                         ^ fg=#ebdbb2 fs=
    //                          ^ fg=#83a598 fs=

    var_dump($x instanceof Countable);
    //                     ^^^^^^^^^ fg=#d3869b fs=
    //                              ^ fg=#83a598 fs=

    var_dump($x instanceof $y);
    //                     ^ fg=#fe8019 fs=
    //                      ^ fg=#ebdbb2 fs=
    //                       ^ fg=#83a598 fs=

    $x = &$obj;
    //   ^ fg=#fe8019 fs=
    //    ^ fg=#fe8019 fs=
    //     ^ fg=#ebdbb2 fs=

    $nullSafe?->getUser(5)?->name;
    //       ^^^ fg=#fabd2f fs= build>=4140
    //                    ^^^ fg=#fabd2f fs= build>=4140
    //                       ^^^^ fg=#ebdbb2 fs= build>=4140

    add(...[1, 2]);
    // ^ fg=#83a598 fs=
    //  ^^^ fg=#fe8019 fs=
    //     ^ fg=#83a598 fs=
    //      ^ fg=#d3869b fs=
    //       ^ fg=#ebdbb2 fs=
    //         ^ fg=#d3869b fs=
    //          ^^ fg=#83a598 fs=

    echo "x $x";
    //   ^^^ fg=#b8bb26 fs=
    //      ^ fg=#fe8019 fs=
    //       ^ fg=#ebdbb2 fs=
    //        ^ fg=#b8bb26 fs=
    //         ^ fg=#ebdbb2 fs=

    echo "x ${$x}";
    //   ^^^ fg=#b8bb26 fs=
    //      ^^^ fg=#fe8019 fs=
    //         ^ fg=#ebdbb2 fs=
    //          ^ fg=#fe8019 fs=
    //           ^ fg=#b8bb26 fs=
    //            ^ fg=#ebdbb2 fs=

    echo "x $x[0]";
    //   ^^^ fg=#b8bb26 fs=
    //      ^ fg=#fe8019 fs=
    //       ^ fg=#ebdbb2 fs=
    //        ^ fg=#83a598 fs=
    //         ^ fg=#d3869b fs=
    //          ^ fg=#83a598 fs=
    //           ^ fg=#b8bb26 fs=
    //            ^ fg=#ebdbb2 fs=

    echo "x $x[xyz]";
    //   ^^^ fg=#b8bb26 fs=
    //      ^ fg=#fe8019 fs=
    //       ^ fg=#ebdbb2 fs=
    //        ^ fg=#83a598 fs=
    //         ^^^ fg=#ebdbb2 fs=
    //            ^ fg=#83a598 fs=
    //             ^ fg=#b8bb26 fs=
    //              ^ fg=#ebdbb2 fs=

    echo "x $x->y";
    //   ^^^ fg=#b8bb26 fs=
    //      ^ fg=#fe8019 fs=
    //       ^ fg=#ebdbb2 fs=
    //        ^^ fg=#fabd2f fs=
    //          ^ fg=#ebdbb2 fs=
    //           ^ fg=#b8bb26 fs=
    //            ^ fg=#ebdbb2 fs=

    echo "{$x} {$x->y} {$x['y']}";
    //   ^ fg=#b8bb26 fs=
    //    ^ fg=#83a598 fs=
    //     ^ fg=#fe8019 fs=
    //      ^ fg=#ebdbb2 fs=
    //       ^ fg=#83a598 fs=
    //        ^ fg=#b8bb26 fs=
    //         ^ fg=#83a598 fs=
    //          ^ fg=#fe8019 fs=
    //           ^ fg=#ebdbb2 fs=
    //            ^^ fg=#fabd2f fs=
    //              ^ fg=#ebdbb2 fs=
    //               ^ fg=#83a598 fs=
    //                ^ fg=#b8bb26 fs=
    //                 ^ fg=#83a598 fs=
    //                  ^ fg=#fe8019 fs=
    //                   ^ fg=#ebdbb2 fs=
    //                    ^ fg=#83a598 fs=
    //                     ^^^ fg=#b8bb26 fs=
    //                        ^^ fg=#83a598 fs=
    //                          ^ fg=#b8bb26 fs=
    //                           ^ fg=#ebdbb2 fs=

    echo "x {${$name}}";
    //   ^^^ fg=#b8bb26 fs=
    //      ^ fg=#83a598 fs=
    //       ^ fg=#fe8019 fs= build>=4092
    //        ^ fg=#fe8019 fs= build>=4134
    //         ^ fg=#fe8019 fs=
    //          ^^^^ fg=#ebdbb2 fs=
    //              ^ fg=#fe8019 fs=
    //               ^ fg=#83a598 fs= build>=4134
    //                ^ fg=#b8bb26 fs= build>=4134
    //                 ^ fg=#ebdbb2 fs= build>=4134

    echo "x {$x->$y}";
    //   ^^^ fg=#b8bb26 fs=
    //      ^ fg=#83a598 fs=
    //       ^ fg=#fe8019 fs=
    //        ^ fg=#ebdbb2 fs=
    //         ^^ fg=#fabd2f fs=
    //           ^ fg=#fe8019 fs=
    //            ^ fg=#ebdbb2 fs=
    //             ^ fg=#83a598 fs=
    //              ^ fg=#b8bb26 fs=
    //               ^ fg=#ebdbb2 fs=

    echo "x {$x->{$y[1]}} z";
    //   ^^^ fg=#b8bb26 fs=
    //      ^ fg=#83a598 fs=
    //       ^ fg=#fe8019 fs=
    //        ^ fg=#ebdbb2 fs=
    //         ^^ fg=#fabd2f fs=
    //           ^ fg=#fe8019 fs=
    //            ^ fg=#fe8019 fs=
    //             ^ fg=#ebdbb2 fs=
    //              ^ fg=#83a598 fs=
    //               ^ fg=#d3869b fs=
    //                ^ fg=#83a598 fs=
    //                 ^ fg=#fe8019 fs=
    //                  ^ fg=#83a598 fs=
    //                   ^^^ fg=#b8bb26 fs=
    //                      ^ fg=#ebdbb2 fs=

    echo '/x/{y}';
    //   ^^^^^^^^ fg=#b8bb26 fs=
    //           ^ fg=#ebdbb2 fs=

    $test = <<<EOT
//  ^ fg=#fe8019 fs=
//   ^ fg=#ebdbb2 fs=
//        ^ fg=#fe8019 fs= build>=4134
//          ^^^ fg=#fe8019 fs= build>=4134 -->
//             ^^^ fg=#83a598 fs= build>=4134 -->
<div>
    <p>$x</p>
//  ^^^ fg=#b8bb26 fs=
//     ^ fg=#fe8019 fs=
//      ^ fg=#ebdbb2 fs=
//       ^^^^ fg=#b8bb26 fs=
    <p>${x}</p>
//  ^^^ fg=#b8bb26 fs=
//     ^ fg=#fe8019 fs= build>=4134
//      ^ fg=#fe8019 fs= build>=4134
//       ^ fg=#ebdbb2 fs= build>=4134
//        ^ fg=#fe8019 fs= build>=4134
//         ^^^^ fg=#b8bb26 fs=
    <p>{$x}</p>
//  ^^^ fg=#b8bb26 fs=
//     ^ fg=#83a598 fs=
//      ^ fg=#fe8019 fs=
//       ^ fg=#ebdbb2 fs=
//        ^ fg=#83a598 fs=
//         ^^^^ fg=#b8bb26 fs=
    <p>{ $x }</p>
//  ^^^^ fg=#b8bb26 fs=
//       ^ fg=#fe8019 fs=
//        ^ fg=#ebdbb2 fs=
//          ^^^^^ fg=#b8bb26 fs=
    <p>{$x[1]}</p>
//  ^^^ fg=#b8bb26 fs=
//     ^ fg=#83a598 fs=
//      ^ fg=#fe8019 fs=
//       ^ fg=#ebdbb2 fs=
//        ^ fg=#83a598 fs=
//         ^ fg=#d3869b fs=
//          ^^ fg=#83a598 fs=
//            ^^^^ fg=#b8bb26 fs=
    <p>{$x['y']}</p>
//  ^^^ fg=#b8bb26 fs=
//     ^ fg=#83a598 fs=
//      ^ fg=#fe8019 fs=
//       ^ fg=#ebdbb2 fs=
//        ^ fg=#83a598 fs=
//         ^^^ fg=#b8bb26 fs=
//            ^^ fg=#83a598 fs=
//              ^^^^ fg=#b8bb26 fs=
    <p>$x->y</p>
//  ^^^ fg=#b8bb26 fs=
//     ^ fg=#fe8019 fs=
//      ^ fg=#ebdbb2 fs=
//       ^^ fg=#fabd2f fs=
//         ^ fg=#ebdbb2 fs=
//          ^^^^ fg=#b8bb26 fs=
    <p>{$x->y}</p>
//  ^^^ fg=#b8bb26 fs=
//     ^ fg=#83a598 fs=
//      ^ fg=#fe8019 fs=
//       ^ fg=#ebdbb2 fs=
//        ^^ fg=#fabd2f fs=
//          ^ fg=#ebdbb2 fs=
//           ^ fg=#83a598 fs=
//            ^^^^ fg=#b8bb26 fs=
    <p>{$x->y[1]}</p>
//  ^^^ fg=#b8bb26 fs=
//     ^ fg=#83a598 fs=
//      ^ fg=#fe8019 fs=
//       ^ fg=#ebdbb2 fs=
//        ^^ fg=#fabd2f fs=
//          ^ fg=#ebdbb2 fs=
//           ^ fg=#83a598 fs=
//            ^ fg=#d3869b fs=
//             ^^ fg=#83a598 fs=
//               ^^^^ fg=#b8bb26 fs=
    <p>{$x->y()}</p>
//  ^^^ fg=#b8bb26 fs=
//     ^ fg=#83a598 fs=
//      ^ fg=#fe8019 fs=
//       ^ fg=#ebdbb2 fs=
//        ^^ fg=#fabd2f fs=
//          ^ fg=#ebdbb2 fs=
//           ^^ fg=#83a598 fs=
//             ^ fg=#83a598 fs=
//              ^^^^ fg=#b8bb26 fs=
    <p>{$x->y()->z()}</p>
//  ^^^ fg=#b8bb26 fs=
//     ^ fg=#83a598 fs=
//      ^ fg=#fe8019 fs=
//       ^ fg=#ebdbb2 fs=
//        ^^ fg=#fabd2f fs=
//          ^ fg=#ebdbb2 fs=
//           ^^ fg=#83a598 fs=
//             ^^ fg=#fabd2f fs=
//               ^ fg=#ebdbb2 fs=
//                ^^ fg=#83a598 fs=
//                  ^ fg=#83a598 fs=
//                   ^^^^ fg=#b8bb26 fs=
    <p>{$this->y()}</p>
//     ^ fg=#83a598 fs=
//      ^ fg=#fe8019 fs=
//       ^^^^ fg=#ebdbb2 fs=
//           ^^ fg=#fabd2f fs=
//             ^ fg=#ebdbb2 fs=
//              ^^^ fg=#83a598 fs=
</div>
EOT;
//^ fg=#83a598 fs=
// ^ fg=#ebdbb2 fs=

    $x = <<<'EOT'
//  ^ fg=#fe8019 fs=
//   ^ fg=#ebdbb2 fs=
//     ^ fg=#fe8019 fs=
//       ^^^ fg=#fe8019 fs=
//          ^^^^^ fg=#83a598 fs=
<div>
    <p>$x</p>
//  ^^^^^^^^^ fg=#b8bb26 fs=
    <p>{$x}</p>
//  ^^^^^^^^^^^ fg=#b8bb26 fs=
    <p>$x->y</p>
//  ^^^^^^^^^^^^ fg=#b8bb26 fs=
    <p>{$x->y[1]}</p>
//  ^^^^^^^^^^^^^^^^^ fg=#b8bb26 fs=
</div>
EOT;
//^ fg=#83a598 fs=
// ^ fg=#ebdbb2 fs=

    $x = <<<XML
<!--^ fg=#fe8019 fs= build>=3154 -->
<!-- ^ fg=#ebdbb2 fs= build>=3154 -->
<!--   ^ fg=#fe8019 fs= build>=3154 -->
<!--     ^^^ fg=#fe8019 fs= build>=3154 -->
<!--        ^^^ fg=#83a598 fs= build>=3154 -->
<?xml version="1.0" encoding="UTF-8"?>
<!--^ fg=#8ec07c fs= build>=3154 -->
<!--  ^^^^^^^ fg=#8ec07c fs= build>=3154 -->
<!--         ^ fg=#fe8019 fs= build>=3154 -->
<!--          ^^^^^ fg=#b8bb26 fs= build>=3154 -->
<!--                ^^^^^^^^ fg=#8ec07c fs= build>=3154 -->
<!--                        ^ fg=#fe8019 fs= build>=3154 -->
<!--                         ^^^^^^^ fg=#b8bb26 fs= build>=3154 -->
<!--                                ^^ fg=#83a598 fs= build>=3154 -->
    <food>
<!--^ fg=#83a598 fs= build>=3154 -->
    <!--^ fg=#b8bb26 fs= build>=3154 -->
    <!-- ^ fg=#83a598 fs= build>=3154 -->
        <name>Belgian Waffles</name>
    <!--^ fg=#83a598 fs= build>=3154 -->
        <!--^ fg=#b8bb26 fs= build>=3154 -->
        <!-- ^ fg=#83a598 fs= build>=3154 -->
        <!--  ^ fg=#ebdbb2 fs= build>=3154 -->
        <!--                 ^^ fg=#83a598 fs= build>=3154 -->
        <!--                   ^ fg=#b8bb26 fs= build>=3154 -->
        <!--                       ^ fg=#83a598 fs= build>=3154 -->
    </food>
</xml>
XML;
//^ fg=#83a598 fs= build>=3154
// ^ fg=#ebdbb2 fs= build>=3154

    $x = <<<CSS
/*  ^ fg=#fe8019 fs= build>=3154 */
/*   ^ fg=#ebdbb2 fs= build>=3154 */
/*     ^ fg=#fe8019 fs= build>=3154 */
/*       ^^^ fg=#fe8019 fs= build>=3154 */
/*          ^^^ fg=#83a598 fs= build>=3154 */
    body {}
/*  ^^^^ fg=#fb4934 fs= build>=3154 */
/*       ^^ fg=#83a598 fs= build>=3154 */

    #id {}
/*  ^^^ fg=#8ec07c fs= build>=3154 */
/*      ^^ fg=#83a598 fs= build>=3154 */

    .class {}
/*  ^^^^^^ fg=#b8bb26 fs= build>=3154 */
/*         ^^ fg=#83a598 fs= build>=3154 */
CSS;
//^ fg=#83a598 fs= build>=3154
// ^ fg=#ebdbb2 fs= build>=3154

    if (x('y') && $x instanceof Countable) {
    // ^ fg=#83a598 fs=
    //  ^ fg=#ebdbb2 fs=
    //   ^ fg=#83a598 fs=
    //    ^^^ fg=#b8bb26 fs=
    //       ^ fg=#83a598 fs=
    //         ^^ fg=#fe8019 fs=
    //            ^ fg=#fe8019 fs=
    //             ^ fg=#ebdbb2 fs=
    //               ^^^^^^^^^^ fg=#fb4934 fs=
    //                          ^^^^^^^^^ fg=#d3869b fs=
    //                                   ^ fg=#83a598 fs=
    //                                     ^ fg=#83a598 fs=

        for ($i = 0; $i < 2; $i++) {}
        //^ fg=#fb4934 fs=
        //  ^ fg=#83a598 fs=
        //   ^ fg=#fe8019 fs=
        //    ^ fg=#ebdbb2 fs=
        //      ^ fg=#fe8019 fs=
        //        ^ fg=#d3869b fs=
        //         ^ fg=#ebdbb2 fs=
        //           ^ fg=#fe8019 fs=
        //            ^ fg=#ebdbb2 fs=
        //              ^ fg=#fb4934 fs=
        //                ^ fg=#d3869b fs=
        //                 ^ fg=#ebdbb2 fs=
        //                   ^ fg=#fe8019 fs=
        //                    ^ fg=#ebdbb2 fs=
        //                     ^^ fg=#fe8019 fs=
        //                       ^ fg=#83a598 fs=
        //                         ^^ fg=#83a598 fs=

        foreach ($x as $y) {
        // ^ fg=#fb4934 fs=
        //      ^ fg=#83a598 fs=
        //       ^ fg=#fe8019 fs=
        //        ^ fg=#ebdbb2 fs=
        //          ^^ fg=#fb4934 fs=
        //             ^ fg=#fe8019 fs=
        //              ^ fg=#ebdbb2 fs=
        //               ^ fg=#83a598 fs=
        //                 ^ fg=#83a598 fs=
            continue;
            // ^ fg=#fb4934 fs=
            //      ^ fg=#ebdbb2 fs=
        }
    //  ^ fg=#83a598 fs=

        switch ($expr) {
        // ^ fg=#fb4934 fs=
        //     ^ fg=#83a598 fs=
        //      ^ fg=#fe8019 fs=
        //       ^ fg=#ebdbb2 fs=
        //           ^ fg=#83a598 fs=
        //             ^ fg=#83a598 fs=

            case 1:
            // ^ fg=#fb4934 fs=
            //   ^ fg=#d3869b fs=
            //    ^ fg=#fe8019 fs=
                break;
                // ^ fg=#fb4934 fs=
                //   ^ fg=#ebdbb2 fs=

            default:
            // ^ fg=#fb4934 fs=
            //     ^ fg=#fe8019 fs=
                break;
                // ^ fg=#fb4934 fs=
                //   ^ fg=#ebdbb2 fs=
        }
    //  ^ fg=#83a598 fs=

        try {
        //^ fg=#fb4934 fs=
        //  ^ fg=#83a598 fs=

        } catch (Exception $e) {
    //  ^ fg=#83a598 fs=
        // ^ fg=#fb4934 fs=
        //      ^ fg=#83a598 fs=
        //       ^ fg=#d3869b fs=
        //                 ^ fg=#fe8019 fs=
        //                  ^ fg=#ebdbb2 fs=
        //                   ^ fg=#83a598 fs=
        //                     ^ fg=#83a598 fs=

        } finally {
    //  ^ fg=#83a598 fs=
        // ^ fg=#fb4934 fs=
        //        ^ fg=#83a598 fs=

        }
    //  ^ fg=#83a598 fs=

        while (1 >= 3) {}
        // ^ fg=#fb4934 fs=
        //    ^ fg=#83a598 fs=
        //     ^ fg=#d3869b fs=
        //       ^^ fg=#fb4934 fs=
        //          ^ fg=#d3869b fs=
        //           ^ fg=#83a598 fs=
        //             ^^ fg=#83a598 fs=

        do {
    //  ^ fg=#fb4934 fs=
        // ^ fg=#83a598 fs=
        } while (0);
    //  ^ fg=#83a598 fs=
        // ^ fg=#fb4934 fs=
        //      ^ fg=#83a598 fs=
        //       ^ fg=#d3869b fs=
        //        ^ fg=#83a598 fs=
        //         ^ fg=#ebdbb2 fs=

        if (0) {
    //  ^^ fg=#fb4934 fs=
        // ^ fg=#83a598 fs=
        //  ^ fg=#d3869b fs=
        //   ^ fg=#83a598 fs=
        //     ^ fg=#83a598 fs=
        } elseif ($arg != 1) {
        //             ^^ fg=#fb4934 fs=
        } elseif ($arg !== 1) {
        //             ^^^ fg=#fb4934 fs=
        } elseif ($arg == 1) {
        //             ^^ fg=#fb4934 fs=
        } elseif ($arg === 1) {
    //  ^ fg=#83a598 fs=
        // ^^^^^ fg=#fb4934 fs=
        //       ^ fg=#83a598 fs=
        //        ^ fg=#fe8019 fs=
        //         ^ fg=#ebdbb2 fs=
        //             ^^^ fg=#fb4934 fs=
        //                 ^ fg=#d3869b fs=
        //                  ^ fg=#83a598 fs=
        //                    ^ fg=#83a598 fs=
        } else {
    //  ^ fg=#83a598 fs=
        // ^^^ fg=#fb4934 fs=
        //     ^ fg=#83a598 fs=
        }
    //  ^ fg=#83a598 fs=
    }
//  ^ fg=#83a598 fs=
}

     ?>
<!-- ^^ fg=#83a598 fs= -->
    <?php
//  ^^^^^ fg=#83a598 fs=
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

/**
 * @param int $x desc
// ^^^^^^ fg=#8ec07c fs= build>=4000
//        ^^^ fg=#928374 fs=italic
//            ^^ fg=#928374 fs=italic
//               ^^^^ fg=#928374 fs=italic
 */

/**
 * @param X $x desc
// ^^^^^^ fg=#8ec07c fs= build>=4000
//        ^ fg=#928374 fs=italic
//          ^^ fg=#928374 fs=italic
//             ^^^^ fg=#928374 fs=italic
 */

/**
 * @return int
// ^^^^^^^ fg=#8ec07c fs= build>=4000
//         ^^^ fg=#928374 fs=italic
 */

?>

    <?php if ($expr == true): ?>
<!--^^^^^ fg=#83a598 fs= -->
<!--      ^^ fg=#fb4934 fs= -->
<!--         ^ fg=#83a598 fs= -->
<!--          ^ fg=#fe8019 fs= -->
<!--           ^ fg=#ebdbb2 fs= -->
<!--                ^^ fg=#fb4934 fs= -->
<!--                   ^^^^ fg=#d3869b fs= -->
<!--                       ^ fg=#83a598 fs= -->
<!--                        ^ fg=#fe8019 fs= -->
<!--                          ^^ fg=#83a598 fs= -->
        Text
<!--    ^^^^ fg=#ebdbb2 fs= -->
    <?php else: ?>
<!--^^^^^ fg=#83a598 fs= -->
<!--      ^^^^ fg=#fb4934 fs= -->
<!--          ^ fg=#fe8019 fs= -->
<!--            ^^ fg=#83a598 fs= -->
        Text
<!--    ^^^^ fg=#ebdbb2 fs= -->
    <?php endif; ?>
<!--^^^^^ fg=#83a598 fs= -->
<!--      ^^^^^ fg=#fb4934 fs= -->
<!--           ^ fg=#ebdbb2 fs= -->
<!--             ^^ fg=#83a598 fs= -->

<?php


class x
{
    const X = 1;
    // ^ fg=#fb4934 fs=
    //    ^ fg=#ebdbb2 fs=
    //      ^ fg=#fe8019 fs=
    //        ^ fg=#d3869b fs=
    //         ^ fg=#ebdbb2 fs=

    public const X2 = 1;
    // ^ fg=#fabd2f fs= build>=4140
    //     ^ fg=#fb4934 fs= build>=4140

    final public const X3 = "foo";
    // ^ fg=#fabd2f fs= build>=4140
    //    ^ fg=#fabd2f fs= build>=4140
    //           ^ fg=#fb4934 fs= build>=4140

    public $a;
    // ^ fg=#fabd2f fs=
    //     ^ fg=#fe8019 fs=
    //      ^ fg=#ebdbb2 fs=

    protected $b;
    // ^ fg=#fabd2f fs=

    private $c;
    // ^ fg=#fabd2f fs=

    public static $d;
    // ^ fg=#fabd2f fs=
    //     ^ fg=#fabd2f fs=

    protected Fizz&Buzz $test;
    //        ^^^^ fg=#ebdbb2 fs= build>=4134
    //            ^ fg=#fe8019 fs= build>=4134
    //             ^^^^ fg=#ebdbb2 fs= build>=4134
    //                  ^ fg=#fe8019 fs=
    //                   ^^^^^ fg=#ebdbb2 fs=

    public readonly string $readonly;
    //     ^ fg=#fabd2f fs= build>=4140

    public function a() {}
    // ^ fg=#fabd2f fs=
    //     ^ fg=#8ec07c fs= build>=4143
    //              ^ fg=#ebdbb2 fs=
    //               ^^ fg=#83a598 fs=
    //                  ^^ fg=#83a598 fs=

    public static function b() {}
    //     ^ fg=#fabd2f fs=

    abstract public function c();
    // ^ fg=#fabd2f fs=

    final public function d() {}
    // ^ fg=#fabd2f fs=

    public function __construct() {}
    //              ^^^^^^^^^^^ fg=#fe8019 fs=

    public function __toString() {}
    //              ^^^^^^^^^^ fg=#fe8019 fs=

    public function e()
    {
        user_defined();
        // ^^^^^^^^^ fg=#ebdbb2 fs=
        //          ^^ fg=#83a598 fs=
        //            ^ fg=#ebdbb2 fs=

        phpversion();
        // ^ fg=#b8bb26 fs=bold
        //        ^^ fg=#83a598 fs=
        //          ^ fg=#ebdbb2 fs=

        parent::a();
        // ^ fg=#fabd2f fs=
        //    ^^ fg=#fe8019 fs=
        //      ^ fg=#ebdbb2 fs=
        //       ^^ fg=#83a598 fs=

        self::class;
        // ^ fg=#ebdbb2 fs=
        //  ^^ fg=#fe8019 fs=
        //    ^^^^^ fg=#fabd2f fs=
        //         ^ fg=#ebdbb2 fs=

        self::$x;
        // ^ fg=#ebdbb2 fs=
        //  ^^ fg=#fe8019 fs=
        //    ^ fg=#fe8019 fs=
        //     ^ fg=#ebdbb2 fs=

        self::a();
        // ^ fg=#ebdbb2 fs=
        //  ^^ fg=#fe8019 fs=
        //    ^ fg=#ebdbb2 fs=
        //     ^^ fg=#83a598 fs=

        static::$x;
        // ^ fg=#fabd2f fs=
        //    ^^ fg=#fe8019 fs=
        //      ^ fg=#fe8019 fs=
        //       ^ fg=#ebdbb2 fs=

        static::a();
        // ^ fg=#fabd2f fs=
        //    ^^ fg=#fe8019 fs=
        //      ^ fg=#ebdbb2 fs=
        //       ^^ fg=#83a598 fs=

        $this->x;
        // ^ fg=#ebdbb2 fs=
        //   ^^ fg=#fabd2f fs=
        //     ^^ fg=#ebdbb2 fs=

        $this->a();
        // ^ fg=#ebdbb2 fs=
        //   ^^ fg=#fabd2f fs=
        //     ^ fg=#ebdbb2 fs=
        //      ^^ fg=#83a598 fs=

        $this->$x();
        // ^ fg=#ebdbb2 fs=
        //   ^^ fg=#fabd2f fs=
        //     ^ fg=#fe8019 fs=
        //      ^ fg=#ebdbb2 fs=
        //       ^ fg=#83a598 fs=
        //        ^ fg=#83a598 fs=

        $this->a()->c()->d();
        // ^ fg=#ebdbb2 fs=
        //   ^^ fg=#fabd2f fs=
        //     ^ fg=#ebdbb2 fs=
        //      ^^ fg=#83a598 fs=
        //        ^^ fg=#fabd2f fs=
        //          ^ fg=#ebdbb2 fs=
        //           ^^ fg=#83a598 fs=
        //             ^^ fg=#fabd2f fs=
        //               ^ fg=#ebdbb2 fs=
        //                ^^ fg=#83a598 fs=

        Abcd::$x;
        // ^ fg=#ebdbb2 fs=
        //  ^^ fg=#fe8019 fs=
        //    ^ fg=#fe8019 fs=
        //     ^ fg=#ebdbb2 fs=

        Abcd::X;
        // ^ fg=#ebdbb2 fs=
        //  ^^ fg=#fe8019 fs=
        //    ^ fg=#ebdbb2 fs=
        //     ^ fg=#ebdbb2 fs=

        echo X::class;
        // ^ fg=#fe8019 fs=
        //   ^ fg=#ebdbb2 fs=
        //    ^^ fg=#fe8019 fs=
        //      ^^^^^ fg=#fabd2f fs=
        //           ^ fg=#ebdbb2 fs=

        $x = new X();
        //   ^ fg=#8ec07c fs=
        //       ^ fg=#ebdbb2 fs=
        //        ^^ fg=#83a598 fs=

        $x = new self();
        //   ^ fg=#8ec07c fs=
        //       ^ fg=#ebdbb2 fs=
        //           ^^ fg=#83a598 fs=

        $x = new static();
        //   ^ fg=#8ec07c fs=
        //       ^ fg=#fabd2f fs=
        //             ^^ fg=#83a598 fs=

        $x = new A\B\C();
        //   ^ fg=#8ec07c fs= build>=4134
        //       ^^^^ fg=#ebdbb2 fs= build>=4134
        //           ^ fg=#ebdbb2 fs= build>=4134
        //            ^^ fg=#83a598 fs= build>=4134

        $abc->a();
        // ^ fg=#ebdbb2 fs=
        //  ^^ fg=#fabd2f fs=
        //    ^ fg=#ebdbb2 fs=
        //     ^^ fg=#83a598 fs=

        $abc::a();
        // ^ fg=#ebdbb2 fs=
        //  ^^ fg=#fe8019 fs=
        //    ^ fg=#ebdbb2 fs=
        //     ^^ fg=#83a598 fs=

        $abc::$x;
        // ^ fg=#ebdbb2 fs=
        //  ^^ fg=#fe8019 fs=
        //    ^ fg=#fe8019 fs=
        //     ^ fg=#ebdbb2 fs=

        $abc->$x();
        // ^ fg=#ebdbb2 fs=
        //  ^^ fg=#fabd2f fs=
        //    ^ fg=#fe8019 fs=
        //     ^ fg=#ebdbb2 fs=

        $this->x = array_merge($this->y, $z);
        // ^ fg=#ebdbb2 fs=
        //   ^^ fg=#fabd2f fs=
        //     ^ fg=#ebdbb2 fs=
        //       ^ fg=#fe8019 fs=
        //         ^ fg=#b8bb26 fs=bold
        //                    ^ fg=#83a598 fs=
        //                     ^ fg=#fe8019 fs=
        //                      ^ fg=#ebdbb2 fs=
        //                          ^^ fg=#fabd2f fs=
        //                            ^^ fg=#ebdbb2 fs=
        //                               ^ fg=#fe8019 fs=
        //                                ^ fg=#ebdbb2 fs=

        $this->x($k, $v);
        // ^ fg=#ebdbb2 fs=
        //     ^ fg=#ebdbb2 fs=
        //      ^ fg=#83a598 fs=
        //       ^ fg=#fe8019 fs=
        //        ^ fg=#ebdbb2 fs=
        //           ^ fg=#fe8019 fs=
        //            ^ fg=#ebdbb2 fs=
        //             ^ fg=#83a598 fs=

        $a = isset($this->b) ? $this->b->c('d') : new X();
        // ^ fg=#fe8019 fs=
        //   ^^^^^ fg=#fe8019 fs=
        //        ^ fg=#83a598 fs=
        //         ^ fg=#fe8019 fs=
        //          ^ fg=#ebdbb2 fs=
        //              ^^ fg=#fabd2f fs=
        //                ^ fg=#ebdbb2 fs=
        //                 ^ fg=#83a598 fs=
        //                   ^ fg=#fe8019 fs= build>=4085
        //                     ^ fg=#fe8019 fs=
        //                      ^^^^ fg=#ebdbb2 fs=
        //                          ^^ fg=#fabd2f fs=
        //                            ^ fg=#ebdbb2 fs=
        //                             ^ fg=#fabd2f fs=
        //                              ^ fg=#fabd2f fs=
        //                               ^ fg=#ebdbb2 fs=
        //                                ^ fg=#83a598 fs=
        //                                 ^^^ fg=#b8bb26 fs=
        //                                    ^ fg=#83a598 fs=
        //                                      ^ fg=#fe8019 fs= build>=4085
        //                                        ^^^ fg=#8ec07c fs=
        //                                            ^ fg=#ebdbb2 fs=
        //                                             ^^ fg=#83a598 fs=

        if (!in_array($x, [false, 'a', 'b'], true)) {
        // ^ fg=#83a598 fs=
        //  ^ fg=#fe8019 fs=
        //   ^ fg=#b8bb26 fs=bold
        //           ^ fg=#83a598 fs=
        //            ^ fg=#fe8019 fs=
        //             ^ fg=#ebdbb2 fs=
        //                ^ fg=#83a598 fs=
        //                 ^^^^^ fg=#d3869b fs=
        //                      ^ fg=#ebdbb2 fs=
        //                        ^^^ fg=#b8bb26 fs=
        //                           ^ fg=#ebdbb2 fs=
        //                             ^^^ fg=#b8bb26 fs=
        //                                ^ fg=#83a598 fs=
        //                                 ^ fg=#ebdbb2 fs=
        //                                   ^^^^ fg=#d3869b fs=
        //                                       ^^ fg=#83a598 fs=
        //                                          ^ fg=#83a598 fs=
            throw new InvalidArgumentException('x');
            // ^ fg=#fb4934 fs=
            //    ^ fg=#8ec07c fs=
            //        ^ fg=#d3869b fs=
            //                                ^ fg=#83a598 fs=
            //                                 ^^^ fg=#b8bb26 fs=
            //                                    ^ fg=#83a598 fs=
        }

        if (isset(static::$x[$y])) {}
        // ^ fg=#83a598 fs=
        //  ^^^^^ fg=#fe8019 fs=
        //       ^ fg=#83a598 fs=
        //        ^^^^^^ fg=#fabd2f fs=
        //              ^^ fg=#fe8019 fs=
        //                ^ fg=#fe8019 fs=
        //                 ^ fg=#ebdbb2 fs=
        //                  ^ fg=#83a598 fs=
        //                   ^ fg=#fe8019 fs=
        //                    ^ fg=#ebdbb2 fs=
        //                     ^ fg=#83a598 fs=
        //                      ^^ fg=#83a598 fs=
        //                         ^^ fg=#83a598 fs=

        \defined('SIGINT');
    //  ^ fg=#ebdbb2 fs= build>=4000

        \A\B::class;
    //  ^ fg=#ebdbb2 fs= build>=4000
    //   ^ fg=#ebdbb2 fs= build>=4000
    //    ^ fg=#ebdbb2 fs= build>=4000
    //     ^ fg=#ebdbb2 fs=

        return new self();
        // ^ fg=#fb4934 fs=
        //     ^ fg=#8ec07c fs=
        //         ^^^^ fg=#ebdbb2 fs=
        //             ^^ fg=#83a598 fs=
    }

    public function x(callable $v, int $v2, string $v3) {}
    // ^ fg=#fabd2f fs=
    //     ^ fg=#8ec07c fs= build>=4143
    //              ^ fg=#ebdbb2 fs=
    //               ^ fg=#83a598 fs=
    //                ^^^^^^^^ fg=#fabd2f fs=
    //                         ^ fg=#fe8019 fs=
    //                          ^ fg=#ebdbb2 fs=
    //                           ^ fg=#ebdbb2 fs=
    //                             ^^^ fg=#fabd2f fs=
    //                                 ^ fg=#fe8019 fs=
    //                                  ^ fg=#ebdbb2 fs=
    //                                    ^ fg=#ebdbb2 fs=
    //                                      ^^^^^^ fg=#fabd2f fs=
    //                                             ^ fg=#fe8019 fs=
    //                                              ^ fg=#ebdbb2 fs=
    //                                                ^ fg=#83a598 fs=
    //                                                  ^^ fg=#83a598 fs=
}

class ClassNamespaces extends Extended
//    ^ fg=#ebdbb2 fs= build>=4000
//                            ^^ fg=#ebdbb2 fs= b>=4168
{
    use Used;
    //  ^ fg=#ebdbb2 fs= build>=4168
    use \Fi\zz\Buzz;
    //   ^^ fg=#ebdbb2 fs= build>=4168
    //      ^^ fg=#ebdbb2 fs= build>=4168
    //         ^^ fg=#ebdbb2 fs= build>=4168

    protected $x = [
        \A\B::class,
    //  ^^^ fg=#ebdbb2 fs= build>=4000
        \A\B\C::class,
    //  ^^^^^ fg=#ebdbb2 fs= build>=4000
    ];
}

class ConstructorPromotion
{
    public function __construct(public int $x, protected int $y = 0)
    //                          ^ fg=#fabd2f fs= build>=4140
    //                                            ^ fg=#fabd2f fs= build>=4140
    {
    }
}

enum Suit
// ^ fg=#fabd2f fs= build>=4140
//   ^ fg=#ebdbb2 fs= build>=4140
{
    case Hearts;
//  ^ fg=#fb4934 fs=
//       ^ fg=#ebdbb2 fs= build>=4140
}

    #[Attribute]
//  ^^ fg=#83a598 fs= build>=4168
//      ^ fg=#b8bb26 fs=bold build>=4168
//             ^ fg=#83a598 fs= build>=4168
    class Title { }

    #[\Attribute]
//  ^^ fg=#83a598 fs= build>=4168
//      ^ fg=#b8bb26 fs=bold build>=4168
//              ^ fg=#83a598 fs= build>=4168
    class Title { }

    #[\Fizz\Buzz\Attribute]
//  ^^ fg=#83a598 fs= build>=4168
//                  ^ fg=#b8bb26 fs=bold build>=4168
//                        ^ fg=#83a598 fs= build>=4168
    class Title { }

array_merge();
// ^ fg=#b8bb26 fs=bold
bcadd();
// ^ fg=#b8bb26 fs=bold
count();
// ^ fg=#b8bb26 fs=bold
ctype_cntrl();
// ^ fg=#b8bb26 fs=bold
date_diff();
// ^ fg=#b8bb26 fs=bold
imagesx();
// ^ fg=#b8bb26 fs=bold
pcntl_wait();
// ^ fg=#b8bb26 fs=bold
session_start();
// ^ fg=#b8bb26 fs=bold
str_getcsv();
// ^ fg=#b8bb26 fs=bold
strcspn();
// ^ fg=#b8bb26 fs=bold
var_dump();
// ^ fg=#b8bb26 fs=bold
