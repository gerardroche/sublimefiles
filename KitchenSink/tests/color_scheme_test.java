// COLOR SCHEME TEST "GruvboxDark.sublime-color-scheme" "Java"

package hi;
// ^ fg=#8ec07c fs=
//      ^^ fg=#ebdbb2 fs= build>=3157
//        ^ fg=#ebdbb2 fs=

import java.util.HashMap;
// ^ fg=#8ec07c fs=
//     ^^^^ fg=#ebdbb2 fs= build>=4125
//         ^ fg=#ebdbb2 fs= build>=3157
//          ^^^^ fg=#ebdbb2 fs= build>=4125
//              ^ fg=#ebdbb2 fs= build>=3157
//               ^^^^^^^ fg=#ebdbb2 fs= build>=4125
//                      ^ fg=#ebdbb2 fs=
import javax.swing.*;
//     ^^^^^ fg=#ebdbb2 fs= build>=4125
//          ^ fg=#ebdbb2 fs= build>=3157
//           ^^^^^ fg=#ebdbb2 fs= build>=4125
//                ^ fg=#ebdbb2 fs= build>=3150
//                 ^ fg=#fb4934 fs= build>=3157
//                  ^ fg=#ebdbb2 fs=

class ExtendsTest implements Foo {}
// ^ fg=#fabd2f fs= build>=3127
//    ^ fg=#ebdbb2 fs=
//                ^ fg=#fabd2f fs=
//                           ^ fg=#ebdbb2 fs=
//                               ^^ fg=#83a598 fs=

class Foo<A> extends Bar<? extends A> {}
// ^ fg=#fabd2f fs= build>=3127
//    ^^^ fg=#ebdbb2 fs=
//       ^ fg=#ebdbb2 fs=
//        ^ fg=#ebdbb2 fs= build>=3127
//         ^ fg=#ebdbb2 fs=
//           ^ fg=#fabd2f fs=
//                   ^^^ fg=#ebdbb2 fs=
//                      ^ fg=#ebdbb2 fs= build>=3127
//                       ^ fg=#fb4934 fs= build>=3127
//                         ^^^^^^^ fg=#fabd2f fs= build>=3127
//                                 ^ fg=#ebdbb2 fs= build>=3127
//                                  ^ fg=#ebdbb2 fs=
//                                    ^^ fg=#83a598 fs=

public class FibCalculator extends Fibonacci implements Calculator {
// ^ fg=#fabd2f fs=
//     ^ fg=#fabd2f fs= build>=3127
//           ^ fg=#ebdbb2 fs=
//                         ^ fg=#fabd2f fs=
//                                 ^ fg=#ebdbb2 fs=
//                                           ^ fg=#fabd2f fs=
//                                                      ^ fg=#ebdbb2 fs=

    public static final int A_CONSTANT = 1;
    //                  ^ fg=#fabd2f fs=
    //                      ^ fg=#ebdbb2 fs=

    private static Map<Integer, Integer> memoized = new HashMap<Integer, Integer>();
    // ^ fg=#fabd2f fs=
    //      ^ fg=#fabd2f fs=
    //             ^^^ fg=#ebdbb2 fs=
    //                ^ fg=#ebdbb2 fs= build>=3127
    //                 ^^^^^^^ fg=#ebdbb2 fs=
    //                        ^ fg=#ebdbb2 fs= build>=3127
    //                          ^^^^^^^ fg=#ebdbb2 fs=
    //                                 ^ fg=#ebdbb2 fs= build>=3127
    //                                   ^ fg=#ebdbb2 fs=
    //                                            ^ fg=#fe8019 fs=
    //                                              ^^^ fg=#fb4934 fs=
    //                                                  ^^^^^^^ fg=#ebdbb2 fs=
    //                                                         ^ fg=#ebdbb2 fs= build>=3127
    //                                                          ^^^^^^^ fg=#ebdbb2 fs=
    //                                                                 ^ fg=#ebdbb2 fs= build>=3127
    //                                                                   ^^^^^^^ fg=#ebdbb2 fs=
    //                                                                          ^ fg=#ebdbb2 fs= build>=3127
    //                                                                           ^^ fg=#83a598 fs=

    public static void x(String... args) {}
    // ^ fg=#fabd2f fs=
    //     ^ fg=#fabd2f fs=
    //            ^^^^ fg=#83a598 fs=
    //                 ^ fg=#ebdbb2 fs=
    //                  ^ fg=#83a598 fs=
    //                   ^^^^^^ fg=#ebdbb2 fs=
    //                         ^^^ fg=#fe8019 fs= build>=3127
    //                             ^^^^ fg=#ebdbb2 fs=
    //                                 ^ fg=#83a598 fs=
    //                                   ^^ fg=#83a598 fs=

