@ECHO OFF
CLS
SET /P name=Files to commit... 
IF "%name%"=="" (SET name=".") ELSE (SET name="./%name%")
SET /P cMsg=Summary message... 
IF "%cMsg%"=="" (
    SET name="Update %name%"
    SET cDsc=""
    GOTO upload_process
)
SET /P cDsc=Description... 
:upload_process
git add "%name%"
IF "%cDsc%" NEQ "" (git commit -m "%cMsg% | %cDsc%") ELSE (git commit -m "%cMsg%")
git push
ECHO. && ECHO Push done !
SET /P option=Open repository (Y/[N])? 
IF /I "%option%"=="Y" START chrome "https://github.com/TianTcl/KU01-challenge"
TIMEOUT 2