// COLOR SCHEME TEST "GruvboxDark.sublime-color-scheme" "Rust"

#[derive(Debug)]
pub enum State {
//^ fg=#fabd2f fs=
//  ^ fg=#fabd2f fs= build>=4174
//       ^ fg=#ebdbb2 fs=
//             ^ fg=#83a598 fs=
    Start,
    // ^ fg=#83a598 fs= build>=4134
    //   ^ fg=#ebdbb2 fs=
    Transient,
    Closed,
}

impl From<&'a str> for State {
// ^ fg=#fabd2f fs= build>=4174
//            ^ fg=#83a598 fs=
//               ^ fg=#ebdbb2 fs=
//                 ^ fg=#fb4934 fs=
//                     ^ fg=#ebdbb2 fs=
//                           ^ fg=#83a598 fs=
    fn from(s: &'a str) -> Self {
//  ^ fg=#8ec07c fs=
//     ^ fg=#ebdbb2 fs=
//         ^ fg=#83a598 fs=
//          ^ fg=#ebdbb2 fs=
//           ^ fg=#ebdbb2 fs=
//                 ^ fg=#83a598 fs=
//                    ^ fg=#83a598 fs=
//                      ^^ fg=#ebdbb2 fs=
//                         ^ fg=#83a598 fs=
//                              ^ fg=#83a598 fs=
        match s {
//      ^ fg=#fb4934 fs=
//            ^ fg=#ebdbb2 fs=
//              ^ fg=#83a598 fs=
            "start" => State::Start,
            // ^ fg=#b8bb26 fs=
            //    ^ fg=#b8bb26 fs=
            //      ^^ fg=#fb4934 fs=
            //              ^^ fg=#ebdbb2 fs=
            "closed" => State::Closed,
            //       ^^ fg=#fb4934 fs=
            //               ^^ fg=#ebdbb2 fs=
            _ => unreachable!(),
        }
    }
}