    public static void main(String[] args) {
    // ^ fg=#fabd2f fs=
    //     ^ fg=#fabd2f fs=
    //            ^^^^ fg=#83a598 fs=
    //                 ^ fg=#ebdbb2 fs=
    //                     ^ fg=#83a598 fs=
    //                      ^ fg=#ebdbb2 fs=
    //                            ^^ fg=#fabd2f fs=
    //                               ^ fg=#ebdbb2 fs=
    //                                   ^ fg=#83a598 fs=
    //                                     ^ fg=#83a598 fs=
        System.out.println("Hello World!");
        // ^^^ fg=#ebdbb2 fs= build>=3150
        //    ^ fg=#ebdbb2 fs= build>=3127
        //     ^^^ fg=#ebdbb2 fs=
        //        ^ fg=#ebdbb2 fs= build>=3127
        //         ^^^^^^^ fg=#ebdbb2 fs= build>=3127
        //                ^ fg=#83a598 fs= build>=3127
        //                 ^^^^^^^^^^^^^^ fg=#b8bb26 fs=
        //                               ^ fg=#83a598 fs=

        memoized.put(1, 1);
        memoized.put(2, 1);
        // ^^^^^ fg=#ebdbb2 fs=
        //      ^ fg=#ebdbb2 fs= build>=3127
        //       ^^^ fg=#ebdbb2 fs= build>=3127
        //          ^ fg=#83a598 fs=
        //           ^ fg=#d3869b fs=
        //            ^ fg=#ebdbb2 fs=
        //              ^ fg=#d3869b fs=
        //               ^ fg=#83a598 fs=
        System.out.println(fibonacci(12)); //Get the 12th Fibonacci number and print to console
        // ^^^ fg=#ebdbb2 fs= build>=3150
        //    ^ fg=#ebdbb2 fs= build>=3127
        //     ^^^ fg=#ebdbb2 fs=
        //        ^ fg=#ebdbb2 fs= build>=3127
        //         ^^^^^^^ fg=#ebdbb2 fs= build>=3127
        //                ^ fg=#83a598 fs=
        //                 ^^^^^^^^^ fg=#ebdbb2 fs= build>=3127
        //                          ^ fg=#83a598 fs=
        //                           ^^ fg=#d3869b fs=
        //                             ^^ fg=#83a598 fs=
    }
//  ^ fg=#83a598 fs=

    public static int fibonacci(int fibIndex) {
    //            ^^^ fg=#fabd2f fs=
    //                ^ fg=#ebdbb2 fs=
    //                          ^^^ fg=#fabd2f fs=
    //                              ^ fg=#ebdbb2 fs=
        if (memoized.containsKey(fibIndex)) {
    //  ^ fg=#fb4934 fs=
            return memoized.get(fibIndex);
            // ^ fg=#fb4934 fs=
        } else {
        // ^ fg=#fb4934 fs=
            int answer = fibonacci(fibIndex - 1) + fibonacci(fibIndex - 2);
        //  ^^^ fg=#fabd2f fs=
            //         ^ fg=#fe8019 fs=
            //                              ^ fg=#fe8019 fs=
            //                                   ^ fg=#fe8019 fs=
            //                                                        ^ fg=#fe8019 fs=
            memoized.put(fibIndex, answer);
            // ^^^^^ fg=#ebdbb2 fs=
            //      ^ fg=#ebdbb2 fs= build>=3127
            //       ^^^ fg=#ebdbb2 fs= build>=3127
            //          ^ fg=#83a598 fs=
            //           ^ fg=#ebdbb2 fs=
            //           ^ fg=#ebdbb2 fs=
            //                      ^ fg=#ebdbb2 fs=
            //                           ^ fg=#83a598 fs=

            return answer;
            // ^ fg=#fb4934 fs=
            //     ^^^^^^^ fg=#ebdbb2 fs=
        }
    //  ^ fg=#83a598 fs=
    }
//  ^ fg=#83a598 fs=
}

public class Hello extends JFrame {
    public Hello() {
        super.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        // ^ fg=#fabd2f fs=
        //   ^ fg=#ebdbb2 fs= build>=3127
        //    ^ fg=#ebdbb2 fs= build>=3127
        //                            ^ fg=#83a598 fs=
        //                             ^ fg=#ebdbb2 fs= build>=3150
        //                                            ^ fg=#ebdbb2 fs= build>=3127
        //                                             ^ fg=#ebdbb2 fs=
        //                                                          ^ fg=#83a598 fs=
        super.add(new JLabel("Hello, world!"));
        //            ^ fg=#ebdbb2 fs=
        super.setVisible(true);
        //               ^^^^ fg=#d3869b fs=
    }
}
