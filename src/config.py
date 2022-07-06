import transformers # what is this package 

MAX_LEN = 512
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
DEVICE ="cuda"

BERT_PATH = '/datasets/bert_base_uncased/'
MODEL_PATH = "/datasets/bert_base_uncased/model.bin"
TRAINING_FILE = '../input/imdb.csv'
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BERT_PATH, do_lower_case=True)
