# OpenQuant

## Description

OpenQuant is an open-source quantitative trading platform that provides a comprehensive set of tools for developing, testing, and deploying quantitative trading strategies. It is designed to be highly customizable and extensible, with a focus on providing a flexible and scalable framework for quantitative trading. The open-source app includes an open-source PyPi package called QuantPyML. This package includes a collection of tools for quantitative trading, including technical analysis, machine learning, and forecasting.

## Core Features

- main page
    - main page must display interactive stock chart
        - must have a selector for asset (includes stocks, etfs, indices, forex, futures, crypto)
        - must display both price and volume
        - must have a selector for time window (includes intrady, daily, weekly, monthly, yearly)
        - must have selector for technical indicators (includes indicators supported by QuantPyML).
        - must have selector for drawing tools (includes trendlines, rectangles, and circles)
        - must have a selector for forecasting models (includes models supported by QuantPyML)
  - main page must have a second chart that displays returns overlayed with volatility and access to the same filters as the first chart
- options page
    - must have an options profitability calculator that allows user to select price, strike, and expiration and displays the profitability chart and table
    - must have an options greeks calculator that allows user to select price, strike, and expiration and displays the greeks
    - must have an options strategy builder that allows user to select options and display the strategy chart and table
        - includes common strategies (butterfly, condor, iron condor, iron butterfly, straddle, strangle, and back ratio) and those supported by QuantPyML
       - must have a backtest tool that allows user to select options and display the strategy chart and table
- backtest page
    - tba, in notes
- forecast page
    - tba, in notes

## Tech Stack
- python
- streamlit
- pandas
- torch
- quantpyml
- huggingface
- openai
- anthropic

possibly
- pinecone
- redis
- supabase
- stripe
- dune
- yahoo finance
- alpaca
- ibkr

## Core Features

## Documentation

