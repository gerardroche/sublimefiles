<!-- COLOR SCHEME TEST "GruvboxDarkVim.sublime-color-scheme" SKIP IF NOT "Vue Syntax Highlight/Vue Component"

Vue Syntax Highlight
========================
https://packagecontrol.io/packages/Vue%20Syntax%20Highlight
-->
<script setup>
// ^ fg=#fe8019 fs= build>=4148
//      ^ fg=#8ec07c fs= build>=4148
//
import { ref } from 'vue'
// ^ fg=#fb4934 fs= build>=4168
//     ^ fg=#83a598 fs= build>=4168
//       ^^^ fg=#ebdbb2 fs= build>=4168
//           ^ fg=#83a598 fs= build>=4168
//             ^ fg=#fb4934 fs= build>=4168
//                  ^^^^ fg=#b8bb26 fs= build>=4168

defineProps({
// ^ fg=#ebdbb2 fs= build>=4148
  on: Boolean,
// ^^ fg=#ebdbb2 fs= build>=4148
//    ^ fg=#d3869b fs= build>=4148
})

const props = defineProps(['title'])
// ^ fg=#fabd2f fs= build>=4168
//    ^ fg=#ebdbb2 fs= build>=4168
//            ^ fg=#ebdbb2 fs= build>=4168

const count = ref(0)
// ^ fg=#fabd2f fs= build>=4168
//    ^ fg=#ebdbb2 fs= build>=4168
//            ^ fg=#ebdbb2 fs= build>=4168
//                ^ fg=#d3869b fs= build>=4168

const publishedBooksMessage = computed(() => {
// ^ fg=#fabd2f fs= build>=4168
//                            ^ fg=#ebdbb2 fs= build>=4168
//                                        ^^ fg=#8ec07c fs= build>=4168
  return author.books.length > 0 ? 'Yes' : 'No'
})

function increment() {
// ^ fg=#b8bb26 fs=bold build>=4168
//       ^ fg=#ebdbb2 fs= build>=4168
  count.value++
//    ^ fg=#ebdbb2 fs= build>=4168
//     ^ fg=#ebdbb2 fs= build>=4168
//      ^ fg=#ebdbb2 fs= build>=4168
}

const open = () => {
//    ^ fg=#ebdbb2 fs= build>=4168
//           ^^ fg=#83a598 fs= build>=4168
//              ^^ fg=#8ec07c fs= build>=4168
}

</script>

<template #title>
<!--  ^ fg=#b8bb26 fs= build>=4168 -->
    <!--  ^^^^^^ fg=#83a598 fs= build>=4168 -->
<!--            ^ fg=#83a598 fs= build>=4168 -->
    <slot name="title" />
    <!--  ^ fg=#8ec07c fs= build>=4148 -->

    <div v-if="x" :href="x" :fizz="x">
    <!-- ^^^^ fg=#83a598 fs= build>=4168 -->
    <!--          ^^^^^ fg=#83a598 fs= build>=4168 -->
    <!--                    ^^^^^ fg=#83a598 fs= build>=4168 -->
        fizz</div>
    <div v-else :class="x">
    <!-- ^^^^^^ fg=#83a598 fs= build>=4168 -->
    <!--        ^^^^^^ fg=#83a598 fs= build>=4168 -->
        buzz</div>

        <template>
<!--    ^ fg=#83a598 fs= build>=4168 -->
<!--     ^ fg=#b8bb26 fs= build>=4168 -->
<!--             ^ fg=#83a598 fs= build>=4168 -->
          <button @click="increment">
          <!-- ^ fg=#b8bb26 fs= build>=4168 -->
          <!--    ^^ fg=#83a598 fs= build>=4168 -->
          <!--          ^ fg=#fe8019 fs= build>=4168 -->
          <!--           ^ fg=#b8bb26 fs= build>=4168 -->
          <!--            ^ fg=#b8bb26 fs= build>=4168 -->
          <!--                     ^ fg=#b8bb26 fs= build>=4168 -->
            {{ count }}
<!--        ^^ fg=#83a598 fs= build>=4168 -->
<!--           ^ fg=#ebdbb2 fs= build>=4168 -->
<!--                 ^^ fg=#83a598 fs= build>=4168 -->
          </button>
<!--      ^^ fg=#83a598 fs= build>=4168 -->
<!--        ^ fg=#b8bb26 fs= build>=4168 -->
<!--              ^ fg=#83a598 fs= build>=4168 -->
          <span :key="text">{{ text }}</span>
<!--      ^ fg=#83a598 fs= build>=4168 -->
<!--       ^ fg=#b8bb26 fs= build>=4168 -->
<!--                       ^ fg=#83a598 fs= build>=4168 -->
<!--                        ^^ fg=#83a598 fs= build>=4168 -->
<!--                                ^^ fg=#83a598 fs= build>=4168 -->
<!--                                  ^^ fg=#83a598 fs= build>=4168 -->
          <button class="btn" v-bind="$attrs">click me</button>
          <!--    ^ fg=#b8bb26 fs= build>=4168 -->
          <!--         ^ fg=#fe8019 fs= build>=4168 -->
          <!--          ^^^^^ fg=#b8bb26 fs= build>=4168 -->
          <!--                        ^ fg=#fe8019 fs= build>=4168 -->
          <!--                         ^ fg=#ebdbb2 fs= build>=4168 -->
          <p :class="$attrs.class">Hi!</p>
          <!--       ^ fg=#fe8019 fs= build>=4168 -->
          <!--        ^ fg=#ebdbb2 fs= build>=4168 -->
          <!--             ^ fg=#ebdbb2 fs= build>=4168 -->
          <!--              ^ fg=#ebdbb2 fs= build>=4168 -->
          <p :class="$page.post.id">Hi!</p>
          <!--       ^ fg=#fe8019 fs= build>=4168 -->
          <!--        ^ fg=#ebdbb2 fs= build>=4168 -->
          <!--            ^ fg=#ebdbb2 fs= build>=4168 -->
          <!--             ^ fg=#ebdbb2 fs= build>=4168 -->
          <!--                 ^ fg=#ebdbb2 fs= build>=4168 -->
          <!--                  ^ fg=#ebdbb2 fs= build>=4168 -->
          <img v-if="$page.x">
          <!--       ^ fg=#fe8019 fs= build>=4168 -->
          <!--        ^ fg=#ebdbb2 fs= build>=4168 -->
          <!--            ^ fg=#ebdbb2 fs= build>=4168 -->
          <!--             ^ fg=#ebdbb2 fs= build>=4168 -->
          <span>{{ $page.props.x.y }}</span>
          <!--  ^^ fg=#83a598 fs= build>=4168 -->
          <!--     ^ fg=#fe8019 fs= build>=4168 -->
          <!--      ^ fg=#ebdbb2 fs= build>=4168 -->
          <!--          ^ fg=#ebdbb2 fs= build>=4168 -->
          <!--           ^ fg=#ebdbb2 fs= build>=4168 -->
          <!--                     ^^ fg=#83a598 fs= build>=4168 -->
        </template>
<!--    ^^ fg=#83a598 fs= build>=4168 -->
<!--      ^^^^^^^^  fg=#b8bb26 fs= build>=4168 -->
<!--              ^ fg=#83a598 fs= build>=4168 -->

</template>
<!-- ^^^^^  fg=#b8bb26 fs= build>=4168 -->
<!--      ^ fg=#83a598 fs= build>=4168 -->
