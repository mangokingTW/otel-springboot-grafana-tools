#bin/bash

curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION="v1.24.16+k3s1" sh -
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
snap install helm --classic
mkdir -p ~/.kube
kubectl config view --raw > ~/.kube/config

helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

kubectl create ns observability

cd kubernetes/promtail
helm upgrade --install promtail grafana/promtail --version 6.15.3 -n observability -f promtail.yaml

helm upgrade --install loki grafana/loki-distributed --version 0.76.0 -n observability

cd ../tempo
kubectl apply -f minio.yaml
helm upgrade --install tempo grafana/tempo-distributed --version 1.6.13 -n observability -f tempo.yaml

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

cd ../prometheus-grafana
helm upgrade --install kube-prometheus-stack prometheus-community/kube-prometheus-stack --version 52.0.1 -n observability -f values.yaml

cd ../springboot-app
kubectl apply -f springboot-app.yaml

cd ../python-app
kubectl apply -f python-app.yaml

kubectl get svc -l app=springboot-app
kubectl get svc -n observability kube-prometheus-stack-grafana
