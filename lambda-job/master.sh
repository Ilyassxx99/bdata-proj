sudo hostnamectl set-hostname master && \
sudo service docker start && \
sudo kubeadm init --pod-network-cidr=10.244.0.0/16 && \
mkdir -p /home/ubuntu/.kube && \
sudo cp -i /etc/kubernetes/admin.conf /home/ubuntu/.kube/config && \
sudo chown $(id -u):$(id -g) /home/ubuntu/.kube/config && \
sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
