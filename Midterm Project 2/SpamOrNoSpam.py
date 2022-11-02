import os
import random

# 0 is not spam and 1 is spam

spam_list = []
ham_list = []
ham_500 = []
spam_500 = []
word_count_ham = {}  # How many times a word appears in the non-spam emails in the training set
word_count_spam = {}  # How many times a word appears in the spam emails in the training set
probability_of_spam = {}  # The calculated values for the probability of a word being spam
probability_of_ham = {}  # The calculated values for the probability of a word being non-spam
final_word_probability = {}  # The final binary values that each word will have. Calculated using a Laplace Smooth.
testing_list = []


def select_emails():
    """Select 500 non-spam (ham) and 500 phishing emails (spam) randomly, then count the number of times each word
    appears. """
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

        # Combine the leftover spam emails with the leftover non-spam emails to create the testing set.
        testing_list.extend(spam_list)
        testing_list.extend(ham_list)

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


def calculate_probability():
    """Calculate the probability that a word is spam or not spam. Probability of a word being spam is calculated by
    using a Laplace Smooth, which accounts for words not seen inside the training set. """

    # For each word in the non-spam emails, divide the number of occurrences of the word by the total number of
    # non-spam emails in the training set (500 in this case).
    for key in word_count_ham.keys():
        calculated_probability = word_count_ham[key] / len(ham_500)
        probability_of_ham[key] = calculated_probability

    # For each word in the spam emails, divide the number of occurrences of the word by the total number of
    # spam emails in the training set (500 in this case).
    for key in word_count_spam.keys():
        calculated_probability = word_count_spam[key] / len(spam_500)
        probability_of_spam[key] = calculated_probability

    # Apply the Laplace Smooth to the probability of a word being spam. A value closer to 1 means a greater probability
    # of being spam. A value closer to 0 means a greater probability of being non-spam.
    for key in probability_of_spam.keys():
        if key in probability_of_ham:
            final_word_probability[key] = (probability_of_spam[key] + 1) / (
                        probability_of_spam[key] + probability_of_ham[key] + 2)
        else:
            final_word_probability[key] = (probability_of_spam[key] + 1) / (probability_of_spam[key] + 1)

    for key in probability_of_ham.keys():
        if key not in probability_of_spam:
            final_word_probability[key] = probability_of_ham[key] / (probability_of_ham[key] + 1)


def test_classifier():
    """Test the classifier on the 200 emails that were not used for training. Calculates the true positive rate,
    true negative rate, false positive rate, and false negative rate. Also calculates the accuracy of the classifier,
    the precision of the classifier, the recall of the classifier, and the F1 score of the classifier."""

    # Initialize the counters for the true positive, true negative, false positive, and false negative rates.
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    # For each email in the testing set, calculate the probability that the email is spam and the probability
    # that the email is not spam.
    for email in testing_list:
        spam_probability = 1
        ham_probability = 1
        for word in email.split():
            if word in final_word_probability:
                spam_probability *= final_word_probability[word]
                ham_probability *= (1 - final_word_probability[word])
            else:
                spam_probability *= (1 / (len(spam_500) + 1))
                ham_probability *= (1 / (len(ham_500) + 1))

        # If the probability that the email is spam is greater than the probability that the email is not spam,
        # the email is classified as spam. If the probability that the email is not spam is greater than the
        # probability that the email is spam, the email is classified as not spam.
        if spam_probability > ham_probability:
            if testing_list.index(email) < 100:
                true_positive += 1
            else:
                false_positive += 1
        else:
            if testing_list.index(email) < 100:
                false_negative += 1
            else:
                true_negative += 1

    # Calculate the true positive rate, true negative rate, false positive rate, and false negative rate.
    true_positive_rate = true_positive / (true_positive + false_negative)
    true_negative_rate = true_negative / (true_negative + false_positive)
    false_positive_rate = false_positive / (false_positive + true_negative)
    false_negative_rate = false_negative / (false_negative + true_positive)

    # Calculate the accuracy of the classifier.
    accuracy = (true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative)

    # Calculate the precision of the classifier.
    precision = true_positive / (true_positive + false_positive)

    # Calculate the recall of the classifier.
    recall = true_positive / (true_positive + false_negative)

    # Calculate the F1 score of the classifier.
    f1_score = (2 * precision * recall) / (precision + recall)

    # Print the results as percentages rounded to two decimals.
    print("True Positive Rate: {0:.2%}".format(true_positive_rate))
    print("True Negative Rate: {0:.2%}".format(true_negative_rate))
    print("False Positive Rate: {0:.2%}".format(false_positive_rate))
    print("False Negative Rate: {0:.2%}".format(false_negative_rate))
    print("Accuracy: {0:.2%}".format(accuracy))
    print("Precision: {0:.2%}".format(precision))
    print("Recall: {0:.2%}".format(recall))
    print("F1 Score: {0:.2%}".format(f1_score))



if __name__ == "__main__":
    select_emails()
    calculate_probability()
    test_classifier()
