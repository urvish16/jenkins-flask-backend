# Flask Backend — Jenkins CI/CD Assignment

Flask API (student data submission) deployed to a single EC2 instance under
`pm2`, redeployed automatically by a Jenkins pipeline on every push to `main`.

- App: `app.py` — `/submit` (POST) and `/health` (GET), port 5000, MongoDB
  Atlas via `MONGO_URI`.
- `Jenkinsfile`: checkout -> Python syntax check -> SSH into the EC2 instance,
  `git pull`, `pip install`, `pm2 restart flask-backend`.

See [jenkins-cicd-assignment](https://github.com/urvish16/jenkins-cicd-assignment)
for the full deployment + CI/CD writeup (EC2 setup, Jenkins configuration,
webhook wiring, screenshots) and the
[jenkins-express-frontend](https://github.com/urvish16/jenkins-express-frontend)
repo for the other half of the app.
