#! /bin/sh
 
echo $1
#echo "hello"
lex=$1

#ls -la
tail -n +3 $lex/lexicon.txt > $lex/temp.txt
chmod 777 $lex/temp.txt
cut -d ' ' -f 2- -s $lex/temp.txt | gsed 's/ /\n/g' | sort -u > $lex/nonsilence_phones.txt
chmod 777 $lex/nonsilence_phones.txt

head -n 2 lexicon.txt > $lex/temp.txt
chmod 777 $lex/temp.txt
cut -d ' ' -f 2 $lex/temp.txt > $lex/silence_phones.txt
chmod 777 $lex/silence_phones.txt

echo 'SIL' > $lex/optional_silence.txt 
chmod 777 $lex/optional_silence.txt

rm temp.txt

exit 0