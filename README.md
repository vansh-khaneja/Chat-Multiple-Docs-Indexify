# Chat-Multiple-Docs-Indexify
This repository contains a chatbot application capable of answering questions from multiple PDF files simultaneously. The application leverages Indexify for document indexing and retrieval, DSPy for natural language processing, and Streamlit for the user interface.

Read full article with detailed steps over here [test](test)

![Alt Text - description of the image](https://github.com/vansh-khaneja/Chat-Multiple-Docs-Indexify/blob/main/sample%20outputs/output1.png?raw=true)

## Getting Started
Follow these steps to set up and run the application.

## Prerequisites
Ensure you have Python installed on your system. You can download it from here.

## Installation
1) Clone the repository:
   
```git clone https://github.com/vansh-khaneja/Chat-Multiple-Docs-Indexify.git```

```cd multi-pdf-chatbot```

2) Indexify setup:
Refer to this article for setting up Indexify extractors
[Download Indexify Extractors](https://docs.getindexify.ai/apis/extractors/pdf/#marker-extractor)

4) Install the required dependencies:

```pip install -r requirements.txt```

## Database Setup
Create the Indexify database graph by running:

```python db_setup.py```

## Running the Application
Start the Streamlit application with the following command:


```streamlit run main.py```


## Contact
For any questions or issues, please open an issue on this repository or contact us at [vanshkhaneja2004@gmail.com](vanshkhaneja2004@gmail.com).



Happy coding!


