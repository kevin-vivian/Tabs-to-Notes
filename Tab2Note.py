import re
import string

NOTES_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def custom_make_translation(text, translation):
    regex = re.compile('|'.join(map(re.escape, translation)))
    return regex.sub(lambda match: translation[match.group(0)], text)


def parallel_fifths(notes_table):
    notes = [NOTES_SHARP.index(note) for note in notes_table.values()]
    fifths = [NOTES_SHARP[(int(note) + 7) % len(NOTES_SHARP)] for note in notes]
    return fifths

with open('cmajor.txt', 'r') as f:
    lines = f.readlines()
    output = []
    for line in lines:
        if line == '\n':
            output.append(line)
            continue
        string_name_idx = NOTES_SHARP.index(line[0][0].upper())  # string name always at beginning of line
        intervals = re.findall('\d+', line)  # find all numbers in tab

        # hash intervals with computed note values
        notes_table = {interval: NOTES_SHARP[(string_name_idx + int(interval)) % len(NOTES_SHARP)] for interval in intervals}
        if len(notes_table) > 0:
            translated = custom_make_translation(line, notes_table)
            output.append(translated)
        if len(notes_table) == 0:
            output.append(line)

        notes = notes_table.values()
        fifths = parallel_fifths(notes_table)

        print(f'{dict(zip(notes, fifths))}')
# print(''.join(s for s in output))
