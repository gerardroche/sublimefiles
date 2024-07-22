# COLOR SCHEME TEST "GruvboxDark.sublime-color-scheme" "Ruby"

    #     whitespace
# ^ fg=#ebdbb2 bg=#282828 fs=

x = nil
#   ^ fg=#fabd2f fs=

x = false
#   ^ fg=#d3869b fs=

x = __dir__
#   ^ fg=#fe8019 fs=

x = __FILE__
#   ^ fg=#fabd2f fs=

abc.to_s
# ^ fg=#ebdbb2 fs=
#  ^ fg=#ebdbb2 fs=
#   ^ fg=#fe8019 fs=

x = String.new("x")
#   ^ fg=#fe8019 fs=
#         ^ fg=#ebdbb2 fs=
#          ^ fg=#fb4934 fs=
#             ^ fg=#ebdbb2 fs=
#              ^^^ fg=#b8bb26 fs=
#                 ^ fg=#ebdbb2 fs=

x = "x%dy\nz"
#   ^^ fg=#b8bb26 fs=
#     ^^ fg=#d3869b fs=
#       ^ fg=#b8bb26 fs=
#        ^^ fg=#fe8019 fs=
#          ^^ fg=#b8bb26 fs=

puts "x"
# ^ fg=#fe8019 fs=
#    ^^^ fg=#b8bb26 fs=

x = %(x)
#   ^^^^ fg=#b8bb26 fs=

x = %[x]
#   ^^^^ fg=#b8bb26 fs=

x = %{x}
#   ^^^^ fg=#b8bb26 fs=

x = "a#{x}b"
#   ^^ fg=#b8bb26 fs=
#     ^^ fg=#83a598 fs= build>=3177
#       ^ fg=#ebdbb2 fs= build>=3177
#        ^ fg=#83a598 fs= build>=3177
#         ^^ fg=#b8bb26 fs=

x = "a#{x.y}b"
#   ^^ fg=#b8bb26 fs=
#     ^^ fg=#83a598 fs= build>=3177
#       ^^^ fg=#ebdbb2 fs= build>=3177
#          ^ fg=#83a598 fs= build>=3177
#           ^^ fg=#b8bb26 fs=

x = "a#{X.inspect}b"
#   ^^ fg=#b8bb26 fs=
#     ^^ fg=#83a598 fs= build>=3177
#       ^ fg=#d3869b fs= build>=4118
#        ^ fg=#ebdbb2 fs= build>=3177
#         ^ fg=#fe8019 fs=
#                ^ fg=#83a598 fs= build>=3177
#                 ^^ fg=#b8bb26 fs=

x = "a#{X.y}b"
#   ^^ fg=#b8bb26 fs=
#     ^^ fg=#83a598 fs= build>=3177
#       ^ fg=#d3869b fs= build>=4118
#        ^^ fg=#ebdbb2 fs= build>=3177
#          ^ fg=#83a598 fs=
#           ^^ fg=#b8bb26 fs=

x = "y".freeze
#   ^^^ fg=#b8bb26 fs=
#      ^ fg=#ebdbb2 fs=
#       ^ fg=#fe8019 fs=

x = /^\/?(a|b|c|\(\w*\))/
#   ^^ fg=#b8bb26 fs=
#     ^^ fg=#fe8019 fs=
#       ^^^^^^^^ fg=#b8bb26 fs=
#               ^^^^ fg=#fe8019 fs=
#                   ^ fg=#b8bb26 fs=
#                    ^^ fg=#fe8019 fs=
#                      ^^ fg=#b8bb26 fs=

x = []
#   ^^ fg=#83a598 fs=

x = ["a", "b"]
#   ^ fg=#83a598 fs=
#    ^^^ fg=#b8bb26 fs=
#       ^ fg=#ebdbb2 fs=
#         ^^^ fg=#b8bb26 fs=
#            ^ fg=#83a598 fs=

x = [:a, :b]
#   ^ fg=#83a598 fs=
#    ^^ fg=#d3869b fs=
#      ^ fg=#ebdbb2 fs=
#        ^^ fg=#d3869b fs=
#          ^ fg=#83a598 fs=

