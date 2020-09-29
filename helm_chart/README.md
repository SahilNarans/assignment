## To create a helm chart application

#STEP 1: Create a helm chart with below mentioned command

helm create hello-world

#it will create templates of deployment and service files to use for deployments.

#STEP 2: modify deployment files as per your requirement and there is one values.yaml, where you mention resources of deployment files, which you want to use.

#STEP 3: with the below mention command, you can check your deployment templates.

helm template ./hello-world

#STEP 4: After verification of deployments charts, we can run below mentioned command to run a deployment or install a chart in your cluster.

For Helm Version2

helm install --name hello-world ./hello-world

#For Helm Version3

helm install --generate-name ./hello-world

or 

helm install hello-world ./hello-world

#your application is deployed now, now you can check everything with kubectl commands

#To check the installed charts on cluster, use below mentioned command

helm ls --all

#STEP 5: like if you have done any done changes in your charts.

helm upgrade hello-world ./hello-world


#STEP 6: To delete everything of deployed service, use below mentioned command

helm uninstall hello-world


