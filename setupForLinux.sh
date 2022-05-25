sudo apt-get update
sudo apt update
yes Y | sudo apt install python3-pip
cd Lung_cancer
mkdir Dataset
cd Dataset
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1CU-eImDIGflCKbPHGdkodgtMp6RDfUjY' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1CU-eImDIGflCKbPHGdkodgtMp6RDfUjY" -O "Dataset_LUNA_16.zip"&& rm -rf /tmp/cookies.txt
yes Y | sudo apt-get install unzip
unzip Dataset_LUNA_16

sudo apt update -qq
yes Y | sudo apt install --no-install-recommends software-properties-common dirmngr
sudo wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
yes '\n' | sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"

yes Y | sudo apt install --no-install-recommends r-base

#add CRAN repositories
yes '\n' | sudo add-apt-repository ppa:c2d4u.team/c2d4u4.0+

#install R packages
sudo R -e "install.packages('rpart')"
sudo R -e "install.packages('rpart.plot')"
sudo R -e "install.packages('caret')"

#install python dependencies
yes Y | sudo apt-get install python3-tk

sudo snap install code --classic