x = [a, b, c].x.join(".")
#   ^ fg=#83a598 fs=
#    ^^ fg=#ebdbb2 fs=
#       ^^ fg=#ebdbb2 fs=
#          ^ fg=#ebdbb2 fs=
#           ^ fg=#83a598 fs=
#            ^^^^^^^^ fg=#ebdbb2 fs=
#                    ^^^ fg=#b8bb26 fs=
#                       ^ fg=#ebdbb2 fs=

x = [A, B, C].x.join(".")
#   ^ fg=#83a598 fs=
#    ^ fg=#d3869b fs=
#     ^ fg=#ebdbb2 fs=
#       ^ fg=#d3869b fs=
#        ^ fg=#ebdbb2 fs=
#          ^ fg=#d3869b fs=
#           ^ fg=#83a598 fs=
#            ^^^^^^^^ fg=#ebdbb2 fs=
#                    ^^^ fg=#b8bb26 fs=
#                       ^ fg=#ebdbb2 fs=

x = {}
#   ^^ fg=#83a598 fs=

x = { a: "b", c: "d" }
#   ^ fg=#83a598 fs=
#     ^^ fg=#d3869b fs=
#        ^^^ fg=#b8bb26 fs=
#           ^ fg=#ebdbb2 fs=
#             ^^ fg=#d3869b fs=
#                ^^^ fg=#b8bb26 fs=
#                    ^ fg=#83a598 fs=

x = Class.new(X::Abc)
#   ^ fg=#fabd2f fs=
#        ^ fg=#ebdbb2 fs=
#         ^ fg=#fb4934 fs=
#            ^ fg=#ebdbb2 fs=
#             ^ fg=#d3869b fs= build>=4118
#              ^^ fg=#fe8019 fs=
#                ^^^ fg=#fabd2f fs= build>=4118
#                   ^ fg=#ebdbb2 fs=

x = merge("a" => x.y, "b" => X.y)
#   ^^^^^^ fg=#ebdbb2 fs=
#         ^^^ fg=#b8bb26 fs=
#             ^^ fg=#fabd2f fs=
#                ^^^^ fg=#ebdbb2 fs=
#                     ^^^ fg=#b8bb26 fs=
#                         ^^ fg=#fabd2f fs=
#                            ^ fg=#d3869b fs= build>=4125
#                             ^^^ fg=#ebdbb2 fs= build>=4118

x = merge(
  "a" => x.y,
#     ^^ fg=#fabd2f fs=
#        ^^^^ fg=#ebdbb2 fs=
  "b" => X.y
#     ^^ fg=#fabd2f fs=
#        ^ fg=#d3869b fs= build>=4118
#         ^^ fg=#ebdbb2 fs=
)

call(/regex/, "x")
# ^^^ fg=#ebdbb2 fs=
#    ^^^^^^^ fg=#b8bb26 fs=
#           ^ fg=#ebdbb2 fs=
#             ^^^ fg=#b8bb26 fs=
#                ^ fg=#ebdbb2 fs=

abc = X.new("y")
# ^ fg=#ebdbb2 fs=
#   ^ fg=#fe8019 fs=
#     ^ fg=#d3869b fs= build>=4118
#      ^ fg=#ebdbb2 fs=
#       ^^^ fg=#fb4934 fs=
#          ^ fg=#ebdbb2 fs=
#           ^^^ fg=#b8bb26 fs=
#              ^ fg=#ebdbb2 fs=

abc.x
# ^^^ fg=#ebdbb2 fs=

ABC::X
# ^ fg=#d3869b fs= build>=4118
#  ^^ fg=#fe8019 fs=
#    ^ fg=#d3869b fs= build>=4118

ABC::X.Y
# ^ fg=#d3869b fs= build>=4118
#  ^^ fg=#fe8019 fs=
#    ^ fg=#d3869b fs= build>=4118
#     ^^ fg=#ebdbb2 fs=

ABC::X.y
# ^ fg=#d3869b fs= build>=4118
#  ^^ fg=#fe8019 fs=
#    ^ fg=#d3869b fs= build>=4118
#     ^^ fg=#ebdbb2 fs=

