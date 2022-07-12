
Hey bro, hope everything is cool. 


If you have come this far is because you are interested in my solution to the TIP.


There are two folders here, one is the test_lambda_tip this is a function that cleans and calculates the kpi's each month, it was tought to use is as a lambda function when the Iberia people upload files to aws S3 bucket. 


The app_kpi is the app itself you should run the application.py 


for the dashboard log ing username:hello and Password: world


The application runs with csv files since I figured out that each year you will need:

TOTAL SIZE OF THE 4 CSV's WITH THE KPI IS 2 KB more or less
So each year you will have 6 *2 = 12 kb of data
In 5 years you will have 60 kb of data

for managing this amounts of data there is no need to create a Data base, a bucket is more than enoguth because is cheaper. 

So i decided to go for aws ELASTICBEANTALK that combines EC2 INSTANCE, S3 BUCKET, LOAD BALANCING, WATCHDOG, AUTOSCALING, HEALTMONITORING


There is no need for a DB with this great solution, and the coders can focus in coding. 


Happy coding guys. I will upload a pp also with my solutions architecture 
