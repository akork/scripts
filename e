emacsclient -e "(ak-dired \"$(pwd)\" \"$1\")"
osascript -e 'tell application "System Events"
                set theProcess to first application process whose displayed name is "Emacs"
                set frontmost of theProcess to true
        end tell'