if name.is_a?(Pathname)

x = <<END
# ^ fg=#fe8019 fs=
#   ^^ fg=#fb4934 fs=
#     ^^^ fg=#8ec07c fs=
  string
#   ^ fg=#b8bb26 fs=
END
# ^ fg=#8ec07c fs=

x = <<-END
#   ^^^ fg=#fb4934 fs=
#      ^^^ fg=#8ec07c fs=
  string
#   ^ fg=#b8bb26 fs=
END
# ^ fg=#8ec07c fs=

x = <<~EOF
#   ^^^ fg=#fb4934 fs=
#      ^^^ fg=#8ec07c fs=
  string
#   ^ fg=#b8bb26 fs=
EOF
# ^ fg=#8ec07c fs=

abc.each do |x|
# ^^^^^^ fg=#ebdbb2 fs=
#        ^^ fg=#fb4934 fs=
#           ^ fg=#fb4934 fs=
#            ^ fg=#ebdbb2 fs=
#             ^ fg=#fb4934 fs=
end
# ^ fg=#fb4934 fs=

module X
# ^ fg=#fabd2f fs= build>=4092
end
# ^ fg=#fb4934 fs=

class X
# ^ fg=#fabd2f fs= build>=4081
#     ^ fg=#ebdbb2 fs=
end
# ^ fg=#fb4934 fs=

class X::Y
#     ^ fg=#ebdbb2 fs=
#      ^^ fg=#fe8019 fs=
#        ^ fg=#ebdbb2 fs=
end

class X < Y
#     ^ fg=#ebdbb2 fs=
#       ^ fg=#fe8019 fs=
#         ^ fg=#ebdbb2 fs=
end

class A::B < C::D
#     ^ fg=#ebdbb2 fs=
#      ^^ fg=#fe8019 fs=
#        ^ fg=#ebdbb2 fs=
#          ^ fg=#fe8019 fs=
#            ^ fg=#ebdbb2 fs=
#             ^^ fg=#fe8019 fs=
#               ^ fg=#ebdbb2 fs=
end

class X # :nodoc
#       ^^^^^^^^ fg=#928374 fs=italic
end

class X
  x "y"
# ^ fg=#ebdbb2 fs=
#   ^^^ fg=#b8bb26 fs=

  X = "y"
# ^ fg=#ebdbb2 fs=
#   ^ fg=#fe8019 fs=
#     ^^^ fg=#b8bb26 fs=

  def self.v
# ^ fg=#8ec07c fs= build>=4081
#     ^^^^ fg=#fabd2f fs=
#         ^ fg=#ebdbb2 fs=
#          ^ fg=#ebdbb2 fs=
    A::B.new C::D
#   ^ fg=#d3869b fs= build>=4118
#    ^^ fg=#fe8019 fs=
#      ^ fg=#d3869b fs= build>=4118
#       ^ fg=#ebdbb2 fs=
#        ^^^ fg=#fb4934 fs=
#            ^ fg=#d3869b fs= build>=4118
#             ^^ fg=#fe8019 fs=
#               ^ fg=#d3869b fs= build>=4118
  end
# ^ fg=#fb4934 fs=

  module C
# ^ fg=#fabd2f fs= build>=4092
#        ^ fg=#ebdbb2 fs=
    A = 5
#   ^ fg=#ebdbb2 fs=
#     ^ fg=#fe8019 fs=
#       ^ fg=#d3869b fs=
    B = 2
    C = 0
    D = [a, b, c].compact.join(".")
#       ^ fg=#83a598 fs=
#        ^^^^^^^ fg=#ebdbb2 fs=
#               ^ fg=#83a598 fs=
#                ^^^^^^^^^^^^^^ fg=#ebdbb2 fs=
#                              ^^^ fg=#b8bb26 fs=
#                                 ^ fg=#ebdbb2 fs=
    E = [A, B, C].compact.join(".")
