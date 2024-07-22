-- COLOR SCHEME TEST "GruvboxDark.sublime-color-scheme" "SQL"

SELECT * FROM x;
-- ^ fg=#fb4934 fs=
--     ^ fg=#fb4934 fs= build>=4107
--       ^^^^ fg=#fb4934 fs=
--            ^^ fg=#ebdbb2 fs=



SELECT 'x''y';
-- ^ fg=#fb4934 fs=
--     ^^ fg=#b8bb26 fs=
--       ^^ fg=#fe8019 fs=
--         ^^ fg=#b8bb26 fs=
--           ^ fg=#ebdbb2 fs=

SELECT "x""y" FROM z;
-- ^ fg=#fb4934 fs=
--     ^^ fg=#b8bb26 fs=
--       ^^ fg=#fe8019 fs=
--         ^^ fg=#b8bb26 fs=
--            ^^^^ fg=#fb4934 fs=
--                 ^^ fg=#ebdbb2 fs=

SELECT VERSION(), CURRENT_DATE;
-- ^ fg=#fb4934 fs=
--     ^^^^^^^ fg=#ebdbb2 fs=
--            ^^ fg=#83a598 fs=
--              ^ fg=#ebdbb2 fs=
--                ^^^^^^^^^^^^ fg=#b8bb26 fs=bold
--                            ^ fg=#ebdbb2 fs=

SELECT SIN(PI() / 4), (4 + 1) * 5;
-- ^ fg=#fb4934 fs=
--     ^^^^^^ fg=#ebdbb2 fs=
--           ^^ fg=#83a598 fs=
--              ^ fg=#fe8019 fs=
--                ^ fg=#d3869b fs=
--                 ^^ fg=#ebdbb2 fs=
--                    ^ fg=#ebdbb2 fs=
--                     ^ fg=#d3869b fs=
--                       ^ fg=#fe8019 fs=
--                         ^ fg=#d3869b fs=
--                          ^ fg=#ebdbb2 fs=
--                            ^ fg=#fb4934 fs= build>=4107
--                              ^ fg=#d3869b fs=
--                               ^ fg=#ebdbb2 fs=

SELECT * FROM a WHERE b = 'c' AND d < 30;
-- ^^^ fg=#fb4934 fs=
--     ^ fg=#fb4934 fs= build>=4107
--       ^^^^ fg=#fb4934 fs=
--            ^ fg=#ebdbb2 fs=
--              ^^^^^ fg=#fb4934 fs=
--                    ^ fg=#ebdbb2 fs=
--                      ^ fg=#fb4934 fs=
--                        ^^^ fg=#b8bb26 fs=
--                            ^^^ fg=#fe8019 fs=
--                                ^ fg=#ebdbb2 fs=
--                                  ^ fg=#fb4934 fs=
--                                    ^^ fg=#d3869b fs=
--                                      ^ fg=#ebdbb2 fs=

/*!40101 SET character_set_client = utf8 */;
-- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ fg=#928374 fs=italic
--                                         ^ fg=#ebdbb2 fs=

CREATE TABLE `x` (
-- ^ fg=#fb4934 fs=
--     ^ fg=#fb4934 fs=
--           ^ fg=#ebdbb2 fs=
--            ^ fg=#ebdbb2 fs=
--             ^ fg=#ebdbb2 fs=
--               ^ fg=#ebdbb2 fs=
  `a` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
-- ^^ fg=#b8bb26 fs=
--    ^^^^^^ fg=#83a598 fs=
--          ^ fg=#ebdbb2 fs=
--           ^^ fg=#d3869b fs=
--              ^^^^^^^^^ fg=#ebdbb2 fs=
--                        ^^^ fg=#fe8019 fs=
--                            ^^^^ fg=#fabd2f fs= build>=4061
--                                 ^^^^^^^^^^^^^^^ fg=#ebdbb2 fs=
  `b` int(10) unsigned NOT NULL,
--    ^^^ fg=#83a598 fs=
--       ^ fg=#ebdbb2 fs=
--        ^^ fg=#d3869b fs=
  PRIMARY KEY (`x`),
-- ^ fg=#fabd2f fs=
--            ^ fg=#ebdbb2 fs=
--             ^^^ fg=#b8bb26 fs=
--                ^^ fg=#ebdbb2 fs=
  KEY `x` (`y`)
-- ^ fg=#fabd2f fs= build>=4090
--    ^^^ fg=#b8bb26 fs=
--        ^ fg=#ebdbb2 fs=
--         ^^^ fg=#b8bb26 fs=
--            ^ fg=#ebdbb2 fs=
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
-- ^^^^^ fg=#ebdbb2 fs=
--      ^ fg=#fb4934 fs=
--       ^^^^^^ fg=#ebdbb2 fs=
--              ^^^^^^^ fg=#fabd2f fs=
--                      ^^^^^^^ fg=#ebdbb2 fs=
--                             ^ fg=#fb4934 fs=
--                              ^^^^^^^^^^^^ fg=#ebdbb2 fs=
--                                          ^ fg=#fb4934 fs=
--                                           ^^^^^^^^^^^^^^^^ fg=#ebdbb2 fs=

INSERT INTO `x` (`a`, `b`) VALUES ('c', 'd');
-- ^ fg=#fb4934 fs=
--          ^^^ fg=#b8bb26 fs=
--              ^ fg=#ebdbb2 fs=
--               ^^^ fg=#b8bb26 fs=
--                  ^ fg=#ebdbb2 fs=
--                    ^^^ fg=#b8bb26 fs=
--                        ^ fg=#ebdbb2 fs=
--                         ^ fg=#fb4934 fs=
--                                ^ fg=#ebdbb2 fs=
--                                 ^^^ fg=#b8bb26 fs=
--                                    ^ fg=#ebdbb2 fs=
--                                      ^^^ fg=#b8bb26 fs=
--                                         ^^ fg=#ebdbb2 fs=
