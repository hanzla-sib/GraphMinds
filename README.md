# GraphMinds

A project exploring LangGraph for building agent state machines and conversational AI workflows.

## Overview

This project demonstrates the basic concepts of LangGraph, including:
- Creating state graphs for agent workflows
- Defining agent states using TypedDict
- Building simple nodes that process and modify state
- Visualizing graph structures

## Installation

```bash
pip install langgraph
```

## Files

- `HelloWorldGraph.ipynb` - A Jupyter notebook demonstrating a basic "Hello World" agent using LangGraph
  - Creates an `AgentState` with a message field
  - Implements a greeting node that processes input messages and adds a greeting
  - Builds and compiles a state graph with entry and finish points
  - Includes graph visualization capabilities using Mermaid
  - Demonstrates how to invoke the compiled graph with input data
  - Shows how to access and display the processed results

## Getting Started

1. Install the required dependencies:
   ```bash
   pip install langgraph
   ```

2. Open and run the `HelloWorldGraph.ipynb` notebook to see a basic LangGraph implementation in action.
   - The notebook demonstrates creating a simple greeting agent
   - Run all cells to see the graph visualization and test the agent with sample input
   - Example: The agent processes "hanzla" and returns "Hello hanzla I am an agent. hows it going?"

## Key Concepts Demonstrated

- **StateGraph**: The main class for creating state machine graphs
- **AgentState**: TypedDict defining the structure of agent state
- **Nodes**: Functions that process and modify the agent state
- **Graph Compilation**: Converting the graph definition into an executable application
- **Graph Visualization**: Displaying the graph structure using Mermaid diagrams
- **Graph Invocation**: Running the compiled graph with input data and retrieving results
- **State Processing**: How nodes can access and modify incoming state data

## RAG Implementation

This project also includes a Retrieval-Augmented Generation (RAG) implementation that allows you to ask questions about restaurant reviews.

### Files

- `vector.py`: This script reads the `restaurant_reviews.csv` file, creates embeddings using `OllamaEmbeddings` with the `llama3.1` model, and stores them in a ChromaDB vector store. The vector store is persisted to the `./chroma_db` directory.
- `Rag.py`: This script loads the ChromaDB vector store and uses it as a retriever. It then creates a question-answering chain with a prompt that instructs an `OllamaLLM` model (`llama3.1`) to answer questions about a pizza restaurant based on the retrieved reviews. The script runs in a loop, allowing you to ask multiple questions.
- `restaurant_reviews.csv`: A CSV file containing restaurant reviews with columns for Title, Date, Rating, and Review.

### How to Run the RAG Application

1.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Create the vector store:**
    Run the `vector.py` script to create the ChromaDB vector store.
    ```bash
    python vector.py
    ```

3.  **Run the RAG application:**
    Run the `Rag.py` script to start the interactive question-answering session.
    ```bash
    python Rag.py
    ```
    You can then enter your questions in the terminal. Type 'exit' to quit.