#       ^ fg=#83a598 fs=
#        ^ fg=#d3869b fs=
#         ^ fg=#ebdbb2 fs=
#           ^ fg=#d3869b fs=
#            ^ fg=#ebdbb2 fs=
#              ^ fg=#d3869b fs=
#               ^ fg=#83a598 fs=
#                ^^^^^^^^^^^^^^ fg=#ebdbb2 fs=
#                              ^^^ fg=#b8bb26 fs=
#                                 ^ fg=#ebdbb2 fs=
  end
# ^ fg=#fb4934 fs=


  private
# ^ fg=#fb4934 fs=

    def x
#   ^ fg=#8ec07c fs= build>=4081
#       ^ fg=#ebdbb2 fs=
    end
#   ^ fg=#fb4934 fs=
end
# ^ fg=#fb4934 fs=

class X

  include X::Y::Z
#   ^ fg=#fb4934 fs=
#         ^ fg=#d3869b fs= build>=4118
#          ^^ fg=#fe8019 fs=
#            ^ fg=#d3869b fs= build>=4118
#             ^^ fg=#fe8019 fs=
#               ^ fg=#d3869b fs= build>=4118

  autoload :X, "y"
#   ^ fg=#fe8019 fs=
#          ^^ fg=#d3869b fs=
#            ^ fg=#ebdbb2 fs=
#              ^^^ fg=#b8bb26 fs=

  def x
#   ^ fg=#8ec07c fs= build>=4081
#     ^ fg=#ebdbb2 fs=

    puts "Hi #{@name}!"
#     ^ fg=#fe8019 fs=
#        ^^^ fg=#b8bb26 fs=
#            ^^ fg=#83a598 fs= build>=3177
#              ^ fg=#fe8019 fs= build>=3177
#               ^^^^ fg=#ebdbb2 fs= build>=3177
#                   ^ fg=#83a598 fs= build>=3177
#                    ^^ fg=#b8bb26 fs=

    abc = @y
#     ^ fg=#ebdbb2 fs=
#       ^ fg=#fe8019 fs=
#         ^ fg=#fe8019 fs=
#          ^ fg=#ebdbb2 fs=

    ABC.y = z
#     ^ fg=#d3869b fs= build>=4118
#      ^^ fg=#ebdbb2 fs=
#         ^ fg=#fe8019 fs=
#           ^ fg=#ebdbb2 fs=

    ABC.y(:z, x)
#     ^ fg=#d3869b fs= build>=4118
#      ^^^ fg=#ebdbb2 fs=
#         ^^ fg=#d3869b fs=
#            ^^^ fg=#ebdbb2 fs=

    abc "y", z, Dir.pwd
#     ^ fg=#ebdbb2 fs=
#       ^^^ fg=#b8bb26 fs=
#          ^ fg=#ebdbb2 fs=
#            ^^ fg=#ebdbb2 fs=
#               ^^^ fg=#fabd2f fs=
#                  ^^^^ fg=#ebdbb2 fs=

    @x = false
#   ^ fg=#fe8019 fs=
#    ^ fg=#ebdbb2 fs=
#      ^ fg=#fe8019 fs=
#        ^ fg=#d3869b fs=

    @x = Class.new(X::Abc)
#   ^ fg=#fe8019 fs=
#    ^ fg=#ebdbb2 fs=
#      ^ fg=#fe8019 fs=
#        ^ fg=#fabd2f fs=
#             ^ fg=#ebdbb2 fs=
#              ^^^ fg=#fb4934 fs=
#                 ^ fg=#ebdbb2 fs=
#                  ^ fg=#d3869b fs= build>=4118
#                   ^^ fg=#fe8019 fs=
#                     ^ fg=#fabd2f fs= build>=4118
    @x = @y
#   ^ fg=#fe8019 fs=
#    ^ fg=#ebdbb2 fs=
#      ^ fg=#fe8019 fs=
#        ^ fg=#fe8019 fs=
#         ^ fg=#ebdbb2 fs=

    x = "a#{@x['y']}b"
