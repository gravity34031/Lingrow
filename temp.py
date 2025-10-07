Основы
    git init               # инициализировать репозиторий в текущей папке
    git clone URL          # клонировать удалённый репозиторий
    git status             # показать состояние файлов
    git help <cmd>         # помощь по команде

Работа с файлами
    git add .              # добавить все изменения в индекс
    git add file.txt       # добавить конкретный файл
    git commit -m "msg"    # сохранить изменения с сообщением
    git rm file.txt        # удалить файл и зафиксировать удаление
    git mv old new         # переименовать файл

Ветки
    git branch             # список веток
    git branch name        # создать ветку
    git checkout name      # переключиться на ветку
    git checkout -b name   # создать и перейти
    git merge name         # слить ветку в текущую
    git branch -d name     # удалить ветку

Удалённый репозиторий
    git remote -v              # показать подключённые репозитории
    git remote add origin URL  # добавить удалённый репозиторий
    git push -u origin main    # отправить ветку main на GitHub
    git push                   # отправить изменения
    git pull                   # получить и слить изменения
    git fetch                  # получить, но не сливать
    git clone URL              # клонировать проект

Работа с изменениями
    git diff                     # показать несохранённые изменения
    git diff --staged            # показать изменения, добавленные в индекс
    git log --oneline --graph --decorate # короткий лог коммитов
    git reset file.txt           # убрать файл из индекса
    git checkout -- file.txt     # отменить изменения в файле

Откаты и исправления
    git restore file.txt           # восстановить файл до последнего коммита
    git restore --staged file.txt  # убрать из индекса
    git revert <hash>              # создать коммит, отменяющий изменения
    git reset --hard <hash>        # откатить всё к указанному коммиту

Прочее полезное
    git log --oneline              # короткая история
    git show <hash>                # показать детали коммита
    git stash                      # временно спрятать изменения
    git stash pop                  # вернуть спрятанные изменения
    .gitignore                     # файл для исключений из Git