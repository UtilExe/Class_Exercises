# 1. Write a program that creates gramatically valid English sentences. Here, we consider a sentence to be gramatically correct when it follows the simple English grammar of the form: 
# Article Adjective Noun Verb. That is, even the sentence A insect fly. is, for the moment, considered correct.
import random
nouns = ['time', 'year', 'people', 'way', 'day', 'man', 'thing', 'woman', 'life', 'child', 'world', 'school', 'state', 'family', 'student', 'group', 'country', 'problem', 'hand', 'part', 'place', 'case', 'week', 'company', 'system', 'program', 'question', 'work', 'government', 'number', 'night', 'point', 'home', 'water', 'room', 'mother', 'area', 'money', 'story', 'fact', 'month', 'lot', 'right', 'study', 'book', 'eye', 'job', 'word', 'business', 'issue', 'side', 'kind', 'head', 'house', 'service', 'friend', 'father', 'power', 'hour', 'game', 'line', 'end', 'member', 'law', 'car', 'city', 'community', 'name', 'president', 'team', 'minute', 'idea', 'kid', 'body', 'information', 'back', 'parent', 'face', 'others', 'level', 'office', 'door', 'health', 'person', 'art', 'war', 'history', 'party', 'result', 'change', 'morning', 'reason', 'research', 'girl', 'guy', 'moment', 'air', 'teacher', 'force', 'education']
verbs = ['be', 'have', 'do', 'say', 'go', 'can', 'get', 'would', 'make', 'know', 'will', 'think', 'take', 'see', 'come', 'could', 'want', 'look', 'use', 'find', 'give', 'tell', 'work', 'may', 'should', 'call', 'try', 'ask', 'need', 'feel', 'become', 'leave', 'put', 'mean', 'keep', 'let', 'begin', 'seem', 'help', 'talk', 'turn', 'start', 'might', 'show', 'hear', 'play', 'run', 'move', 'like', 'live', 'believe', 'hold', 'bring', 'happen', 'must', 'write', 'provide', 'sit', 'stand', 'lose', 'pay', 'meet', 'include', 'continue', 'set', 'learn', 'change', 'lead', 'understand', 'watch', 'follow', 'stop', 'create', 'speak', 'read', 'allow', 'add', 'spend', 'grow', 'open', 'walk', 'win', 'offer', 'remember', 'love', 'consider', 'appear', 'buy', 'wait', 'serve', 'die', 'send', 'expect', 'build', 'stay', 'fall', 'cut', 'reach', 'kill', 'remain']
adjectives = ['other', 'new', 'good', 'high', 'old', 'great', 'big', 'American', 'small', 'large', 'national', 'young', 'different', 'black', 'long', 'little', 'important', 'political', 'bad', 'white', 'real', 'best', 'right', 'social', 'only', 'public', 'sure', 'low', 'early', 'able', 'human', 'local', 'late', 'hard', 'major', 'better', 'economic', 'strong', 'possible', 'whole', 'free', 'military', 'true', 'federal', 'international', 'full', 'special', 'easy', 'clear', 'recent', 'certain', 'personal', 'open', 'red', 'difficult', 'available', 'likely', 'short', 'single', 'medical', 'current', 'wrong', 'private', 'past', 'foreign', 'fine', 'common', 'poor', 'natural', 'significant', 'similar', 'hot', 'dead', 'central', 'happy', 'serious', 'ready', 'simple', 'left', 'physical', 'general', 'environmental', 'financial', 'blue', 'democratic', 'dark', 'various', 'entire', 'close', 'legal', 'religious', 'cold', 'final', 'main', 'green', 'nice', 'huge', 'popular', 'traditional', 'cultural']
articles = ['A', 'An']

def validator(noun):
    vocals = ['a', 'e', 'i', 'o', 'u']
    if (noun[0] in vocals) :
        article = 'An'
    else:
        article = 'A'
    return article;

def picker():
    noun = random.choice(nouns)
    verb = random.choice (verbs)
    adjective = random.choice(adjectives)
    article = validator(noun)
    return str(article + " " + noun + " " + verb + " " + adjective)

print(picker());

# 2. Extend the above program to generate all possible sentences with the given words.

nouns = ['time', 'year', 'elephant']
verbs = ['be', 'have', 'do']
adjectives = ['other', 'good', 'high']
articles = ['A', 'An']

def validator(nouns):
    vocals = ['a', 'e', 'i', 'o', 'u']
    if (nouns[0] in vocals) :
        article = 'An'
    else:
        article = 'A'
    return article;

def picker():
    return [str(validator(noun) + " " + noun + " " + verb + " " + adjective) for noun in nouns for verb in verbs for adjective in adjectives]

print(picker());