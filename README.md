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