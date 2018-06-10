# newsblog


#Install Redis

-sudo apt install redis-server

#run redis
- open terminal and run cmd $redis-server

#run celery worker

- open terminal
- goto blog folder and run 
- $celery worker -A blog --loglevel=debug --concurrency=4

#enable less secure apps for gmail in order to send mails
- https://myaccount.google.com/lesssecureapps