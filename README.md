# Amazon Sentiment Classification Summary

## Problem description

In today's world, online reviews and feedback are vital for businesses to understand their customers' sentiments towards their products and services. Analyzing these sentiments can help businesses make informed decisions, such as improving their products and services, enhancing customer experience, and targeting specific customer segments. The goal of this sentiment analysis and classification project is to develop a machine learning model that can accurately identify and classify the sentiment of customer reviews. The model will be trained on a dataset of customer reviews, which will be labeled as either positive, negative, or neutral.

The dataset consist of of reviews of fine foods from amazon. The data span a period of more than 10 years, including all ~500,000 reviews. Reviews include product and user information, ratings, and a plaintext review. There is also reviews from all other Amazon categories.

The model will need to be able to accurately analyze the text of the review and classify it as either positive, negative, or neutral.

The project will involve several key steps, including data preprocessing, feature extraction, model selection, and evaluation. The data preprocessing step will involve cleaning and transforming the raw data to make it suitable for analysis. The feature extraction step will involve selecting and extracting the relevant features from the preprocessed data. The model selection step will involve selecting an appropriate machine learning algorithm to train the sentiment analysis model. Finally, the evaluation step will involve testing the model's performance on a separate dataset to determine its accuracy and effectiveness.

Overall, the success of this sentiment analysis project will depend on the accuracy of the machine learning model and its ability to correctly identify and classify customer sentiment in real-world scenarios.


## Final deployed project

The objective of the deployment was to classify all of those reviews that were set in a middle point. For example in a score review of 5 stars where 1 star is the worst and 5 stars the best, usually 3 stars stands in the middle and we can not determine if it was a review going more towards the positive side (4 or 5 Stars) or a review going more towards the negative side (2 & 1 Stars). The NLP model was built to classify these reviews and have a clear direction of what, why and when products are bought in the website.

You can test and use the model totally deployed [here](https://liamarguedas-data-data-scienceamazon-fine-foodapp-t5zed6.streamlit.app/).

### Model performing in a 5 star review

![Positive Sentiment](https://raw.githubusercontent.com/liamarguedas/amazon-fine-food/main/Summary-Charts/Positive-Sentiment.gif)

### Model performing in a 1 star review

![Negative Sentiment](https://raw.githubusercontent.com/liamarguedas/amazon-fine-food/main/Summary-Charts/Negative-Sentiment.gif)

5 and 1 Star reviews are usually easy to classify, the challenge was to classify those 3 Star reviews into positive, negative or a misture of both (Labeled as Neutral).

### Model performing in a 3 star (Sentiment Detected) review

![Sentiment Detected](https://raw.githubusercontent.com/liamarguedas/amazon-fine-food/main/Summary-Charts/MiddleSentimentDetected.gif)

### Model performing in a 3 star (Neutral Sentiment) review

![Neutral Sentiment](https://raw.githubusercontent.com/liamarguedas/amazon-fine-food/main/Summary-Charts/MiddleSentiment.gif)

As seen the model perfoms really well, it is easy to implement and it can classify sentiment in entire datasets with only one function. 

## Did it solve the Amazon problem?
From the test and deployment we saw a pretty amazing performance of the pre-trained model, so that I can say safetly that I managed to solve the sentiment classification problem from the food reviews.

## Project Final Thoughts
By analyzing the sentiment of customer reviews for a particular product or service, I have gained valuable insights into how customers feel about it. This information can be used to make data-driven decisions about how to improve the product or service and provide a better customer experience.

This project involved several important steps, including data preprocessing, choosing a suitable sentiment analysis method, training and evaluating the model, and interpreting the results. By following these steps, I was able to develop a robust sentiment analysis system that accurately predicts the sentiment of customer reviews.

It's important to note that sentiment analysis is a constantly evolving field, and there are always new methods and techniques being developed. As anyone reading this notebook continue to work on projects like this, be sure to stay up-to-date with the latest research and techniques, and continue to refine your skills.

Overall, this sentiment analysis project was a valuable learning experience, and it has provided me with the skills and knowledge to apply sentiment analysis techniques to a wide range of applications.
