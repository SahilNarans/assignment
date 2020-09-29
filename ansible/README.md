#Ansible Install helm chart with Dynamic Inventory

# inventory.py script is for run dynamic inventory

#Run below command to install helm chart on kuberntes

ansible-playbook -i inventory.py --list-hosts helm-install-playbook.yaml -vvv -b

#If you want to print host list with script to check, just run below command

python3 /etc/puppet/scripts/generate_inventory.py --list

#Change inventory url or api url as per your inventory
