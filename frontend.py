import gradio as gr
import requests

def process_video(video_file):
    # Send a POST request to the Flask app
    url = "http://localhost:5000/process_video"
    files = {'video': video_file}
    response = requests.post(url, files=files)
    
    # Get the response JSON and return it
    info = response.json()
    value1 = info.get('summary')
    value2 = info.get('keywords')
    return value1, value2

app = gr.Interface(fn=process_video, inputs=gr.Video(label="视频文件"), outputs=[gr.Text(label="摘要"), gr.Text(label="主题词")], description="上传视频，输出视频摘要和主题词")


if __name__ == "__main__":
    app.launch(share=True)