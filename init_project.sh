#!/bin/bash

if [ $# != 1 ]; then
  echo Usage: "$0 project_name"
  exit 1
fi

PROJECT_NAME=$1
echo "Change the project name 'webapi'  to '$PROJECT_NAME'"
echo "================================================================"
echo ""

# change the code
file_list=(src/webapi/wsgi.py src/webapi/settings.py src/webapi/asgi.py src/manage.py src/uwsgi.ini docker-compose.yml README.md pytest.ini infra/mysql/dockerfile)
tmpfile=$(mktemp)
for i in "${file_list[@]}"
do
  echo "Change the keyword 'webapi' to '$PROJECT_NAME' in $i"
  sed -e "s/webapi/$PROJECT_NAME/g" $i > $tmpfile
  mv $tmpfile $i
done

# change the directory name
echo ""
echo "Change the directory name src/webapi to src/$PROJECT_NAME"
mv src/webapi src/$PROJECT_NAME

echo ""
echo "done!!"
exit 0
