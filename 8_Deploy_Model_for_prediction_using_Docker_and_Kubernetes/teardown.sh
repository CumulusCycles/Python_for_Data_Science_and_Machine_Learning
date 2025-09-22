kubectl delete -k k8s/ 
kubectl get namespaces | grep diabetes-predictor
kubectl get all -n diabetes-predictor
docker rmi pima-diabetes-api && docker rmi pima-diabetes-app