####### Update the colonical favaour #####################
sudo apt update

########## Install the dependencies #####################
sudo apt-get install libssl-dev libcurl4-openssl-dev liblog4cplus-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gstreamer1.0-plugins-base-apps gstreamer1.0-plugins-bad gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools

########## Enter into the directory #####################
cd amazon-kinesis-video-streams-webrtc-sdk-c
########## Create the folder ############################
mkdir build

############ Dependencies ###############################
sudo apt install cmake
cmake .. -DBUILD_STATIC_LIBS=TRUE
sudo apt install default-jdk
sudo apt install clang
sudo apt install build-essential
cmake .. -DBUILD_STATIC_LIBS=TRUE


######### Finally ######################################
make



