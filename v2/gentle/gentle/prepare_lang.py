import sys
import os
import shutil
import subprocess


def create_fst(kaldi_path, proto_dir):

    phone_path = proto_dir + "/langdir/phones"
    lang_path = proto_dir + "/langdir"
    # if os.path.exists(phone_path):
    #     shutil.rmtree(phone_path)
    # os.makedirs(phone_path)

    # validate_dict_dir
    # this call expects that all the language, dictionary, input, steps and utils will reside in 'gentle'
    # 'gentle' will reside in kaldi/egs as a recipe
    # cmd = ["./utils/validate_dict_dir.pl", proto_dir + "/dict"]
    # validate_dict = subprocess.check_call(
    #     cmd, cwd=kaldi_path + "/egs/gentle", stdout=subprocess.PIPE
    # )
    cmd = [
        "./utils/prepare_lang.sh",
        proto_dir + "/dict",
        "<UNK>",
        proto_dir + "/lang_test",
        proto_dir + "/langdir",
    ]
    prepare_lang = subprocess.check_call(
        cmd, cwd=kaldi_path + "/egs/gentle", stdout=subprocess.PIPE
    )

    if prepare_lang == 0:  # exit status zero means it succeeded in making lang files
        # if lang files are generated successfully,
        # then copy proto_dir/langdir/words.txt to
        # proto_dir/tdnn../graph../
        print("lang files prepared successfully!")
        src = proto_dir + "/langdir"
        dst = proto_dir + "/tdnn_7b_chain_online/graph_pp"
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):  # copies all directories in langdir
                if os.path.isdir(d):
                    print("** ", d)
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy(s, d)  # copies all files in langdir/
        # shutil.copytree(
        #     proto_dir + "/langdir", "
        # )


if __name__ == "__main__":
    # sys.argv[1]: path to pristine copy of KALDI_ROOT where src and tools have been pre-compiled
    # sys.argv[2]: proto_dir ex: data/ where data/langdir, data/dict, data/tdnn_7b_chain_online/graph_pp
    create_fst(sys.argv[1], sys.argv[2])