#       ^^ fg=#b8bb26 fs=
#         ^^ fg=#83a598 fs= build>=3177
#           ^ fg=#fe8019 fs= build>=3177
#            ^ fg=#ebdbb2 fs= build>=3177
#             ^ fg=#83a598 fs=
#              ^^^ fg=#b8bb26 fs=
#                 ^ fg=#83a598 fs=
#                  ^ fg=#83a598 fs= build>=3177
#                   ^^ fg=#b8bb26 fs=

    super.merge(
#     ^ fg=#fe8019 fs= build>=4081
#        ^^^^^^^ fg=#ebdbb2 fs=
      "a" => x.y,
#     ^^^ fg=#b8bb26 fs=
#         ^^ fg=#fabd2f fs=
#            ^^^^ fg=#ebdbb2 fs=
      "b" => X.y
#     ^^^ fg=#b8bb26 fs=
#         ^^ fg=#fabd2f fs=
#            ^ fg=#d3869b fs= build>=4118
#             ^^ fg=#ebdbb2 fs=
    )
#   ^ fg=#ebdbb2 fs=
  end

  class << self
#       ^^ fg=#fe8019 fs=
#          ^^^^ fg=#fabd2f fs=
    def x(y)
#       ^ fg=#ebdbb2 fs=
#        ^ fg=#ebdbb2 fs=
#         ^ fg=#ebdbb2 fs=
#          ^ fg=#ebdbb2 fs=
      super
#       ^ fg=#fe8019 fs= build>=4081
    end

    def x
      super.x!
#       ^^^ fg=#fe8019 fs= build>=4081
#          ^^^ fg=#ebdbb2 fs=
    end

    def x(x = {}, &block)
#       ^ fg=#ebdbb2 fs=
#        ^ fg=#ebdbb2 fs=
#         ^ fg=#ebdbb2 fs=
#           ^ fg=#fe8019 fs=
#             ^^ fg=#83a598 fs=
#               ^ fg=#ebdbb2 fs=
#                 ^ fg=#fb4934 fs=
#                  ^^^^^ fg=#ebdbb2 fs=
#                       ^ fg=#ebdbb2 fs=
      new(x, &block).x!
#       ^ fg=#fb4934 fs=
#        ^^^ fg=#ebdbb2 fs=
#            ^ fg=#fe8019 fs=
#             ^^^^^^^^^ fg=#ebdbb2 fs=
    end

    attr_accessor :x, :y
#     ^ fg=#fb4934 fs=
    alias_method :x?, :y
#     ^ fg=#fabd2f fs=
    attr_reader :x, :y, :z
#     ^ fg=#fb4934 fs=

    delegate :a, :b=, c: :d
#     ^ fg=#ebdbb2 fs=

    def x?
#       ^^ fg=#ebdbb2 fs=
    end

    def x(name)
#         ^^^^ fg=#ebdbb2 fs=
      if name.is_a?(Pathname)
        y = name
      else
        y = Pathname.new("#{p["c"].e.f}/#{name}.yml")
      end
    rescue X::SyntaxError => e
#     ^ fg=#fb4934 fs=
#          ^ fg=#d3869b fs= build>=4118
#           ^^ fg=#fe8019 fs=
#             ^ fg=#fabd2f fs= build>=4118
#                         ^^ fg=#fabd2f fs=
#                            ^ fg=#ebdbb2 fs=
      raise "A #{x}" \
#       ^ fg=#fb4934 fs=
#           ^^ fg=#b8bb26 fs=
#              ^^ fg=#83a598 fs= build>=3177
#                ^ fg=#ebdbb2 fs= build>=3177
#                 ^ fg=#83a598 fs= build>=3177
#                  ^ fg=#b8bb26 fs=
#                    ^ fg=#ebdbb2 fs=
        "B" \
#       ^^^ fg=#b8bb26 fs=
#           ^ fg=#ebdbb2 fs=
        "C: #{e.message}"
#       ^^^ fg=#b8bb26 fs=
#           ^^ fg=#83a598 fs= build>=3177
#             ^^^ fg=#ebdbb2 fs= build>=3177
#                      ^ fg=#83a598 fs= build>=3177
#                       ^ fg=#b8bb26 fs=
    end
  end
