# API Examples for Cybercore AI Platform

---

## Table of contents

1. [Login](#1-login)

- Login with Google Account to get token for sending request to server.

2. [API Examples](#2-api)

- Guidelines for sending request to server.
- Support API Examples for both image and video.
- Support inference on many different tasks. For example: Traffic Monitoring, Human Analysis, ...

---

## 1. Login

- Firstly, open this [url](http://trafficmonitor.cybercore.co.jp/user/login) in new tab on your browser, this will redirect to the login page using google account.
- Secondly, enter your google account email and password to complete the login phase.
- Finally, if you login successfully, your browser will display access token.

## 2. API Examples

1. Upload Image

- Run the following script to inference with an input image to server. List of supported task names ["traffic_monitoring", "human_analysis"]:

```bash
python apis/image_api_example.py $INPUT_IMAGE_PATH $OUTPUT_IMAGE_PATH --token $YOUR_TOKEN --task_name $TASK_NAME
```

2. Upload Video

- Run the following script to inference with an input video to server. List of supported task names ["traffic_monitoring", "human_analysis"]:

```bash
python apis/video_api_example.py $INPUT_VIDEO_PATH $OUTPUT_VIDEO_PATH --token $YOUR_TOKEN --task_name $TASK_NAME
```
