import os
import random

# 0 is not spam and 1 is spam

spam_list = []
ham_list = []
ham_500 = []
spam_500 = []
word_count_ham = {}
word_count_spam = {}
word_is_spam = {}


def select_emails():
    """Select 500 non-spam (ham) and 500 phishing emails (spam) randomly"""
    # go through the ham list folder and select 500

    # we do a little bit of reading
    # puts all 600 emails in text format into a list
    try:
        for file in os.listdir('email data/Ham/300 good emails'):
            temp = 'email data/Ham/300 good emails/' + file
            f = open(temp, 'r')
            text = f.read()
            ham_list.append(text.strip())
        for file in os.listdir('email data/Ham/301-600 good ones'):
            temp = 'email data/Ham/300 good emails/' + file
            f = open(temp, 'r')
            text = f.read()
            ham_list.append(text.strip())
        # selecting 500 random emails no dupes
        for i in range(500):
            num = random.randint(0, len(ham_list) - 1)
            ham_500.append(ham_list.pop(num))

        # go through the spam list folder and select 500
        for file in os.listdir('email data/Spam'):
            temp = 'email data/Spam/' + file
            f = open(temp, 'r')
            text = f.read().strip()
            spam_list.append(text)

        # select the 500 spam emails, leaving 100 behind for testing
        for i in range(500):
            num = random.randint(0, len(spam_list) - 1)
            spam_500.append(spam_list.pop(num))

        test_list = ham_list + spam_list
        random.shuffle(test_list)

        # Count the number of times each word appears in the 500 emails for both the spam and non-spam emails
        for email in ham_500:
            for word in email.split():
                if word not in word_count_ham:
                    word_count_ham[word] = 1
                else:
                    word_count_ham[word] += 1

        for email in spam_500:
            for word in email.split():
                if word not in word_count_spam:
                    word_count_spam[word] = 1
                else:
                    word_count_spam[word] += 1
    except IOError:
        print('Could not open file')

def create_model():
    total = 0
    for key in word_count_spam.keys():
        total += word_count_spam[key]
    print(total)
    for key in word_count_spam.keys():
        word_count_spam[key] = word_count_spam[key] / total

    total = 0
    for key in word_count_ham.keys():
        total += word_count_ham[key]
    print(total)
    for key in word_count_ham.keys():
        word_count_ham[key] = word_count_ham[key] / total

    # Create a dict that contains the probability that a word is spam based on if the probability for being not spam is
    # greater than the probability for being spam


if __name__ == "__main__":
    select_emails()
    create_model()
