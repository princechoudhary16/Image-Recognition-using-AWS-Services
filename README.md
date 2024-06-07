# Image-Recognition-using-AWS-Services
This WebApp is basically used to deploy an image and get idea about the objects and things that we can see in it.
This project demonstrates how to perform image recognition using various AWS services. The project utilizes AWS Lambda, AWS S3 Bucket, AWS Image Rekognition, AWS CloudWatch Logs, AWS Amplify, AWS IAM, and AWS SNS to create an efficient image recognition system.
## Services Used

    AWS Lambda: Serverless compute service used to run code in response to events.
    AWS S3 Bucket: Object storage service used to store and trigger the Lambda function.
    AWS Image Rekognition: Deep learning-based image analysis service for image and video recognition.
    AWS CloudWatch Logs: Monitoring service used to collect and track logs from Lambda and other AWS services.
    AWS Amplify: Simplifies the deployment of web applications and provides easy integration with AWS services.
    AWS IAM: Identity and Access Management service used to control access permissions.
    AWS SNS: Simple Notification Service used to deliver output logs to subscribed client's email.

## Project Workflow

    Deploying Images:
        Users can deploy images to the website using the provided "Choose Image" option.
        The images are stored in the AWS S3 bucket.

    Triggering Lambda Function:
        Upon image deployment, the Lambda function is triggered automatically.

    Image Recognition:
        The Lambda function integrates with AWS Image Rekognition to perform image recognition on the deployed images.

    CloudWatch Logs:
        CloudWatch Logs record all events and activities that occur during the image recognition process.
        The Lambda function accesses these logs to retrieve the desired output.

    Delivering Output:
        AWS Amplify is integrated with S3 using the code inside index.html.
        A website is deployed using AWS Amplify's Drag and Drop method, allowing clients to access it via a generated URL.
        The Lambda function integrates with AWS SNS, where a topic is created and client emails are subscribed.
        The output logs in JSON format are delivered to the subscribed client's email via AWS SNS.

## Deployment Instructions

    Clone the repository to your local machine.
    Create an S3 Bucket to store the images for recognition.
    Set up the necessary IAM roles and permissions to enable communication between services.
    Deploy the Lambda function and respective codes for image recognition integration.
    Deploy the index.html file to AWS Amplify using the Drag and Drop method.
    Integrate AWS Amplify with S3 by following the code inside index.html.
    Create an SNS topic and subscribe client emails for output delivery.
    Ensure proper error handling and debugging by checking CloudWatch Logs for event tracking.

## Conclusion

This GitHub project showcases an image recognition system using AWS services. With the integration of Lambda, S3, Image Rekognition, CloudWatch Logs, Amplify, IAM, and SNS, the system efficiently detects and analyzes images, providing a seamless experience for clients and facilitating email-based output delivery.

Feel free to contribute to the project and make it even better! If you encounter any issues or have suggestions, please open an issue or submit a pull request. Happy coding!! 🚀
