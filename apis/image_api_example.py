import requests
import argparse
import os
from utils import WEB_URL, task2id

# ------------------------------------------------------------------------------
# IMAGE
# -----------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(description="Image API Example")
    parser.add_argument("input_image_path", type=str)
    parser.add_argument("output_image_path", type=str)
    parser.add_argument("--token", type=str)
    parser.add_argument("--task_name", type=str, default="traffic_monitoring", choices=list(task2id.keys()))
    
    args = parser.parse_args()
    print(args)
    return args

if __name__ == "__main__":
    args = parse_args()
    task_id = task2id.get(args.task_name, -1)
    assert task_id != -1, f"Task name {args.task_name} not yet supported."
    response = requests.post(f"{WEB_URL}/upload/image",
                            files={'file': open(args.input_image_path, 'rb')},
                            data={'task_id': task_id},
                            headers={"Authorization": f"Bearer {args.token}"})

    data = response.json()
    if response.status_code == 200:
        print(f"Your image {os.path.basename(args.input_image_path)} is uploaded successfully to server !!!")
        with open(args.output_image_path, "wb") as file:
            file.write(response.content)
        print(f"Output image has been saved at {args.output_image_path}")
    else:
        err_message = data['message']
        print(f"Error when upload image {os.path.basename(args.input_image_path)} to server: {err_message}.")