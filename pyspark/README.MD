sparkTraining
spark training

install java
sudo apt install openjdk-19-jdk
set JAVA_HOME
javac --version ls /usr/lib/jvm readlink -f $(which javac) | sed "s:/bin/javac::" export JAVA_HOME=/usr/lib/jvm/java-19-openjdk-amd64 echo $JAVA_HOME