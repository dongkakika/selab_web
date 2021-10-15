cd initialize\linux
sh x1_delete_all_migrations_and_db.sh

git add -u
git commit -a -m 'version update'
git push origin master

git add *
git commit -m 'version update'
git push origin master
