import os
import cv2
import torch
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer


class RealESRGANUpscaler:

    def __init__(self, model_path="models/RealESRGAN_x4plus.pth", scale=4):
        self.scale = scale

        self.model = RRDBNet(
            num_in_ch=3,
            num_out_ch=3,
            num_feat=64,
            num_block=23,
            num_grow_ch=32,
            scale=4
        )

        self.upsampler = RealESRGANer(
            scale=4,
            model_path=model_path,
            model=self.model,
            tile=256,
            tile_pad=10,
            pre_pad=0,
            half=torch.cuda.is_available()
        )


    def upscale_image(self, input_path, output_path):

        img = cv2.imread(input_path)

        if img is None:
            raise Exception("Image load failed")


        output, _ = self.upsampler.enhance(
            img,
            outscale=self.scale
        )


        cv2.imwrite(
            output_path,
            output
        )


        return output_path



def upscale_video_frames(
        input_folder,
        output_folder
):

    os.makedirs(
        output_folder,
        exist_ok=True
    )

    upscaler = RealESRGANUpscaler()


    for file in os.listdir(input_folder):

        if file.lower().endswith(
            (".png",".jpg",".jpeg")
        ):

            src = os.path.join(
                input_folder,
                file
            )

            dst = os.path.join(
                output_folder,
                file
            )


            upscaler.upscale_image(
                src,
                dst
            )


    return output_folder



if __name__ == "__main__":

    print(
        "Open4K Real-ESRGAN Upscaler Ready"
    )
