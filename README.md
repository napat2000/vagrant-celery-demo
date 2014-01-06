bensmom
=======

Install the following first:
 - vagrant (http://www.vagrantup.com/downloads.html)
 - ansible 1.4 (http://docs.ansible.com/intro_installation.html)  (sudo pip install ansible==1.4)
 - virtualbox (https://www.virtualbox.org/wiki/Downloads)

Then: 
 - git clone https://github.com/fivestars/vagrant-celery-demo.git into a folder of your choosing.
 - cd vagrant-celery-demo/
 - vagrant up
 - (sometimes the initial provision times out at the 'gathering facts' stage because vagrant VM is not fully up yet; if you see an error that says something about an ssh timeout, simply do 'vagrant provision' to resume the provisioning)
 - (for now...) run the server by vagrant ssh'ing into the vm, and then python code/manage.py runserver 0.0.0.0:8000
 - (for now...) run celeryd by vagrant ssh'ing, then python code/manage.py celeryd -B -E --loglevel=INFO
 - (and finally...) vagrant ssh; python code/manage.py celerycam to start celerycam


TO DO
=====

1. use supervisord to get all services running (last 3 steps above).
2. figure out a way to use the rabbitmq management plugin which shows queues.
3. same for celery-flower.
4. flesh out the django app with more examples of celery tasks (I'm thinking of a simple all-in-one django view with a form that lets users create a large number of tasks, where they choose the type of task to schedule, and the many different task options also)
5. clean up the django app with a better name; get rid of the "polls" app which I partially copy-pastad from django tutorial, because I didn't want to spend time thinking about those things at the time.
6. I didn't set up a virtualenv, because I didn't see a reason for it if all the code's running in a VM anyway. (... or maybe I don't understand the reason for a virtualenv, in which case, do let me know)
7. there are probably other things which I'm forgetting right now.
