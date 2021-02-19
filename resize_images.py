import os
import glob
import cv2

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Resize raw images to uniformed target size (images are automatically labeled as integers)."
    )
    parser.add_argument(
        "--i",
        help="Directory path to raw images.",
        default="data/raw",
        type=str,
    )
    parser.add_argument(
        "--o",
        help="Directory path to save preprocessed images.",
        default="data/VOC2007/JPEGImages/",
        type=str,
    )
    # parser.add_argument(
    #     "--e", help="Raw image files extension to preprocess.", default="jpg", type=str
    # )
    # parser.add_argument(
    #     "--r",
    #     help="Resize the image (True) or not (False).",
    #     default=False,
    #     type=bool
    # )
    parser.add_argument(
        "--s",
        help="Target size to resize as a tuple of 2 integers.",
        default="(800, 600)",
        type=str,
    )
    # parser.add_argument(
    #     "--c",
    #     help="Change image name (True) or not (False).",
    #     default=True,
    #     type=bool
    # )
    args = parser.parse_args()

    raw_dir = args.i
    save_dir = args.o
    #ext = args.e
    target_size = eval(args.s)
    msg = "--target-size must be a tuple of 2 integers"
    assert isinstance(target_size, tuple) and len(target_size) == 2, msg
    #fnames = glob.glob(os.path.join(raw_dir, "*.{}".format(ext)))
    fnames = glob.glob(os.path.join(raw_dir, "*.png"))#glob.glob(os.path.join(raw_dir, "*.jpg")) + glob.glob(os.path.join(raw_dir, "*.png"))
    idx = 0
    if(os.path.exists(save_dir) is False):
        os.makedirs(save_dir)
    else:
        idx = len(glob.glob(os.path.join(save_dir, "*.jpg")) + glob.glob(os.path.join(save_dir, "*.png")))
    print(
        "{} files to resize from directory '{}' to target size: {}".format(
            len(fnames), raw_dir, target_size
        )
    )
    for i, fname in enumerate(fnames):
        print(".", end="", flush=True)
        img = cv2.imread(fname)
        img_small = cv2.resize(img, target_size)
        new_fname = "{}.{}".format(str(i + idx), fname[-3:])
        small_fname = os.path.join(save_dir, new_fname)
        cv2.imwrite(small_fname, img_small)
    print(
        "\nDone resizing {} files.\nSaved to directory: `{}`".format(
            len(fnames), save_dir
        )
    )
