--Get[ImportString @ NotebookGet[ClipboardNotebook[]][[1, 1, 1]]]
tell application "System Events" to set focusedAppID to bundle identifier of first application process whose frontmost is true
tell application "Mathematica" to activate
tell application "System Events" to tell process "Mathematica"
	click menu item "Evaluate Notebook" of menu 1 of menu bar item "Evaluation" of menu bar 1
end tell
-- tell application id focusedAppID to activate
