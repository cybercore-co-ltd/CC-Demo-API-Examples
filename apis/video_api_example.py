import requests
import argparse
import os
import time
from utils import WEB_URL, task2id

# ------------------------------------------------------------------------------
# VIDEO
# -----------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(description="Video API Example")
    parser.add_argument("input_video_path", type=str)
    parser.add_argument("output_video_path", type=str)
    parser.add_argument("--token", type=str)
    parser.add_argument("--task_name", type=str, default="traffic_monitoring", choices=list(task2id.keys()))
    
    args = parser.parse_args()
    print(args)
    return args

if __name__ == "__main__":
    args = parse_args()
    task_id = task2id.get(args.task_name, -1)
    assert task_id != -1, f"Task name {args.task_name} not yet supported."

    # Send request upload video to server
    response = requests.post(f"{WEB_URL}/upload/video",
                            files={'file': open(args.input_video_path, 'rb')},
                            data={'task_id': task_id},
                            headers={"Authorization": f"Bearer {args.token}"})

    data = response.json()
    if response.status_code == 200:
        print(f"Your video {os.path.basename(args.input_video_path)} is uploaded successfully to server !!!")
        video_id = data["id"]
        video_hostname = data["host_name"]
        video_progress = data["progress"]

        # Wait progress of the video to 100%
        print(f"Waiting progress of the uploaded video {os.path.basename(args.input_video_path)} to 100%")
        while (video_progress != "100%"):
            response = requests.get(f"{WEB_URL}/{video_hostname}/video_item/{video_id}",
                                    headers={"Authorization": f"Bearer {args.token}"})
            assert response.status_code == 200, "Error when check progress of the video"
            video_progress = response.json()["progress"]
            print(f"Current video progress: {video_progress}")
            time.sleep(1)
        
        # Download output video
        response = requests.get(f"{WEB_URL}/{video_hostname}/download_video/{video_id}",
                                headers={"Authorization": f"Bearer {args.token}"})
        assert response.status_code == 200, "Error when download output video"

        with open(args.output_video_path, "wb") as file:
            file.write(response.content)

        print(f"Output video has been saved at {args.output_video_path}")
    else:
        err_message = data['message']
        print(f"Error when upload video {os.path.basename(args.input_video_path)} to server: {err_message}")



