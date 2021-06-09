from Scales import *

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
        description=GuitarScale.description(),
        formatter_class=argparse.RawTextHelpFormatter)
    PARSER.add_argument('key', type=str, help='The key')
    PARSER.add_argument('scale', type=str, help='The scale')
    PARSER.add_argument('--chord', '-c', help='Display chord', action='store_true')
    PARSER.add_argument('--tuning', '-t', help='String tuning', default='EADGBE', type=str)
    ARGS = PARSER.parse_args()

    SCALE = GuitarScale(key=ARGS.key, scale=ARGS.scale, chord=ARGS.chord, tuning=ARGS.tuning)
    SCALE.construct_fretboard()
    print (SCALE.printable_fretboard())