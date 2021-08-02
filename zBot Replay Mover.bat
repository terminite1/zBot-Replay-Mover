@echo off
title zBot Replay Mover
:start
cls
type donottouch.txt
echo.
set /p replay=Enter the name of the replay: 
set /p extension=Enter the extension of the file (e.x zbot, zbf): 
if EXIST %replay%.%extension% (
goto move
) else goto error

:move
move "C:\Users\%USERNAME%\Downloads\zBot Replay Mover\%replay%.%extension%" "C:\Program Files (x86)\Steam\steamapps\common\Geometry Dash\replays\%replay%.%extension%"
echo Replay moved successfully!
echo.
pause
goto start

:error
echo File Not Found. Did you type the name correctly?
echo.
pause
goto start