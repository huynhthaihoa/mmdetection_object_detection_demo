import os
import glob
import argparse
import ntpath
from shutil import copyfile

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Change image & annotation file names."
    )
    parser.add_argument(
        "--ii",
        help="Directory path to raw images.",
        default="//192.168.0.199/ubay_share/OCR Survey Document/JPEGImages",
        type=str,
    )
    parser.add_argument(
        "--ia",
        help="Directory path to raw annotations.",
        default="//192.168.0.199/ubay_share/OCR Survey Document/Annotations",
        type=str,
    )
    parser.add_argument(
        "--oi",
        help="Directory path to save name-changed images.",
        default="data/VOC2007/JPEGImages/",
        type=str,
    )
    parser.add_argument(
        "--oa",
        help="Directory path to save name-changed annotations.",
        default="data/VOC2007/Annotations/",
        type=str,
    )

    args = parser.parse_args()
    raw_imgs = args.ii 
    raw_anns = args.ia 
    des_imgs = args.oi 
    des_anns = args.oa
    fnames = glob.glob(os.path.join(raw_imgs, "*.jpg")) + glob.glob(os.path.join(raw_imgs, "*.png"))
    idx = 0
    if(os.path.exists(des_imgs) is False):
        os.makedirs(des_imgs)
    else:
        idx = len(glob.glob(os.path.join(des_imgs, "*.jpg")) + glob.glob(os.path.join(des_imgs, "*.png")))
    print(
        "{} images to copy from directory '{}' to directory '{}'".format(
            len(fnames), raw_imgs, des_imgs)
        )
    for i, fname in enumerate(fnames):
        print(".", end="", flush=True)
        basename = ntpath.basename(fname)
        #basename = os.path.splitext(ntpath.basename(fname))[0]#os.path.basename(fname)
        name = os.path.splitext(basename)[0]
        ext = os.path.splitext(basename)[1]
        src_ann = raw_anns + '/' + name + '.xml'
        dst_ann = des_anns + '/' + str(i + idx) + '.xml'
        dst_img = des_imgs + '/' + str(i + idx) + ext
        copyfile(fname, dst_img)
        try:
            copyfile(src_ann, dst_ann)
        except:
            print("Cannot copy annotation. It is possibly because the annotation '{}' does not exist".format(src_ann))
        #copyfile(src, dst)
    print(
        "\nDone copying {} files.\nSaved images to directory '{}' and annotations to directory '{}'".format(
            len(fnames), des_imgs, des_anns
        )
    )