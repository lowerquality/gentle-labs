import subprocess

if __name__=="__main__":

    # gmm-latgen-faster$thread_string --max-active=$max_active --beam=$beam --lattice-beam=$lattice_beam \
    # --acoustic-scale=$acwt --allow-partial=true --word-symbol-table=$graphdir/words.txt $decode_extra_opts \
    # $model $graphdir/HCLG.fst "$feats" "ark:|gzip -c > $dir/lat.JOB.gz" "ark,t:$dir/words.JOB" "ark,t:$dir/alignments.JOB" || exit 1;
    cmd = ['gmm-latgen-faster',]
    process = subprocess.run(cmd, cwd = '/Users/shreya/Document/kaldi/src/gmmbin/', stdout=subprocess.PIPE)