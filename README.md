Vagran Celery Demo
=======

Install the following first:
 - vagrant (http://www.vagrantup.com/downloads.html)
 - ansible 1.4 (http://docs.ansible.com/intro_installation.html)  (sudo pip install ansible==1.4)
 - virtualbox (https://www.virtualbox.org/wiki/Downloads)

Then: 
 - git clone https://github.com/fivestars/vagrant-celery-demo.git into a folder of your choosing.
 - cd vagrant-celery-demo/
 - vagrant up
 - sometimes the initial provision times out at the 'gathering facts' stage because vagrant VM is not fully up yet; if you see an error that says something about an ssh timeout, simply do 'vagrant provision' to resume the provisioning

On the host computer:
 - Django server should be accessible at http://localhost:8080
 - RabbitMQ management UI should be accessible at http://localhost:8081
 - Celery Flower should be accessible at http://localhost:8082

TO DO
=====

 - use supervisord to get all services running (last 3 steps above).
 - flesh out the django app with more examples of celery tasks (I'm thinking of a simple all-in-one django view with a form that lets users create a large number of tasks, where they choose the type of task to schedule, and the many different task options also)
 - clean up the django app with a better name; get rid of the "polls" app which I partially copy-pastad from django tutorial, because I didn't want to spend time thinking about those things at the time.
 - there are probably other things which I'm forgetting right now.
