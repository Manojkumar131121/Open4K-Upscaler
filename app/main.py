import os
import gradio as gr

from core.video_processor import VideoProcessor


processor = VideoProcessor()



def upscale_video(
        video,
        enable_60fps
):

    if video is None:
        return None


    input_path = video


    output_path = (
        "outputs/"
        + "Open4K_result.mp4"
    )


    os.makedirs(
        "outputs",
        exist_ok=True
    )


    result = processor.process_video(
        input_path,
        output_path,
        enable_60fps
    )


    return result




with gr.Blocks(
    title="Open4K AI Upscaler"
) as app:


    gr.Markdown(
        """
        # 🚀 Open4K AI Video Upscaler

        AI powered 4K video enhancement using:
        
        - Real-ESRGAN
        - GFPGAN Face Enhancement
        - FFmpeg Processing
        - 60 FPS Interpolation
        """
    )


    with gr.Row():

        video_input = gr.Video(
            label="Upload Video"
        )


        output_video = gr.Video(
            label="4K Output"
        )



    fps_checkbox = gr.Checkbox(
        label="Enable 60 FPS Smooth Motion",
        value=False
    )


    upscale_button = gr.Button(
        "✨ Upscale To 4K"
    )


    upscale_button.click(
        fn=upscale_video,
        inputs=[
            video_input,
            fps_checkbox
        ],
        outputs=output_video
    )



app.launch(
    server_name="0.0.0.0",
    share=True
)
