# Nodejs app deployment (manual)

1. Vagrant up 
2. gem install bundler
3. cd into environment/spec-tests 
   - rake spec
   - tests fail as we don't have all packages installed in our vagrant box
2. Open separate git terminal, vagrant ssh
   - sudo apt-get update -y
   - sudo apt-get install nodejs -y
   - sudo apt-get install python-software-properties
   - curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
   - sudo apt-get update -y
   - sudo npm install pm2 -g
3. Run rake spec, tests should now all pass
4. cd into app/app
   - npm install
   - npm start
5. App is now ready and listening at port 3000

