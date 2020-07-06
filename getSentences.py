import re
import io

def getSentences(inputFile, outputFile):
    # input = open(inputFile, "r")
    with io.open(inputFile,"r", encoding='utf-8') as text, io.open(outputFile, "w", encoding='utf-8') as output:
        # fullArray = [ line for line in text ]
        fullArray = []
        for line in text:
            if len(line.split()) > 3:
                fullArray.append(line)
        fullString = '' . join(fullArray) . replace('\n', '')
        # sentences = re.split(r'[.!?]', fullString)
        pattern = re.compile(r'([A-ZА-ЯЁ][^\.!?]*[\.!?])', re.M)
        sentences = pattern.findall(fullString)
        # sentences = [i[0].strip() for i in re.findall(r"((\W\w+){3,}(?=(\.|\!|\?)))", fullString)]
        # print(sentences)
        for item in sentences:
            # if len(item.split()) > 3:
            output.write("%s\n" % item)

getSentences('input.txt', 'output.txt')