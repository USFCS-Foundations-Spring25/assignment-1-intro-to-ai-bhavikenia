# import sys
# from string import punctuation

# def wordfreq(fname, stripPunc, toLower) :
#     wordDict = {}
#     with open(fname) as f:
#         ## let's just get all the words at once.
#         words = f.read().split()
#         for word in words :
#             if stripPunc :
#                 word = word.strip(punctuation)
#             if toLower :
#                 word = word.lower()
#             if word in wordDict :
#                 wordDict[word] += 1
#             else :
#                 wordDict[word] = 1
#     return wordDict

# if __name__== '__main__':
#     if len(sys.argv) < 2:
#         print("Usage: wc {--strip --convert --pfile=outfile} file")
#         sys.exit(-1)
#     fname = sys.argv[-1]
#     strip = '--strip' in sys.argv
#     convert = '--convert' in sys.argv
#     for r,d,f in os.walk(path) :
#         wd = wordfreq(fname, stripPunc=strip, toLower=convert)
#     pickled = False
#     for arg in sys.argv:
#         if arg.startswith('--pfile'):
#                 ofile = arg.split('=')[1]
#                 pickle.dump(wd, open(ofile, 'w'))
#                 pickled = True
#         if not pickled:
#             print(wd)




import sys
import argparse
import re
from string import punctuation

def wordfreq(fname, strip_punc=False, to_lower=False, nonwords=False, separator=None):
    """ Reads a file and counts word occurrences based on given options. """
    word_dict = {}

    try:
        with open(fname, encoding="utf-8") as f:
            text = f.read()

            # Use custom separators if provided
            if separator:
                words = re.split(f"[{re.escape(separator)}]+", text)
            else:
                words = text.split()

            for word in words:
                if strip_punc:
                    word = word.strip(punctuation)
                if to_lower:
                    word = word.lower()
                if nonwords and not word.isalpha():
                    continue  # Skip non-words

                word_dict[word] = word_dict.get(word, 0) + 1
    except Exception as e:
        print(f"Error reading file {fname}: {e}", file=sys.stderr)

    return word_dict

def main():
    parser = argparse.ArgumentParser(description="Word frequency counter")

    parser.add_argument("file", help="Text file to process")
    parser.add_argument("--strip", action="store_true", help="Strip punctuation from words")
    parser.add_argument("--convert", action="store_true", help="Convert words to lowercase")
    parser.add_argument("--nonwords", action="store_true", help="Exclude non-words (words with non-alphabetic characters)")
    parser.add_argument("--separator", type=str, help="Custom separator characters (e.g., ',.;')")

    args = parser.parse_args()

    word_count = wordfreq(
        args.file,
        strip_punc=args.strip,
        to_lower=args.convert,
        nonwords=args.nonwords,
        separator=args.separator
    )

    print(word_count)

if __name__ == "__main__":
    main()
