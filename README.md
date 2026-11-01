# Local LLM Inference Using Ollama

## 1. Project Objective
To run a Large Language Model locally using Ollama and generate AI responses using Python.

## 2. Technologies Used
- Python
- Ollama
- Llama 3.2
- Pandas
- Requests
- Jupyter Notebook
- Matplotlib

## 3. Project Description
This project demonstrates Local Large Language Model (LLM) inference using Ollama.

The Llama 3.2 model processes 10 different prompts and generates responses locally through Python.

The generated responses are stored in CSV files and analyzed using word count and character count. A response comparison chart is also generated.

## 4. Folder Structure

```text
Local_LLM_Inference/
│
├── dataset/
│   ├── prompts.csv
│   ├── llm_responses.csv
│   ├── response_comparison.csv
│   ├── conversation_history.txt
│   └── response_length_chart.png
│
├── notebook/
│   └── Week8_Local_LLM_Inference.ipynb
│
├── local_llm.py
├── README.md
└── requirements.txt
```

## 5. Execution Steps
1. Install Python and Ollama.
2. Download the Llama 3.2 model.
3. Install required Python libraries.
4. Create a dataset containing 10 prompts.
5. Execute the Python program.
6. Generate AI responses using Ollama.
7. Save responses in CSV files.
8. Compare response lengths.
9. Visualize results using Matplotlib.

## 6. Results
- Successfully processed 10 prompts.
- Generated 10 AI responses.
- Stored responses in CSV format.
- Calculated word count and character count.
- Generated a response length comparison chart.

Average response length: 406.5 words.

## 7. Conclusion
The project successfully demonstrates local LLM inference using Ollama and Python. It explains how locally running AI models can generate responses and how the generated results can be stored, analyzed, and visualized.