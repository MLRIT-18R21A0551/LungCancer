sudo apt-get update
sudo apt update
yes Y | sudo apt install python3-pip
cd Lung_cancer
mkdir Dataset
cd Dataset
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1CU-eImDIGflCKbPHGdkodgtMp6RDfUjY' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1CU-eImDIGflCKbPHGdkodgtMp6RDfUjY" -O "Dataset_LUNA_16.zip"&& rm -rf /tmp/cookies.txt


