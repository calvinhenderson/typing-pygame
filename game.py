from random import randint
import sys

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame  # noqa

# Average word size for computing WPM
WPM_AVG_CHARS = 4
# Default test length
WORD_COUNT = 25
FONT_SIZE = 72

CHARS = (
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    'abcdefghijklmnopqrstuvwxyz'
    '1234567890!@#$%^&*()-=_+[]{}\\|;:\'",.<>/?'
)

WORDS = [
    'the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that', 'he',
    'was', 'for', 'on', 'are', 'with', 'as', 'I', 'his', 'they', 'be', 'at',
    'one', 'have', 'this', 'from', 'or', 'had', 'by', 'not', 'word', 'but',
    'what', 'some', 'we', 'can', 'out', 'other', 'were', 'all', 'there',
    'when', 'up', 'use', 'your', 'how', 'said', 'an', 'each', 'she', 'which',
    'do', 'their', 'time', 'if', 'will', 'way', 'about', 'many', 'then',
    'them', 'write', 'would', 'like', 'so', 'these', 'her', 'long', 'make',
    'thing', 'see', 'him', 'two', 'has', 'look', 'more', 'day', 'could', 'go',
    'come', 'did', 'number', 'sound', 'no', 'most', 'people', 'my', 'over',
    'know', 'water', 'than', 'call', 'first', 'who', 'may', 'down', 'side',
    'been', 'now', 'find', 'any', 'new', 'work', 'part', 'take', 'get',
    'place', 'made', 'live', 'where', 'after', 'back', 'little', 'only',
    'round', 'man', 'year', 'came', 'show', 'every', 'good', 'me', 'give',
    'our', 'under', 'name', 'very', 'through', 'just', 'form', 'sentence',
    'great', 'think', 'say', 'help', 'low', 'line', 'differ', 'turn', 'cause',
    'much', 'mean', 'before', 'move', 'right', 'boy', 'old', 'too', 'same',
    'tell', 'does', 'set', 'three', 'want', 'air', 'well', 'also', 'play',
    'small', 'end', 'put', 'home', 'read', 'hand', 'port', 'large', 'spell',
    'add', 'even', 'land', 'here', 'must', 'big', 'high', 'such', 'follow',
    'act', 'why', 'ask', 'men', 'change', 'went', 'light', 'kind', 'off',
    'need', 'house', 'picture', 'try', 'us', 'again', 'animal', 'point',
    'mother', 'world', 'near', 'build', 'self', 'earth', 'father', 'head',
    'stand', 'own', 'page', 'should', 'country', 'found', 'answer', 'school',
    'grow', 'study', 'still', 'learn', 'plant', 'cover', 'food', 'sun', 'four',
    'between', 'state', 'keep', 'eye', 'never', 'last', 'let', 'thought',
    'city', 'tree', 'cross', 'farm', 'hard', 'start', 'might', 'story', 'saw',
    'far', 'sea', 'draw', 'left', 'late', 'run', 'don\'t', 'while', 'press',
    'close', 'night', 'real', 'life', 'few', 'north', 'open', 'seem',
    'together', 'next', 'white', 'children', 'begin', 'got', 'walk', 'example',
    'ease', 'paper', 'group', 'always', 'music', 'those', 'both', 'mark',
    'often', 'letter', 'until', 'mile', 'river', 'car', 'feet', 'care',
    'second', 'book', 'carry', 'took', 'science', 'eat', 'room', 'friend',
    'began', 'idea', 'fish', 'mountain', 'stop', 'once', 'base', 'hear',
    'horse', 'cut', 'sure', 'watch', 'color', 'face', 'wood', 'main', 'enough',
    'plain', 'girl', 'usual', 'young', 'ready', 'above', 'ever', 'red', 'list',
    'though', 'feel', 'talk', 'bird', 'soon', 'body', 'dog', 'family',
    'direct', 'pose', 'leave', 'song', 'measure', 'door', 'product', 'black',
    'short', 'numeral', 'class', 'wind', 'question', 'happen', 'complete',
    'ship', 'area', 'half', 'rock', 'order', 'fire', 'south', 'problem',
    'piece', 'told', 'knew', 'pass', 'since', 'top', 'whole', 'king',
    'space', 'heard', 'best', 'hour', 'better', 'true', 'during', 'hundred',
    'five', 'remember', 'step', 'early', 'hold', 'west', 'ground', 'interest',
    'reach', 'fast', 'verb', 'sing', 'listen', 'six', 'table', 'travel',
    'less', 'morning', 'ten', 'simple', 'several', 'vowel', 'toward', 'war',
    'lay', 'against', 'pattern', 'slow', 'center', 'love', 'person', 'money',
    'serve', 'appear', 'road', 'map', 'rain', 'rule', 'govern', 'pull',
    'cold', 'notice', 'voice', 'unit', 'power', 'town', 'fine', 'certain',
    'fly', 'fall', 'lead', 'cry', 'dark', 'machine', 'note', 'wait',
    'plan', 'figure', 'star', 'box', 'noun', 'field', 'rest', 'correct',
    'able', 'pound', 'done', 'beauty', 'drive', 'stood', 'contain', 'front',
    'teach', 'week', 'final', 'gave', 'green', 'oh', 'quick', 'develop',
    'ocean', 'warm', 'free', 'minute', 'strong', 'special', 'mind', 'behind',
    'clear', 'tail', 'produce', 'fact', 'street', 'inch', 'multiply',
    'course', 'stay', 'wheel', 'full', 'force', 'blue', 'object', 'decide',
    'surface', 'deep', 'moon', 'island', 'foot', 'system', 'busy', 'test',
    'record', 'boat', 'common', 'gold', 'possible', 'plane', 'stead', 'dry',
    'wonder', 'laugh', 'thousand', 'ago', 'ran', 'check', 'game', 'shape',
    'equate', 'hot', 'miss', 'brought', 'heat', 'snow', 'tire', 'bring',
    'yes', 'distant', 'fill', 'east', 'paint', 'language', 'among', 'grand',
    'ball', 'yet', 'wave', 'drop', 'heart', 'am', 'present', 'heavy',
    'dance', 'engine', 'position', 'arm', 'wide', 'sail', 'material', 'size',
    'vary', 'settle', 'speak', 'weight', 'general', 'ice', 'matter', 'circle',
    'pair', 'include', 'divide', 'syllable', 'felt', 'perhaps', 'pick',
    'count', 'square', 'reason', 'length', 'represent', 'art', 'subject',
    'energy', 'hunt', 'probable', 'bed', 'brother', 'egg', 'ride', 'cell',
    'believe', 'fraction', 'forest', 'sit', 'race', 'window', 'store',
    'train', 'sleep', 'prove', 'lone', 'leg', 'exercise', 'wall', 'catch',
    'mount', 'wish', 'sky', 'board', 'joy', 'winter', 'sat', 'written',
    'wild', 'instrument', 'kept', 'glass', 'grass', 'cow', 'job', 'edge',
    'sign', 'visit', 'past', 'soft', 'fun', 'bright', 'gas', 'weather',
    'month', 'million', 'bear', 'finish', 'happy', 'hope', 'flower', 'clothe',
    'sudden', 'nothing', 'region', 'summer', 'strange', 'gone', 'jump', 'baby',
    'eight', 'village', 'meet', 'root', 'buy', 'raise', 'solve', 'metal',
    'whether', 'push', 'seven', 'paragraph', 'third', 'shall', 'held', 'hair',
    'describe', 'cook', 'floor', 'either', 'result', 'burn', 'hill', 'safe',
    'cat', 'century', 'consider', 'type', 'law', 'bit', 'coast', 'copy',
    'phrase', 'silent', 'tall', 'sand', 'soil', 'roll', 'temperature',
    'industry', 'value', 'fight', 'lie', 'beat', 'excite', 'natural', 'view',
    'sense', 'ear', 'else', 'quite', 'broke', 'case', 'middle', 'kill',
    'son', 'lake', 'moment', 'scale', 'loud', 'spring', 'observe', 'child',
    'straight', 'consonant', 'nation', 'dictionary', 'milk', 'speed', 'method',
    'pay', 'age', 'section', 'dress', 'cloud', 'surprise', 'quiet', 'stone',
    'tiny', 'climb', 'cool', 'design', 'poor', 'lot', 'experiment', 'bottom',
    'key', 'iron', 'single', 'stick', 'flat', 'twenty', 'skin', 'smile',
    'crease', 'hole', 'trade', 'melody', 'trip', 'office', 'receive', 'row',
    'mouth', 'exact', 'symbol', 'die', 'least', 'trouble', 'shout', 'except',
    'wrote', 'seed', 'tone', 'join', 'suggest', 'clean', 'break', 'lady',
    'yard', 'rise', 'bad', 'blow', 'oil', 'blood', 'touch', 'grew', 'captain',
    'cent', 'mix', 'team', 'wire', 'cost', 'lost', 'brown', 'wear', 'whose',
    'garden', 'equal', 'sent', 'choose', 'fell', 'fit', 'flow', 'fair',
    'bank', 'collect', 'save', 'control', 'decimal', 'gentle', 'woman',
    'practice', 'separate', 'difficult', 'doctor', 'please', 'protect', 'noon',
    'locate', 'finger', 'organ', 'ring', 'character', 'insect', 'caught',
    'period', 'indicate', 'radio', 'spoke', 'atom', 'human', 'history',
    'electric', 'expect', 'crop', 'modern', 'element', 'hit', 'student',
    'party', 'supply', 'bone', 'rail', 'imagine', 'provide', 'agree', 'thus',
    'capital', 'won\'t', 'chair', 'danger', 'fruit', 'rich', 'thick',
    'process', 'operate', 'guess', 'necessary', 'sharp', 'wing', 'create',
    'wash', 'bat', 'rather', 'crowd', 'corn', 'compare', 'poem', 'string',
    'bell', 'depend', 'meat', 'rub', 'tube', 'famous', 'dollar', 'stream',
    'fear', 'sight', 'thin', 'triangle', 'planet', 'hurry', 'chief', 'colony',
    'clock', 'mine', 'tie', 'enter', 'major', 'fresh', 'search', 'send',
    'yellow', 'gun', 'allow', 'print', 'dead', 'spot', 'desert', 'suit',
    'current', 'lift', 'rose', 'continue', 'block', 'chart', 'hat', 'sell',
    'success', 'company', 'subtract', 'event', 'particular', 'deal', 'swim',
    'opposite', 'wife', 'shoe', 'shoulder', 'spread', 'arrange', 'camp',
    'cotton', 'born', 'determine', 'quart', 'nine', 'truck', 'noise', 'effect',
    'chance', 'gather', 'shop', 'stretch', 'throw', 'shine', 'property',
    'molecule', 'select', 'wrong', 'gray', 'repeat', 'require', 'broad',
    'salt', 'nose', 'plural', 'anger', 'claim', 'continent', 'oxygen', 'sugar',
    'death', 'pretty', 'skill', 'women', 'season', 'solution', 'magnet',
    'thank', 'branch', 'match', 'suffix', 'especially', 'fig', 'afraid',
    'sister', 'steel', 'discuss', 'forward', 'similar', 'guide', 'experience',
    'apple', 'bought', 'led', 'pitch', 'coat', 'mass', 'card', 'band',
    'rope', 'slip', 'win', 'dream', 'evening', 'condition', 'feed', 'tool',
    'total', 'basic', 'smell', 'valley', 'nor', 'double', 'seat', 'arrive',
    'master', 'track', 'parent', 'shore', 'division', 'sheet', 'substance',
    'connect', 'post', 'spend', 'chord', 'fat', 'glad', 'original', 'share',
    'station', 'dad', 'bread', 'charge', 'proper', 'bar', 'offer', 'segment',
    'slave', 'duck', 'instant', 'market', 'degree', 'populate', 'chick',
    'dear', 'enemy', 'reply', 'drink', 'occur', 'support', 'speech', 'nature',
    'range', 'steam', 'motion', 'path', 'liquid', 'log', 'meant', 'quotient',
    'teeth', 'shell', 'neck', 'favor', 'score', 'huge', 'silver', 'prepare',
    'column', 'level', 'invent', 'term', 'neighbor', 'soldier', 'corner',
]


