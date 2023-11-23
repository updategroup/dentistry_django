# build_files.sh
echo "Start Build"
pip install -r requirements.txt

# make migrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic --noinput --clear

echo "Build files done"
