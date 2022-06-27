

old_keys = {
        'normal': {
            '<Escape>': 'clear-keychain ;; search ;; fullscreen --leave',
            'o': 'set-cmd-text -s :open',
            'go': 'set-cmd-text :open {url:pretty}',
            'O': 'set-cmd-text -s :open -t',
            'gO': 'set-cmd-text :open -t -r {url:pretty}',
            'xo': 'set-cmd-text -s :open -b',
            'xO': 'set-cmd-text :open -b -r {url:pretty}',
            'wo': 'set-cmd-text -s :open -w',
            'wO': 'set-cmd-text :open -w {url:pretty}',
            '/': 'set-cmd-text /',
            '?': 'set-cmd-text ?',
            ':': 'set-cmd-text :',
            'ga': 'open -t',
            '<Ctrl+t>': 'open -t',
            '<Ctrl+n>': 'open -w',
            '<Ctrl+Shift+n>': 'open -p',
            'd': 'tab-close',
            '<Ctrl+w>': 'tab-close',
            '<Ctrl+Shift+w>': 'close',
            'D': 'tab-close -o',
            'co': 'tab-only',
            'T': 'set-cmd-text -sr :tab-focus',
            'gm': 'tab-move',
            'gK': 'tab-move -',
            'gJ': 'tab-move +',
            'J': 'tab-next',
            '<Ctrl+PgDown>': 'tab-next',
            'K': 'tab-prev',
            '<Ctrl+PgUp>': 'tab-prev',
            'gC': 'tab-clone',
            'r': 'reload',
            '<F5>': 'reload',
            'R': 'reload -f',
            '<Ctrl+F5>': 'reload -f',
            'H': 'back',
            '<Back>': 'back',
            'th': 'back -t',
            'wh': 'back -w',
            'L': 'forward',
            '<Forward>': 'forward',
            'tl': 'forward -t',
            'wl': 'forward -w',
            '<F11>': 'fullscreen',
            'f': 'hint',
            'F': 'hint all tab',
            'wf': 'hint all window',
            ';b': 'hint all tab-bg',
            ';f': 'hint all tab-fg',
            ';h': 'hint all hover',
            ';i': 'hint images',
            ';I': 'hint images tab',
            ';o': 'hint links fill :open {hint-url}',
            ';O': 'hint links fill :open -t -r {hint-url}',
            ';y': 'hint links yank',
            ';Y': 'hint links yank-primary',
            ';r': 'hint --rapid links tab-bg',
            ';R': 'hint --rapid links window',
            ';d': 'hint links download',
            ';t': 'hint inputs',
            'gi': 'hint inputs --first',
            'h': 'scroll left',
            'j': 'scroll down',
            'k': 'scroll up',
            'l': 'scroll right',
            'u': 'undo',
            'U': 'undo -w',
            '<Ctrl+Shift+t>': 'undo',
            'gg': 'scroll-to-perc 0',
            'G': 'scroll-to-perc',
            'n': 'search-next',
            'N': 'search-prev',
            'i': 'mode-enter insert',
            'v': 'mode-enter caret',
            'V': 'mode-enter caret ;; selection-toggle --line',
            '`': 'mode-enter set_mark',
            '\'': 'mode-enter jump_mark',
            'yy': 'yank',
            'yY': 'yank -s',
            'yt': 'yank title',
            'yT': 'yank title -s',
            'yd': 'yank domain',
            'yD': 'yank domain -s',
            'yp': 'yank pretty-url',
            'yP': 'yank pretty-url -s',
            'ym': 'yank inline [{title}]({url})',
            'yM': 'yank inline [{title}]({url}) -s',
            'pp': 'open -- {clipboard}',
            'pP': 'open -- {primary}',
            'Pp': 'open -t -- {clipboard}',
            'PP': 'open -t -- {primary}',
            'wp': 'open -w -- {clipboard}',
            'wP': 'open -w -- {primary}',
            'm': 'quickmark-save',
            'b': 'set-cmd-text -s :quickmark-load',
            'B': 'set-cmd-text -s :quickmark-load -t',
            'wb': 'set-cmd-text -s :quickmark-load -w',
            'M': 'bookmark-add',
            'gb': 'set-cmd-text -s :bookmark-load',
            'gB': 'set-cmd-text -s :bookmark-load -t',
            'wB': 'set-cmd-text -s :bookmark-load -w',
            'sf': 'save',
            'ss': 'set-cmd-text -s :set',
            'sl': 'set-cmd-text -s :set -t',
            'sk': 'set-cmd-text -s :bind',
            '-': 'zoom-out',
            '+': 'zoom-in',
            '=': 'zoom',
            '[[': 'navigate prev',
            ']]': 'navigate next',
            '{{': 'navigate prev -t',
            '}}': 'navigate next -t',
            'gu': 'navigate up',
            'gU': 'navigate up -t',
            '<Ctrl+a>': 'navigate increment',
            '<Ctrl+x>': 'navigate decrement',
            'wi': 'devtools',
            'wIh': 'devtools left',
            'wIj': 'devtools bottom',
            'wIk': 'devtools top',
            'wIl': 'devtools right',
            'wIw': 'devtools window',
            'wIf': 'devtools-focus',
            'gd': 'download',
            'ad': 'download-cancel',
            'cd': 'download-clear',
            'gf': 'view-source',
            'gt': 'set-cmd-text -s :tab-select',
            '<Ctrl+Tab>': 'tab-focus last',
            '<Ctrl+Shift+Tab>': 'nop',
            '<Ctrl+^>': 'tab-focus last',
            '<Ctrl+v>': 'mode-enter passthrough',
            '<Ctrl+q>': 'quit',
            'ZQ': 'quit',
            'ZZ': 'quit --save',
            '<Ctrl+f>': 'scroll-page 0 1',
            '<Ctrl+b>': 'scroll-page 0 -1',
            '<Ctrl+d>': 'scroll-page 0 0.5',
            '<Ctrl+u>': 'scroll-page 0 -0.5',
            '<Alt+1>': 'tab-focus 1',
            'g0': 'tab-focus 1',
            'g^': 'tab-focus 1',
            '<Alt+2>': 'tab-focus 2',
            '<Alt+3>': 'tab-focus 3',
            '<Alt+4>': 'tab-focus 4',
            '<Alt+5>': 'tab-focus 5',
            '<Alt+6>': 'tab-focus 6',
            '<Alt+7>': 'tab-focus 7',
            '<Alt+8>': 'tab-focus 8',
            '<Alt+9>': 'tab-focus -1',
            'g$': 'tab-focus -1',
            '<Ctrl+h>': 'home',
            '<Ctrl+s>': 'stop',
            '<Ctrl+Alt+p>': 'print',
            'Ss': 'set',
            'Sb': 'bookmark-list --jump',
            'Sq': 'bookmark-list',
            'Sh': 'history',
            '<Return>': 'selection-follow',
            '<Ctrl+Return>': 'selection-follow -t',
            '.': 'repeat-command',
            '<Ctrl+p>': 'tab-pin',
            '<Alt+m>': 'tab-mute',
            'gD': 'tab-give',
            'q': 'macro-record',
            '@': 'macro-run',
            'tsh': 'config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload',
            'tSh': 'config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload',
            'tsH': 'config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload',
            'tSH': 'config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload',
            'tsu': 'config-cycle -p -t -u {url} content.javascript.enabled ;; reload',
            'tSu': 'config-cycle -p -u {url} content.javascript.enabled ;; reload',
            'tph': 'config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload',
            'tPh': 'config-cycle -p -u *://{url:host}/* content.plugins ;; reload',
            'tpH': 'config-cycle -p -t -u *://*.{url:host}/* content.plugins ;; reload',
            'tPH': 'config-cycle -p -u *://*.{url:host}/* content.plugins ;; reload',
            'tpu': 'config-cycle -p -t -u {url} content.plugins ;; reload',
            'tPu': 'config-cycle -p -u {url} content.plugins ;; reload',
            'tih': 'config-cycle -p -t -u *://{url:host}/* content.images ;; reload',
            'tIh': 'config-cycle -p -u *://{url:host}/* content.images ;; reload',
            'tiH': 'config-cycle -p -t -u *://*.{url:host}/* content.images ;; reload',
            'tIH': 'config-cycle -p -u *://*.{url:host}/* content.images ;; reload',
            'tiu': 'config-cycle -p -t -u {url} content.images ;; reload',
            'tIu': 'config-cycle -p -u {url} content.images ;; reload',
            'tch': 'config-cycle -p -t -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload',
            'tCh': 'config-cycle -p -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload',
            'tcH': 'config-cycle -p -t -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload',
            'tCH': 'config-cycle -p -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload',
            'tcu': 'config-cycle -p -t -u {url} content.cookies.accept all no-3rdparty never ;; reload',
            'tCu': 'config-cycle -p -u {url} content.cookies.accept all no-3rdparty never ;; reload',
            },
            'caret': {
                    'v': 'selection-toggle',
                    'V': 'selection-toggle --line',
                    '<Space>': 'selection-toggle',
                    '<Ctrl+Space>': 'selection-drop',
                    'c': 'mode-enter normal',
                    'j': 'move-to-next-line',
                    'k': 'move-to-prev-line',
                    'l': 'move-to-next-char',
                    'h': 'move-to-prev-char',
                    'e': 'move-to-end-of-word',
                    'w': 'move-to-next-word',
                    'b': 'move-to-prev-word',
                    'o': 'selection-reverse',
                    ']': 'move-to-start-of-next-block',
                    '[': 'move-to-start-of-prev-block',
                    '}': 'move-to-end-of-next-block',
                    '{': 'move-to-end-of-prev-block',
                    '0': 'move-to-start-of-line',
                    '$': 'move-to-end-of-line',
                    'gg': 'move-to-start-of-document',
                    'G': 'move-to-end-of-document',
                    'Y': 'yank selection -s',
                    'y': 'yank selection',
                    '<Return>': 'yank selection',
                    'H': 'scroll left',
                    'J': 'scroll down',
                    'K': 'scroll up',
                    'L': 'scroll right',
                    '<Escape>': 'mode-leave',
                    },
            'command': {
                    '<Ctrl+p>': 'command-history-prev',
                    '<Ctrl+n>': 'command-history-next',
                    '<Up>': 'completion-item-focus --history prev',
                    '<Down>': 'completion-item-focus --history next',
                    '<Shift+Tab>': 'completion-item-focus prev',
                    '<Tab>': 'completion-item-focus next',
                    '<Ctrl+Tab>': 'completion-item-focus next-category',
                    '<Ctrl+Shift+Tab>': 'completion-item-focus prev-category',
                    '<PgDown>': 'completion-item-focus next-page',
                    '<PgUp>': 'completion-item-focus prev-page',
                    '<Ctrl+d>': 'completion-item-del',
                    '<Shift+Del>': 'completion-item-del',
                    '<Ctrl+c>': 'completion-item-yank',
                    '<Ctrl+Shift+c>': 'completion-item-yank --sel',
                    '<Return>': 'command-accept',
                    '<Ctrl+Return>': 'command-accept --rapid',
                    '<Ctrl+b>': 'rl-backward-char',
                    '<Ctrl+f>': 'rl-forward-char',
                    '<Alt+b>': 'rl-backward-word',
                    '<Alt+f>': 'rl-forward-word',
                    '<Ctrl+a>': 'rl-beginning-of-line',
                    '<Ctrl+e>': 'rl-end-of-line',
                    '<Ctrl+u>': 'rl-unix-line-discard',
                    '<Ctrl+k>': 'rl-kill-line',
                    '<Alt+d>': 'rl-kill-word',
                    '<Ctrl+w>': 'rl-rubout " "',
                    '<Ctrl+Shift+w>': 'rl-filename-rubout',
                    '<Alt+Backspace>': 'rl-backward-kill-word',
                    '<Ctrl+y>': 'rl-yank',
                    '<Ctrl+?>': 'rl-delete-char',
                    '<Ctrl+h>': 'rl-backward-delete-char',
                    '<Escape>': 'mode-leave',
                    },
            'hint': {
                    '<Return>': 'hint-follow',
                    '<Ctrl+r>': 'hint --rapid links tab-bg',
                    '<Ctrl+f>': 'hint links',
                    '<Ctrl+b>': 'hint all tab-bg',
                    '<Escape>': 'mode-leave',
                    },
            'insert': {
                    '<Ctrl+e>': 'edit-text',
                    '<Shift+Ins>': 'insert-text -- {primary}',
                    '<Escape>': 'mode-leave',
                    '<Shift+Escape>': 'fake-key <Escape>',
                    },
            'passthrough': {
                    '<Shift+Escape>': 'mode-leave',
                    },
            'prompt': {
                    '<Return>': 'prompt-accept',
                    '<Ctrl+x>': 'prompt-open-download',
                    '<Ctrl+p>': 'prompt-open-download --pdfjs',
                    '<Shift+Tab>': 'prompt-item-focus prev',
                    '<Up>': 'prompt-item-focus prev',
                    '<Tab>': 'prompt-item-focus next',
                    '<Down>': 'prompt-item-focus next',
                    '<Alt+y>': 'prompt-yank',
                    '<Alt+Shift+y>': 'prompt-yank --sel',
                    '<Ctrl+b>': 'rl-backward-char',
                    '<Ctrl+f>': 'rl-forward-char',
                    '<Alt+b>': 'rl-backward-word',
                    '<Alt+f>': 'rl-forward-word',
                    '<Ctrl+a>': 'rl-beginning-of-line',
                    '<Ctrl+e>': 'rl-end-of-line',
                    '<Ctrl+u>': 'rl-unix-line-discard',
                    '<Ctrl+k>': 'rl-kill-line',
                    '<Alt+d>': 'rl-kill-word',
                    '<Ctrl+w>': 'rl-rubout " "',
                    '<Ctrl+Shift+w>': 'rl-filename-rubout',
                    '<Alt+Backspace>': 'rl-backward-kill-word',
                    '<Ctrl+?>': 'rl-delete-char',
                    '<Ctrl+h>': 'rl-backward-delete-char',
                    '<Ctrl+y>': 'rl-yank',
                    '<Escape>': 'mode-leave',
                    },
            'register': {
                    '<Escape>': 'mode-leave',
                    },
            'yesno': {
                    '<Return>': 'prompt-accept',
                    'y': 'prompt-accept yes',
                    'n': 'prompt-accept no',
                    'Y': 'prompt-accept --save yes',
                    'N': 'prompt-accept --save no',
                    '<Alt+y>': 'prompt-yank',
                    '<Alt+Shift+y>': 'prompt-yank --sel',
                    '<Escape>': 'mode-leave',
                    },
        }
