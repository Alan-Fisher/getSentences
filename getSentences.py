import re
import io

def getSentences(inputFile, outputFile):
    with io.open(inputFile, "r", encoding='utf-8') as input, io.open(outputFile, "w", encoding='utf-8') as output:
        fullArray = []
        for line in input:
            if len(line.split()) > 4:
                fullArray.append(line)
        fullString = '' . join(fullArray) . replace('\n', '') . replace(':— ', '.\n')
        pattern = re.compile(r'([A-ZА-ЯЁ][^\.!?…]*[\.!?…])', re.M)
        sentences = pattern.findall(fullString)
        for item in sentences:
            if len(item.split()) > 3:
                item = re.sub(r'\[[0-9]+\]', '', item)
                item = item.replace('…', '.')
                output.write("%s\n" % item)

getSentences('input.txt', 'output.txt')