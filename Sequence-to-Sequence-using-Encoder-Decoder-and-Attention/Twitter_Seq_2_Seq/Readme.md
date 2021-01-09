# Customer Support on Twitter dataset

The Customer Support on Twitter dataset is a large, modern corpus of tweets and replies to aid innovation in natural language understanding and conversational models, and for study of modern customer support practices and impact.

### Context
Natural language remains the densest encoding of human experience we have, and innovation in NLP has accelerated to power understanding of that data, but the datasets driving this innovation don't match the real language in use today. The Customer Support on Twitter dataset offers a large corpus of modern English (mostly) conversations between consumers and customer support agents on Twitter, and has three important advantages over other conversational text datasets:

- Focused - Consumers contact customer support to have a specific problem solved, and the manifold of problems to be discussed is relatively small, especially compared to unconstrained conversational datasets like the reddit Corpus.
- Natural - Consumers in this dataset come from a much broader segment than those in the Ubuntu Dialogue Corpus and have much more natural and recent use of typed text than the Cornell Movie Dialogs Corpus.
- Succinct - Twitter's brevity causes more natural responses from support agents (rather than scripted), and to-the-point descriptions of problems and solutions. Also, its convenient in allowing for a relatively low message limit size for recurrent nets.

### Inspiration
The size and breadth of this dataset inspires many interesting questions:

- Can we predict company responses? Given the bounded set of subjects handled by each company, the answer seems like yes!
- Do requests get stale? How quickly do the best companies respond, compared to the worst?
- Can we learn high quality dense embeddings or representations of similarity for topical clustering?
- How does tone affect the customer support conversation? Does saying sorry help?
- Can we help companies identify new problems, or ones most affecting their customers?

### Content
The dataset is a CSV, where each row is a tweet. The different columns are described below. Every conversation included has at least one request from a consumer and at least one response from a company. Which user IDs are company user IDs can be calculated using the inbound field.

- tweet_id - A unique, anonymized ID for the Tweet. Referenced by response_tweet_id and in_response_to_tweet_id.
- author_id - A unique, anonymized user ID. @s in the dataset have been replaced with their associated anonymized user ID.
- inbound - Whether the tweet is "inbound" to a company doing customer support on Twitter. This feature is useful when re-organizing data for training conversational models.
- created_at - Date and time when the tweet was sent.
- text - Tweet content. Sensitive information like phone numbers and email addresses are replaced with mask values like __email__.
- response_tweet_id - IDs of tweets that are responses to this tweet, comma-separated.
- in_response_to_tweet_id - ID of the tweet this tweet is in response to, if any.


# [Model1](Twitter_Dataset_Learning_Phrase_Representation_RNN_Encoder_Decoder.ipynb)

Model Architecture

    Seq2Seq(
      (encoder): Encoder(
        (embedding): Embedding(2197, 256)
        (rnn): GRU(256, 512)
        (dropout): Dropout(p=0.5, inplace=False)
      )
      (decoder): Decoder(
        (embedding): Embedding(1504, 256)
        (rnn): GRU(768, 512)
        (fc_out): Linear(in_features=1280, out_features=1504, bias=True)
        (dropout): Dropout(p=0.5, inplace=False)
      )
    )

