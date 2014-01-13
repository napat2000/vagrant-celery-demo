Vagrant Celery Demo
===================

### Install the following first:
 - vagrant (http://www.vagrantup.com/downloads.html)
 - ansible 1.4 (http://docs.ansible.com/intro_installation.html)  
   - `sudo pip install ansible==1.4` if you have pip
 - virtualbox (https://www.virtualbox.org/wiki/Downloads)

### Then:
===
 - `git clone https://github.com/fivestars/vagrant-celery-demo.git` into a folder of your choosing.
 - `cd vagrant-celery-demo/`
 - `vagrant up`
NB: Sometimes the initial provision times out at the 'gathering facts' stage because vagrant VM is not fully up yet; if you see an error that says something about an ssh timeout, simply do 'vagrant provision' to resume the provisioning

### On the host computer:
 - Django server should be accessible at http://localhost:8080
   - go to http://localhost:8080/sample_tasks/ to start scheduling tasks
   - you can also follow tasks at http://localhost:8080/admin/djcelery/taskstate (id=guest, password=guest)
 - RabbitMQ management UI should be accessible at http://localhost:8081
   - login using id=guest, password=guest at http://localhost:8081/ to monitor queues on rabbitMQ
 - Celery Flower should be accessible at http://localhost:8082
   - monitor tasks on Flower at http://localhost:8082/tasks

### Default users/passwords:
 - Django superuser: guest/guest
 - Rabbitmq: guest/guest
 - PostgresDB: guest/guest

### You may use supervisorctl to check status, start, or stop
 - vagrant ssh into VM
 - `cd code/`
 - `supervisorctl status`
 - `supervisorctl start all`
 - `supervisorctl stop all`

### Logs are stored as follows (on the VM):
 - django server: /var/logs/djangoserver.log
 - celeryworker: /var/logs/celeryworker.log
 - celeryflower: /var/logs/flower.log
 - celerycam: /var/logs/celerycam.log
 - supervisord: /var/logs/supervisord.log

### TO DO
 - refactor playbook.yml using tags/roles so a lot of the setup-related tasks only run on first provision
 - try to stop/start rabbitmq-server using supervisord (currently always on)
 - add comments in supervisord.conf
