# Systems and Software Engineering 1 Project: News Summary

This is the repository of the news summary project for the Systems and Software Engineering I lecture at the Goethe University Frankfurt, winter term 2022/23. The news project is a web-based application for text summarization that shows summarized news from The Guardian and BBC. The summaries are generated using OpenAI's GPT-3 Davinci model.

Our source code for this project can be found in the `src` folder. All other documents (assignments and presentations) are in the `documents` folder.

---

## Running the App

As summaries are generated using OpenAI's API, a working API key is needed. This should be saved as an environment variable with the name `OPENAI_API_KEY`.

To start the application, move into the `src` folder and run
> `streamlit run 01_Home.py`

## Testing
The unit test for this project was done using `PyTest`. Coverage was measured using the `coverage` library. To run the test, move into the `src` folder and run
> `coverage run -m pytest`

The results of the coverage test can be found in `src\htmlcov` as an interactive HTML file.

The questionaire for the usability test can be found [here](https://forms.gle/kuNmMMMCnLoKixCB6).

## Dependencies
The following are used in this project:
 >- Python 3.11
 >- Streamlit 1.17
>* BeautifulSoup 4.11
>* PILLOW 9.4
>* openAI 0.27
>* spacy 3.5
>* feedparser 6.0.10
>* pandas 1.5.3