Training Log

      Epoch: 01 | Time: 0m 47s
        Train Loss: 3.955 | Train PPL:  52.205
         Val. Loss: 5.698 |  Val. PPL: 298.182
      Epoch: 02 | Time: 0m 48s
        Train Loss: 2.758 | Train PPL:  15.760
         Val. Loss: 6.608 |  Val. PPL: 740.750
      Epoch: 03 | Time: 0m 48s
        Train Loss: 2.382 | Train PPL:  10.823
         Val. Loss: 6.111 |  Val. PPL: 450.728
      Epoch: 04 | Time: 0m 47s
        Train Loss: 2.187 | Train PPL:   8.913
         Val. Loss: 6.364 |  Val. PPL: 580.653
      Epoch: 05 | Time: 0m 47s
        Train Loss: 2.068 | Train PPL:   7.910
         Val. Loss: 6.442 |  Val. PPL: 627.627
      Epoch: 06 | Time: 0m 47s
        Train Loss: 1.973 | Train PPL:   7.194
         Val. Loss: 6.419 |  Val. PPL: 613.365
      Epoch: 07 | Time: 0m 47s
        Train Loss: 1.851 | Train PPL:   6.363
         Val. Loss: 6.485 |  Val. PPL: 654.920
      Epoch: 08 | Time: 0m 47s
        Train Loss: 1.814 | Train PPL:   6.133
         Val. Loss: 6.408 |  Val. PPL: 606.482
      Epoch: 09 | Time: 0m 46s
        Train Loss: 1.744 | Train PPL:   5.719
         Val. Loss: 6.340 |  Val. PPL: 566.702
      Epoch: 10 | Time: 0m 47s
        Train Loss: 1.674 | Train PPL:   5.335
         Val. Loss: 6.614 |  Val. PPL: 745.656

Test Loss

      | Test Loss: 5.705 | Test PPL: 300.268 |
       
    
# [Model2](Twitter_Dataset_Sequence_to_Sequence_using_Attention.ipynb)

Model Architecture

    Seq2Seq(
      (encoder): Encoder(
        (embedding): Embedding(2197, 256)
        (rnn): GRU(256, 512, bidirectional=True)
        (fc): Linear(in_features=1024, out_features=512, bias=True)
        (dropout): Dropout(p=0.5, inplace=False)
      )
      (decoder): Decoder(
        (attention): Attention(
          (attn): Linear(in_features=1536, out_features=512, bias=True)
          (v): Linear(in_features=512, out_features=1, bias=False)
        )
        (embedding): Embedding(1504, 256)
        (rnn): GRU(1280, 512)
        (fc_out): Linear(in_features=1792, out_features=1504, bias=True)
        (dropout): Dropout(p=0.5, inplace=False)
      )
    )

Training Log

    Epoch: 01 | Time: 2m 34s
      Train Loss: 3.819 | Train PPL:  45.540
       Val. Loss: 5.468 |  Val. PPL: 236.961
    Epoch: 02 | Time: 2m 37s
      Train Loss: 2.575 | Train PPL:  13.137
       Val. Loss: 6.027 |  Val. PPL: 414.540
    Epoch: 03 | Time: 2m 38s
      Train Loss: 2.252 | Train PPL:   9.506
       Val. Loss: 5.949 |  Val. PPL: 383.506
    Epoch: 04 | Time: 2m 37s
      Train Loss: 2.084 | Train PPL:   8.033
       Val. Loss: 6.242 |  Val. PPL: 513.786
    Epoch: 05 | Time: 2m 36s
      Train Loss: 1.980 | Train PPL:   7.245
       Val. Loss: 6.282 |  Val. PPL: 534.947
    Epoch: 06 | Time: 2m 37s
      Train Loss: 1.903 | Train PPL:   6.709
       Val. Loss: 6.288 |  Val. PPL: 538.064
    Epoch: 07 | Time: 2m 38s
      Train Loss: 1.787 | Train PPL:   5.973
       Val. Loss: 6.315 |  Val. PPL: 553.067
    Epoch: 08 | Time: 2m 36s
      Train Loss: 1.756 | Train PPL:   5.789
       Val. Loss: 6.325 |  Val. PPL: 558.127
    Epoch: 09 | Time: 2m 36s
      Train Loss: 1.679 | Train PPL:   5.359
       Val. Loss: 6.307 |  Val. PPL: 548.256
    Epoch: 10 | Time: 2m 37s
      Train Loss: 1.604 | Train PPL:   4.973
     Val. Loss: 6.523 |  Val. PPL: 680.533

Test Loss

     | Test Loss: 5.508 | Test PPL: 246.537 |