class Game:
    def __init__(self, test_type='words', words=WORD_COUNT, width=800, height=360):
        # Initialize pygame modules
        pygame.init()
        pygame.display.set_caption('Word Racer')
        pygame.font.init()
        pygame.key.start_text_input()

        self.font = pygame.font.Font("monospace.ttf", FONT_SIZE)
        self.menu_ft = pygame.font.Font("monospace.ttf", 24)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.wpm = 0
        self.cps = 0

        self.typed_words = 0
        self.typed = 0
        self.errors = 0
        self.index = 0
        self.started = 0
        self.stopped = 0
        self.end_txt = self.menu_ft.render(
            'Press any key to exit', True, 'green')

        if test_type == 'ascii':
            self.keys = ' '.join([self._get_key() for _ in range(words)])
        elif test_type == 'word':
            self.keys = ' '.join([self._get_word() for _ in range(words)])
        else:
            raise ValueError('invalid test type. must be one of: word, ascii')

    def is_running(self) -> bool:
        return self.running

    def tick(self):
        e = pygame.event.poll()
        if e:
            if e.type == pygame.QUIT:
                self.running = False
                return
            elif e.type == pygame.KEYDOWN and self.typed == len(self.keys):
                self.running = False
                return
            elif e.type != pygame.TEXTINPUT:
                return

            if self.started == 1:
                self.started = pygame.time.get_ticks()

            if e.text == self.keys[self.index]:
                self._next_key()
            else:
                self.errors = self.errors + 1

        self._render()
        self.clock.tick(60)

    def _render(self):
        self.screen.fill("black")
        lh = self.font.render(''.join(self.keys[0:self.index]), True, 'gray')
        c = self.font.render(
            ''.join(self.keys[self.index:self.index+1]), True, 'black', 'gray')
        rh = self.font.render(''.join(self.keys[self.index+1:]), True, 'gray')
        acc = (1 - self.errors/max(1, (self.typed + self.errors))) * 100
        cx = self.width / 2
        cw = c.get_width()/2
        lw = lh.get_width()+cw

        y = self.height / 3 - self.font.get_height()/2
        self.screen.blit(lh, (cx - lw - 5, y))
        self.screen.blit(c, (cx - cw, y))
        self.screen.blit(rh, (cx + cw + 5, y))

        if self.wpm > 0:
            wpm = self.menu_ft.render('WPM: {}, ACC: {}%'.format(
                int(self.wpm + 0.5), int(acc)), True, 'gray')
            y = self.height - wpm.get_height() - 5
            self.screen.blit(wpm, (0, y))
        else:
            cps = self.menu_ft.render('CPS: {}, ACC: {}%'.format(
                round(self.cps, 2), int(acc)), True, 'gray')
            y = self.height - cps.get_height() - 5
            self.screen.blit(cps, (0, y))

        st = self.menu_ft.render('typed: {}, errors: {}, total: {}'.format(
            self.typed, self.errors, self.typed + self.errors), True, 'gray')

        x = self.width - st.get_width()
        y = self.height - st.get_height() - 5
        self.screen.blit(st, (x, y))

        if self.typed == len(self.keys):
            x = self.width / 2 - self.end_txt.get_width() / 2
            y = self.height/2 + self.end_txt.get_height()/2
            self.screen.blit(self.end_txt, (x, y))

        pygame.display.flip()

    def _next_key(self):
        if self.keys[self.index] == ' ':
            self.typed_words += 1

        self.index += 1
        self.typed += 1

        if self.typed > 0:
            self.wpm = self.typed / WPM_AVG_CHARS / \
                ((pygame.time.get_ticks() - self.started) / 1000 / 60)

        if self.index == len(self.keys):
            self.stopped = pygame.time.get_ticks()

    def _get_key(self):
        # returns one key from the ASCII table
        return CHARS[randint(0, len(CHARS)-1)]

    def _get_word(self):
        # returns one word from the words list
        return WORDS[randint(0, len(WORDS)-1)]


if __name__ == '__main__':
    game = None

    if len(sys.argv) < 2:
        print('game.py - A typing game to practice your typing speed\r\n'
              '\r\nUSAGE\r\n'
              '\tpython game.py test_type length\r\n'
              '\r\nCOMMAND LINE ARGUMENTS\r\n'
              '\ttest_type\tOne of: word, ascii\r\n'
              '\tlength\t\tnumber, the length of the test\r\n')
        sys.exit(1)

    test_type = sys.argv[1]
    length = int(sys.argv[2]) if len(sys.argv) == 3 else WORD_COUNT

    game = Game(test_type, length)

    while game.is_running():
        game.tick()
