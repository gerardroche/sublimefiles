def dump_view(view):
    print('>>> DEBUG {} [id={}, file={}'
          '\n   buffer_id={}, is_valid={}, is_primary={}, name={}, is_loading={}'
          '\n   is_dirty={}, is_read_only={}, is_scratch={}, encoding={}'
          '\n   line_endings={}, is_in_edit={}, change_count={}'
          '\n   line_height={}, em_width={}, is_popup_visible={}'
          '\n   overwrite_status={}, is_auto_complete_visible={}'']'
          .format(
              str(view),
              str(view.id()), str(view.file_name()),
              str(view.buffer_id()), str(view.is_valid()), str(view.is_primary()),
              str(view.name()), str(view.is_loading()), str(view.is_dirty()),
              str(view.is_read_only()), str(view.is_scratch()), str(view.encoding()),
              str(view.line_endings()), str(view.is_in_edit()), str(view.change_count()),
              str(view.line_height()), str(view.em_width()), str(view.is_popup_visible()),
              str(view.overwrite_status()), str(view.is_auto_complete_visible())))

    print('  size = {}'.format(view.size()))
    print('  has non empty selection? {}'.format(view.has_non_empty_selection_region()))
    print('  sel={}, {}'.format(list(view.sel()), type(view.sel())))

    for i, sel in enumerate(view.sel()):
        print('    sel[{}] = {}, a = {}, b = {}'.format(i, sel, sel.a, sel.b))
        print('    sel[{}] begin = {}, end = {}, begin substr = "{}", end substr = "{}"'.format(
            i, sel.begin(), sel.end(),
            view.substr(sel.begin()).replace('\n', '\\n'),
            view.substr(sel.end()).replace('\n', '\\n')
        ))
        print('    sel[{}] empty? {}'.format(i, sel.empty()))
        print('    sel[{}] word = {}, substr = "{}"'.format(
            i, view.word(sel.begin()), view.substr(view.word(sel.begin()))).replace('\n', '\\n'))
        print('    sel[{}] rowcol = {}'.format(i, view.rowcol(sel.begin())))
        print('    sel[{}] visible_region = {} {}'.format(i, view.visible_region(), type(view.visible_region())))
        print('    sel[{}] viewport_position = {}'.format(i, view.viewport_position()))
        print('    sel[{}] viewport_extent = {} {}'.format(i, view.viewport_extent(), type(view.viewport_extent())))
        print('    sel[{}] layout_extent = {} {}'.format(i, view.layout_extent(), type(view.layout_extent())))
        print('    sel[{}] text_to_layout (begin) = {} {}'.format(
            i, view.text_to_layout(sel.begin()), type(view.text_to_layout(sel.begin()))))
        # print('    sel[{}] word classify = {}'.format(i, view.classify(sel.begin())))
        # print('    sel[{}] scope name begin = {}'.format(i, view.scope_name(sel.begin())))
        # print('    sel[{}] indentation level begin = {}'.format(i, str(view.indentation_level(sel.begin()))))
        # print('    sel[{}] indented region begin = {}'.format(i, view.indented_region(sel.begin())))
        # print('    sel[{}] indented region begin substr = >>{}<<'.format(
        #   i, view.substr(view.indented_region(sel.begin()))))


def dump_neovintageous_view_settings(view):

    keys = [
        '_cmdline_cd',
        '_vintageous_cmdline_cd',
        '_vintageous_glue_until_normal_mode',
        '_vintageous_last_buffer_search',
        '_vintageous_last_buffer_search_command',
        '_vintageous_last_char_search_command',
        '_vintageous_last_character_search',
        '_vintageous_non_interactive',
        '_vintageous_processing_notation',
        '_vintageous_reset_during_init',
        'action',
        'action_count',
        'autoindent',
        'command_mode',
        'ex_data',
        'hlsearch',
        'ignorecase',
        'incsearch',
        'inverse_caret_state',
        'last_buffer_search',
        'linux_shell',
        'magic',
        'mode',
        'motion',
        'motion_count',
        'must_capture_register_name',
        'normal_insert_count',
        'partial_sequence',
        'recording',
        'register',
        'repeat_data',
        'rulers',
        'sequence',
        'showsidebar',
        'vi_editor_setting',
        'vintage',
        'vintageous_action',
        'vintageous_action_count',
        'vintageous_autoindent',
        'vintageous_cmdline_cd',
        'vintageous_command_mode',
        'vintageous_enable_cmdline_mode',
        'vintageous_enable_surround',
        'vintageous_ex_data',
        'vintageous_hlsearch',
        'vintageous_ignorecase',
        'vintageous_ignorecase',
        'vintageous_incsearch',
        'vintageous_inverse_caret_state',
        'vintageous_last_buffer_search',
        'vintageous_linux_shell',
        'vintageous_magic',
        'vintageous_magic',
        'vintageous_mode',
        'vintageous_motion',
        'vintageous_motion_count',
        'vintageous_must_capture_register_name',
        'vintageous_normal_insert_count',
        'vintageous_partial_sequence',
        'vintageous_recording',
        'vintageous_register',
        'vintageous_repeat_data',
        'vintageous_rulers',
        'vintageous_sequence',
        'vintageous_showsidebar',
        'vintageous_surround_spaces',
        'vintageous_use_ctrl_keys',
        'vintageous_use_sys_clipboard',
        'vintageous_vi_editor_setting',
        'VintageousEx_linux_shell',
        'VintageousEx_linux_terminal',
        'VintageousEx_osx_shell',
        'VintageousEx_osx_terminal',
        'visual_bloc',
        'visual_block_direction',
        'visualbell',
        'WrapPlus.include_line_ending',
        'xpos',
    ]

    print('>>> DEBUG NeoVintageous: view[id=%s,file=%s]')

    settings = view.settings()
    for key in keys:
        print('  {} = {}'.format(key, settings.get(key)))
    print('<<<')
