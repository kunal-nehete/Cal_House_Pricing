# Cal_House_Pricing
SOftware / Tools
1. Github Account
2. HerokuAccount
3. VSCodeIDE
4. GitCLI
---
Create a new environment
conda create -p venv python==3.7 -y
---
if problem with storing temp file,
then change temp file location to E:\Temp

set set TMP=E:\Temp
set TEMP=E:\Temp
---
select environment
conda activate E:\DepEtEProject\Cal_House_Pricing\venv
or
conda activate venv/
---
install Libraries required
---
check git global user.name and user.email
git config --global user.name
Kunal Nehete
git config --global user.email   
kunalnehete@gmail.com
---
add file in the local 
git add .  (to add all files)
git add Libraries_required.txt  (add specific file)
git status (to check present files)
...(search on net for all git steps)
---
commit local files to push to staging environment
(git commit tutorial steps read on net)
git commit -m "This commit includ
e Libraries_required.txt and README.md files"
---
push files from stage env "origin" to "main"
