import subprocess
import os


def run_ffmpeg(command):
    """
    Execute FFmpeg command
    """

    process = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if process.returncode != 0:
        raise Exception(
            process.stderr
        )

    return process.stdout



def extract_frames(
        video_path,
        output_folder,
        fps=None
):

    os.makedirs(
        output_folder,
        exist_ok=True
    )


    command = [
        "ffmpeg",
        "-i",
        video_path
    ]


    if fps:
        command += [
            "-vf",
            f"fps={fps}"
        ]


    command += [
        os.path.join(
            output_folder,
            "frame_%08d.png"
        )
    ]


    run_ffmpeg(command)

    return output_folder



def create_video(
        frames_folder,
        output_path,
        fps=30
):

    command = [
        "ffmpeg",
        "-framerate",
        str(fps),

        "-i",
        os.path.join(
            frames_folder,
            "frame_%08d.png"
        ),

        "-c:v",
        "libx264",

        "-preset",
        "slow",

        "-crf",
        "18",

        "-pix_fmt",
        "yuv420p",

        output_path
    ]


    run_ffmpeg(command)

    return output_path



def convert_60fps(
        input_video,
        output_video
):

    command = [
        "ffmpeg",
        "-i",
        input_video,

        "-vf",
        "minterpolate=fps=60:mi_mode=mci",

        "-c:a",
        "copy",

        output_video
    ]


    run_ffmpeg(command)

    return output_video
