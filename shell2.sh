sudo apt-get install python-pip python-dev build-essential 
sudo apt-get install python3-pip python3-dev build-essential
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 
sudo pip install pygsr
sudo pip install pygst
sudo pip install pyttsx
sudo pip install SpeechRecognition
sudo apt-get install python3-matplotlib
sudo pip install gTTS
sudo apt-get install espeak
sudo pip install speech
sudo apt-get install python-pyaudio python3-pyaudio
sudo apt-get install libasound-dev
git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
cd pyaudio
sudo python setup.py install
sudo pip install microphone
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
sudo apt-get install python-pyaudio
sudo apt-get install mpg321
sudo pip install pypiwin32

sudo apt-get install sphinxsearch
sudo apt-get install mercurial python-dev python-numpy python-opengl \
    libav-tools libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
    libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm timgm6mb-soundfont \
    xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf
hg clone https://bitbucket.org/pygame/pygame
cd pygame
python setup.py build
sudo python setup.py install
sudo apt-get install mercurial python3-dev python3-setuptools python3-numpy python3-opengl \
    libav-tools libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
    libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm timgm6mb-soundfont \
    xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf
hg clone https://bitbucket.org/pygame/pygame
cd pygame
python3 setup.py build
sudo python3 setup.py install


