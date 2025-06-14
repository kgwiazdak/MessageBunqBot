# 🏦 bunq-Agent: AI-Powered Expense Assistant

A Discord-integrated AI agent for the bunq Hackathon 6.0 that helps you intelligently split costs, track expenses from receipt images, and generate fun end-of-period spending stories with images.

---

## 📜 About the Challenge

The bunq Hackathon 6.0 challenged developers to build autonomous AI agents leveraging the bunq API to revolutionize banking interactions. Solutions should go beyond basic chatbots—demonstrating intelligence, adaptability, and real user value.

> “Whether it’s helping users save money, make informed investment decisions, simplify expense tracking, or something entirely new—the possibilities are endless.”  
> — bunq Hackathon 6.0

---

## 🤖 bunq-Agent Overview

bunq-Agent is a fully Discord-integrated AI assistant that:

1. **Smart Receipt Splitting**  
   • Upload images of receipts in your Discord channel.  
   • AI parses itemized costs and suggests fair splits based on users’ preferences (e.g., “split equally,” “assign by item,” or “custom ratios”).

2. **Seamless bunq Integration**  
   • Uses bunq’s API to fetch account balances, recent transactions, and group payments.  
   • Automates payment requests and bill settlements directly in Discord.

3. **Spending Story Generator**  
   • At the end of each period (day/week/month), bunq-Agent compiles your spending data.  
   • Creates a fun, illustrated story summary—complete with graphs and annotated images—to share with friends or reflect on your habits.

---

## 🚀 Features

- **Receipt OCR & Parsing**  
  Leverages state-of-the-art OCR to extract line items, prices, and totals from photos.

- **AI-Driven Split Logic**  
  Customizable splitting strategies powered by natural-language prompts.

- **Transactional Automation**  
  Request, confirm, and settle bunq payments without leaving Discord.

- **Visual Storytelling**  
  Automatically generates an illustrated, narratively styled summary of your spending period.

- **Configurable Periods**  
  Define your own “period” (daily, weekly, monthly) for story generation.

---

## 🛠️ Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/bunq-agent.git
   cd bunq-agent
