import os
import shutil

from core.ffmpeg_utils import (
    extract_frames,
    create_video,
    convert_60fps
)

from ai.realesrgan_upscale import RealESRGANUpscaler



class VideoProcessor:


    def __init__(self):

        self.upscaler = RealESRGANUpscaler()



    def process_video(
            self,
            input_video,
            output_video,
            enable_60fps=False
    ):

        work_dir = "workspace"

        frames_dir = os.path.join(
            work_dir,
            "frames"
        )

        upscale_dir = os.path.join(
            work_dir,
            "upscaled_frames"
        )


        # Clean old files
        if os.path.exists(work_dir):
            shutil.rmtree(work_dir)


        os.makedirs(
            upscale_dir,
            exist_ok=True
        )


        # Step 1: Extract video frames

        extract_frames(
            input_video,
            frames_dir
        )



        # Step 2: AI Upscale frames

        for frame in os.listdir(frames_dir):

            if frame.endswith(".png"):

                input_frame = os.path.join(
                    frames_dir,
                    frame
                )

                output_frame = os.path.join(
                    upscale_dir,
                    frame
                )


                self.upscaler.upscale_image(
                    input_frame,
                    output_frame
                )



        # Step 3: Create 4K video

        create_video(
            upscale_dir,
            output_video,
            fps=30
        )



        # Step 4: Optional 60 FPS

        if enable_60fps:

            temp_video = output_video.replace(
                ".mp4",
                "_30fps.mp4"
            )

            os.rename(
                output_video,
                temp_video
            )


            convert_60fps(
                temp_video,
                output_video
            )



        # Remove temporary files

        shutil.rmtree(
            work_dir,
            ignore_errors=True
        )


        return output_video




if __name__ == "__main__":

    processor = VideoProcessor()

    processor.process_video(
        "input.mp4",
        "output_4K.mp4",
        enable_60fps=True
    )

    print(
        "4K Upscaling Completed"
    )
