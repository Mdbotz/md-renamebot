echo "Cloning Repository"
git clone https://github.com/Mdbotz/md-renamebot -b $BRANCH /EvaMaria
cd /md-renamebot 
echo "installing requirements"
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
