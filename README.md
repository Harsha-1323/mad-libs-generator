# RUN
docker build -t madlibs-app:latest .
docker run -d -p 5000:5000 --name madlibs madlibs-app
