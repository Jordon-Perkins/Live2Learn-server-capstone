#!/bin/bash

echo "Saving UserProfile"
python manage.py dumpdata live2learnapi.UserProfile --indent 4 > live2learnapi/fixtures/userProfiles.json

echo "Saving Tokens"
python manage.py dumpdata authtoken.token --indent 4 > live2learnapi/fixtures/tokens.json

echo "Saving Classes"
python manage.py dumpdata live2learnapi.thisclass --indent 4 > live2learnapi/fixtures/classes.json

echo "Saving Instuctors"
python manage.py dumpdata live2learnapi.instructor --indent 4 > live2learnapi/fixtures/instructors.json

echo "Saving Tags"
python manage.py dumpdata live2learnapi.tag --indent 4 > live2learnapi/fixtures/tags.json

echo "Saving Students"
python manage.py dumpdata live2learnapi.student --indent 4 > live2learnapi/fixtures/students.json

